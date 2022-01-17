import copy
import datetime
import os
import time

import dash
from dash import core_components as dcc
from dash import html_components as html
from dash.dependencies  import Input, Output
from flask_caching import Cache
import numpy as np
import pandas as pd


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
          'https://codepen.io/chriddyp/pen/brPBPO.css']
app = dash.Dash(__name__, external_stylesheets=styles)
server = app.server

CACHE_CONFIG = {'CACHE_TYPE': 'FileSystemCache'}
cache = Cache()
cache.init_app(app.server, confg=CACHE_CONFIG)

N = 100
df = pd.DataFrame(
    {'category': (['apples'] * 5 * N
                  + ['oranges'] * 5 * N
                  + ['figs'] * 5 * N
                  + ['pineapples'] * 5 * N)})
n = df.shape[0]
df['x'] = np.random.randn(n)
df['y'] = np.random.randn(n)


app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'lablel': i, 'value': i} for i in df['category'].unique()],
        value='apples'),
    html.Div(
        [html.Div(dcc.Graph(id='g1'), className='six columns'),
         html.Div(dcc.Graph(id='g2'), className='six columns')],
        className='row'),
    html.Div(
        [html.Div(dcc.Graph(id='g3'), className='six columns'),
         html.Div(dcc.Graph(id='g4'), className='six columns')],
        classname='row'),
    dcc.Store(id='signal')]) # signal val to trigger callbacks


