import numpy as np
import plotly
import plotly.graph_objects as go


N = 100
x = np.linspace(0, 1, N)
y0 = np.random.randn(N) + 5
y1 = np.random.randn(N)
y2 = np.random.randn(N) - 5

modes = ['markers', 'lines+markers', 'lines']
traces = [go.Scatter(x=x, y=y, mode=m, name=m)
          for y, m in zip([y0, y1, y2], modes)]
plotly.offline.plot(traces)
