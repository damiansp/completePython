import copy
import time

import dash
from dash import Dash, dcc, html, Input, Output
from flask_caching import Cache
import numpy as np
import pandas as pd


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
          'https://codepen.io/chriddyp/pen/brPBPO.css']
app = dash.Dash(__name__, external_stylesheets=styles)
server = app.server

CACHE_CONFIG = {'CACHE_TYPE': 'FileSystemCache'}
cache = Cache()
cache.init_app(server, config=CACHE_CONFIG)

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


# Perform expensive computations in this "global store". These computations are
# cachedin a globally available memory store which is available across processes
# and for all time
@cache.memoize()
def global_store(val):
    # simulate expensive query
    print(f'Computing value for {val}...')
    time.sleep(3)
    return df[df.category == val]


def generate_figure(val, fig):
    fig = copy.deepcopy(fig)
    filtered_df = global_store(val)
    fig['data'][0]['x'] = filtered_df.x
    fig['data'][0]['y'] = filtered_df.y
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b': 20, 't': 10}}
    return fig


@app.callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_val(val):
    # compute and send signal when done
    global_store(val)
    return val


@app.callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(val):
    # generate_fig() gets data from <global_store>. The data have already been
    # computed by <compute_val> and result is stored in global cache
    return generate_figure(
        val,
        {'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}}}]})


@app.callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(val):
    return generate_figure(
        val,
        {'data': [{
            'type': 'scatter',
            'mode': 'lines',
            'line': {'shape': 'spline', 'width': 0.5}}]})


@app.callback(Output('graph-3', 'figure'), Input('signal', 'data'))
def update_graph_3(val):
    return generate_figure(val, {'data': [{'type': 'histogram2d'}]})


@app.callback(Output('graph-4', 'figure'), Input('signal', 'data'))
def update_graph_4(val):
    return generate_figure(val, {'data': [{'type': 'histogram2dcontour'}]})


if __name__ == '__main__':
    app.run_server(debug=True, processes=4, threaded=False)
