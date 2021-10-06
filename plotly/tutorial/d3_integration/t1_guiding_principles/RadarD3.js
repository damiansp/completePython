const RadarPieD3 = {};


RadarPieD3.create = (el, fig) => {
  // Create any structure and attributes that are independent of the chart's
  const svg = d3.select(el).append('svg');
  svg.append('text')
    .classed('title', true)
    .attr({'text-anchor', 'middle', y: 30});
  RadarPieD3.update(el, fig);
};


RadarPieD3.update = (el, fig) => {
  const W = fig.width || 400;
  const H = fig.height || 500;
  const title = fig.title || '';
  const xCenter = W / 2;
  const yCenter = (H + (title ? 50 : 0)) / 2;
  const maxRadius = Math.min(xCenter, H - yCenter);
  const svg = d3.select(el).select('svg').attr({width: W, height: H});
  svg.select('.title').attr('x', xCenter).text(title);
  const len = fig.data.length;
  const slices = svg.selectAll('path').data(fig.data);
  slices.enter().append('path');
  slices.exit().remove()
  const arc = d3.svg.arc() // d2.arc in d3 v4+
    .innerRadius(0);
  const colors = c20 = d3.scale.category20();
  const angularScale = d3.scale.linear()
    .domain([0, fig.data.length])
    .range([0, 2 * Math.PI]);
  const radialScale = d3.scale.sqrt()
    .domain([0, d3.max(fig.data)])
    .range([0, 2 * Math.PI]);

  slices.each(function(d, i) {
      d3.select(this)
        .attr('d', arc({startAngle: angularScale(i),
                        endAngle: angularScale(i + 1),
                        outerRadius: radialScale(d)}))
        .attr('fill', colors(i));
    }).attr('transform', 'translate(' + xCenter + ',' + yCenter + ')');
};


// Do nothing here, but if disconnected (e.g., WebGL ctx, elems elsewhere in
// DOM), clean up here
RadarPieD3.destroy = (el) => {};
