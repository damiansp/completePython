import plotly
from   plotly.graph_objects import Layout, Scatter


plotly.offline.plot({'data': [Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 2])],
                     'layout': Layout(title='Hello, plotly!')})
