import d3 from 'd3';


const dflts = {width: 600,
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
    /* Continue here */
  }
};
