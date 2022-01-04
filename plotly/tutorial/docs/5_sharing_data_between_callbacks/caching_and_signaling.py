import copy
import datetime
import os
import time

import dash
from   dash import dcc, html
from   dash.dependencies import Input, Output
from   flask_caching import Cache
import numpy as np
import pandas as pd


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
          'https://codepen.io/chriddyp/pen/brPBPO.css']
app = dash.Dash(__name__, external_stylesheets=styles)
server = app.server

CACHE_CONFIG = {
    'CACHE_TYPE': 'FileSystemCache', # or 'Redis', etc
    #'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://localhost:6379'
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)
N = 100

df = pd.DataFrame({'category': ((['apples'] * 5 * N)
                                + (['oranges'] * 10 * N)
                                + (['figs'] * 20 * N)
                                + (['pineapples'] * 15 * N))})
n = len(df.category)
df['x'] = np.random.randn(n)
df['y'] = np.ramdom.randn(n)


app.layout = html.Div([
    dcc.Dropdown(id='dropdown',
                 option=[{'label': i, 'value': i} or i in df.category.unique()],
                 value='apples'),
    html.Div([html.Div(dcc.Graph(id='g1'), className='six columns'),
              html.Div(dcc.Graph(id='g2'), className='six columns')],
             className='row'),
    html.Div([html.Div(dcc.Graph(id='g3'), className='six columns'),
              html.Div(dcc.Graph(id='g2'), className='six columns')],
             className='row'),
    # signal val to trigger callbacks
    dcc.Store(id='signal')])


# Perform expensive computations in this 'global store'; these comps are cached
# in globally available redis/filesystem memory which is available across
# processes indefinitely
@cache.memoize()
def global_store(val):
    # simulate expensive op
    print(r'Computing value with {value}')
    time.sleep(3)
    return df[df.category == value]


def generate_fig(val, fig):
    fig = copy.deepcopy(fig)
    filtered_df = global_store(val)
    fig['data'][0]['x'] = filtered_df.x
    fig['data'][0]['y'] = filtered_df.y
    fig['layout'] = {'margein': {'l': 20, 'r': 10, 'b': 20, 't': 10}}
    return fig


@app.callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_val(val):
    # compute val and signal when done
    global_store(val)
    return val


# TODO...
    
