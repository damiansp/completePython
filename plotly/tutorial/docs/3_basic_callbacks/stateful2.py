# -*- coding: utf-8 -*-
import dash
from   dash.dependencies import Input, Output, State
import dash_core_components as dcc
#import dash_design_kit as ddk
import dash_html_components as html


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)


app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')])


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return (f'Button clicked {n_clicks} times. '
            f'Input 1 is {input1} and Input 2 is {input2}')


if __name__ == '__main__':
    app.run_server(debug=True)
