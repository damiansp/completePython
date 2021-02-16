import numpy as np
import plotly
import plotly.graph_objects as go


N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
trace = go.Scatter(x=x, y=y, mode='markers')
plotly.offline.plot([trace], filename='scatter.html')
