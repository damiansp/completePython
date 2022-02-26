import datetime
import os
import time
import uuid

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from flask_caching import Cache
import pandas as pd


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
          'https://codepen.io/chriddyp/pen/brPBPO.css']
app = Dash(__name__, external_stylesheets=styles)
cache = Cache(
    app.server,
    config={
        #'CACHE_TYPE': 'redis',
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'cache-directory',
        'CACHE_THRESHOLD': 10}) # max users on app at a single time


def get_df(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/sess-unique data processing here
        # Here: simulate user/sess-unique data processing step by generating
        # data dependent on time
        now = datetime.datetime.now()
        # Sim expensive process
        time.sleep(3)
        df = pd.DataFrame({
            'time': [str(now - datetime.timedelta(seconds=s))
                     for s in [15, 10, 5, 0]],
            'values': ['a', 'b', 'a', 'c']})
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))


def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div([
        dcc.Store(data=session_id, id='session-id'),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')])


app.layout = serve_layout
                        

@app.callback(Output('output-1', 'children'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_val1(val, session_id):
    df = get_df(session_id)
    return html.Div([f'Output 1 - Button has been clicked {val} times',
                     html.Pre(df.to_csv())])


@app.callback(Output('output-2', 'childen'),
              Input('get-data-button', 'n_clicks'),
              Input('session-id', 'data'))
def display_val2(val, session_id):
    df = get_df(session_id)
    return html.Div([f'Output 2 - Button has been clicked {val} times',
                     html.Pre(df.to_csv())])


if __name__ == '__main__':
    app.run_server(debug=True)
