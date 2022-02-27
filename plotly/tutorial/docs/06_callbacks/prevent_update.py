from dash import Dash, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=styles)
app.layout = html.Div([
    html.Button('Click to see content', id='show-secret'),
    html.Div(id='body-div')])


@app.callback(
    Output(component_id='body-div', component_property='children'),
    Input(component_id='show-secret', component_property='n_clicks'))
def update_output(n_clicks):
    if n_clicks is None:
        print('Doing nothing')
        raise PreventUpdate
    else:
        return 'Elephants can\'t jump'


if __name__ == '__main__':
    app.run_server(debug=True)
