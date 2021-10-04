import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)

app.layout = html.Div([
    dcc.Input(id='n-multi', type='number', value=5),
    html.Table([html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
                html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
                html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
                html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
                html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')])])])


@app.callback(Output('square', 'children'),
              Output('cube', 'children'),
              Output('twos', 'children'),
              Output('threes', 'children'),
              Output('x^x', 'children'),
              Input('n-multi', 'value'))
def do_math(x):
    return x ** 2, x ** 3, 2 ** x, 3 ** x, x ** x


if __name__ == '__main__':
    app.run_server(debug=True)
    
                
