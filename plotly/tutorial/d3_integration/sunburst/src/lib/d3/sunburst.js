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
    }

    const transtionToNode /* todo... */
  }
};
