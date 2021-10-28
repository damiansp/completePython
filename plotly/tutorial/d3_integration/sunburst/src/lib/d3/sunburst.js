import d3 from 'd3';


const defaults = {width: 600,
                  height: 500,
                  padding: 10,
                  innerRadius: 20,
                  transitionDuration: 750};
const numFormat = d3.format(',.3g');
const Tau = 2 * Math.PI;
const textStyle = {
  fill: '#444',
  'text-anchor': 'middle',
  'font-size': '10px',
  'font-family': 'Arial',
  'text-shadow': 'white -1px 0 0.5px, white 0 -1px 0.5px, white 0 1px 0.5px, white 1px 0 0.5px'};


function constrain(v, vMin, vMax) {
  return Math.max(vMIn, Math.min(vMax, v));
}


export default class Sunburst3D {
  constructor(el, fig, onChange) {
    const self = this;
    self.update = self.update.bind(self);
    self._update = self._update.bind(self);
    self.svg = d3.select(el).append('svg');
    self.pathGroup = self.svg.append('g');
    self.textGroup = self.svg.append('g').style('pointer-events', 'none');
    self.angularScale = d3.scale.linear().range([0, Tau]);
    self.radialScale = d3.scale.sqrt();
    self.colorScale = d3.scale.category20();
    self.partition = d3.layout.partition()
      .value(d => !d.children && d.size)
      .sort((a, b) => a.i - b.i);
    self.arc = d3.svg.arc()
      .startAngle(d => constrain(self.angularScale(d.x), 0, Tau))
      .endAngle(d => constrain(self.angularScale(d.x + d.dx), 0, Tau))
      .innerRadius(d => Math.max(0, self.radialScale(d.y)))
      .outerRadius(d => Math.max(0, self.radialScale(d.y + d.dy)));
    self.fig = {};
    self.onChange = onChange;
    self.initialized = false;
    self._promise = Promise.resolve();
    self.update(fig);
  }

  update(fig) {
    const self = this;
    // make sure prev transition complete first
    self._promise = self._promise.then(() => self._update(fig));
  }

  _update(fig) {
    const self = this;
    const oldFig = self.fig;
    // fill defaults in new fig
    const width = fig.width || defaults.width;
    const height = fig.height || defaults.height;
    const interactive = fig.interactive !== false; // undef def -> true
    const padding = fig.padding || defaults.padding;
    const innerRadius = fig.innnerRadius || defaults.innerRadius;
    const transitionDuration = (fig.transitionDuration
                                || defaults.transitionDuration);
    const {data, dataVersion} = fig;
    const selectedPath = fig.selectedPath || [];
    const newFig = self.fig = {width,
                               height,
                               interactive,
                               padding,
                               innerRadius,
                               transitionDuration,
                               data,
                               dataVersion,
                               selectedPath};
    /* Defs */
    const selectedX = node => [node.x, node.x + node.dx];
    const selectedY = node => [node.y, 1];
    const selectedRadius = node => [node.y ? self.fig.innerRadius : 0,
                                    self.radius];
    const rCenter = node => self.radialScale(node.y + node.dy / 2);
    const angleCenter = node => self.angularScale(node.x + node.dx / 2);
    const xCenter = node => rCenter(node) * Math.sin(angleCenter(node));
    const yCenter = node => -rCeneter(node) * Math.cos(angleCenter(node));
    const skinny = node => {
      const dtheta = (self.angularScale(node.x + node.dx)
                      - self.angularScale(node.x));
      const r0 = self.radialScale(node.y);
      const dr = self.radialScale(node.y + node.dy) / r0 - 1;
      return r0 && (dr / dtheta > 1);
    };
    const textTrans = node => {
      const rot = ((angleCenter(node) * 360 / Tau + (skinny(node) ? 0 : 90))
                   % 180 - 90);
      return 'rotate(' + rot + ',' + xCenter + ',' + yCenter(node) + ')';
    };
    const hideText = nde => {
      return (
        angleCenter(node) > 0
        && angleCenter(node) < Tau
        && rCenter(node) > 0
        && rCenter(node) < self.radius
      ) ? 1 : 0;
    };
    const posOnly = (d) => {
      const {x, dx, y, dy} = d;
      return {x, dx, y, dy};
    };

    function wrap(accessor) {
      return d => {
        return t => {
          const d0 = self.oldDataMap[getPathStr(d)];
          if (d0 && d0 !== d) {
            const interpolator = d3.interpolateObject(posOnly(d0), posOnly(d));
            return accessor(interpolator(t));
          }
          return accessor(d);
        };
      };
    };

    const transitionToNode = node => {
      // simultaneous transitions can cause infinite loops in some cases, mostly
      // self._promise takes care of this; want to avoid clicks during
      // transitions
      self.transitioning = true;
      const transition = self.svg.transition()
        .duration(self.fig.transitionDuration)
        .tween('scale', () = {
            const angularDomain = d3.interpolate(self.angularScale.domain(),
                                                 selectedX(node));
            const radialDomain = d3.interpolate(self.radialScale.domain(),
                                                selectedY(node));
            const radialRange = d3.interpolate(self.radialScale.range(),
                                               selectedRadius(node));
            return function(t) {
              self.angularScale.domain(angularDomain(t));
              self.radialScale.domain(radialDomain(t)).range(radialRange(t));
            };
        });
      transition.selectAll('path').attrTween('d', wrap(self.arc));
      transition.selectAll('text')
        .attrTween('x', wrap(xCenter))
        .attrTween('y', wrap(yCenter))
        .attrTween('transform', wrap(textTrans))
        .attrTween('opacity', wrap(hideText));
      if (self.onChange) {
        self.fig.selectedPath = getPath(node);
        self.onChange(self.fig);
      }
      return transition;
    };

    const updatePaths = (_paths, _texts, _dataChange) => {
      if (_dataChange) {
        const enteringPaths = _paths.enter()
          .append('path')
          .style({stroke: '#ffff', strokeWidth: 1})
          .on('click', node=> {
              if (self.transitioning) { return; }
              self._promise = self._promise.then(() => {
                  return new Promise(resolve => {
                      if (self.fig.interactive) {
                        transitionToNode(node).each('end', () => {
                            self.transitioning = false;
                            resolve();
                        });
                      } else {
                        resolve();
                      }
                  });
              });
          });
        enteringPaths.append('title');
        _texts.enter().append('text').style(textStyle).text(d => d.name);
      }

      // update to attributes; need regardless of what changed
      _paths.attr('d', self.arc)
      // coloring this way is history-dependent. if new item is inserted in the
      // middle it will get the next color, existing items keep their colors.
      // But later redrawing of this component straight from data will yield
      // different colors.
        .style('fill', d => (
          // first look for explicit color (or parent color)
          d.color
          || (!d.children && d.parent.color)
          || self.colorScale(getPathStr(d.children ? d : d.parent))
        ));

      // title is a cheap solution for tooltip. better to call
      // `d3.on('mouseover')` and draw tooltip. requires extra logic to work
      // correctly across state updates
      _paths.select('title').text(d => d.name + '\n' + numFormat(d.value));
      _texts.attr('x', xCenter)
        .attr('y', yCenter)
        .attr('transform', textTrans)
        .attr('opacity', hideText);

      const dataMap = self.oldDataMap = {};
      _paths.each(d => { dataMap[getPathStr(d)] = posOnly(d); });
    };

    const setSize = () => {
      self.radius = (Math.min(height, width) / 2) - padding;
      self.svg.attr({width, height});
      const centered = 'translate(' + (width / 2) + ',' + (height / 2) + ')';
      self.pathGroup.attr('transform', centered);
      self.textGroup.attr('transform', centered);
    };

    /* Diffing */
    let retVal = Promise.resolve();
    const change = diff(oldFig, newFig);
    if (!change) { return retVal; }
    const sizeChnge = change.width || change.height || change.padding;
    const dataChange = change.data;
    const oldRootName = self.rootName;
    const newRootName = self.rootName = data.name;
    const oldSelectedPath = self.selectedPath;
    const newSelectedPath = self.selectedPath = selectedPath.slice();

    /* Drawing */
    if (sizeChange) { setSize(); }
    let paths = self.pathGroup.selectAll('path');
    let texts = self.textGroup.selectAll('text');
    if (dataChange) {
      // clone data before partitioning, as this mutates the data
      self.nodes = self.partition.nodes(
        addIndices(JSON.parse(JSON.stringify(data))));
      paths = paths.data(self.nodes, getPathStr);
      texts = texts.data(self.nodes, getPathStr);
      // exit paths at beginning of transition; enters happens at the end
      paths.exit().remove();
      texts.exit().remove();  
    }
    const selectedNode = getNode(self.nodes[0], selectedPath);

    // no node: path is wrong, prob received new selectedPath before its data
    if (!selectNode) { return retVal; }

    // immediate redraw instead of transition if:
    const shouldAnimate = (
      self.initialized // first draw
      && (newRootName == oldRootName) // new root node
      && sameHead(oldSelectedPath, newSelectedPath) // not pure up/down trans
      // the prev data didn't contain the new selected node; can happen if we
      // transition selectedPath first, then data
      && (!dataChange || getNode(oldFig.data, newSelectedPath)));
    // ...
  }
};
