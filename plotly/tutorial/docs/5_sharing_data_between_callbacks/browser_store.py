import dash
from   dash import dcc, html
from   dash.dependencies import Input, Output


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)
df = pd.DataFrame({f'Col{i + 1}': np.random.rand(30) for i in range(6)})


app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),
    dcc.Store(id='intermediate-value') # stores intermed value
])


@app.callback(Output('intermediate-value', 'data'), Input('dropdown', 'value'))
def clean_data(val):
    # expensive processing step
    clean_df = slow_processing_step(val)
    return clean_df.to_json(date_format='iso', orient='split')


@app.callback(Outuput('graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(json_data):
    df = pd.read_json(json_data, orient='split')
    fig = create_figure(df)
    return fig


@app.callback(Output('table', 'children'), Input('intermediate-value', 'data'))
def update_table(json_data):
    df = pd.read_json(json_data, orient='split')
    table = create_table(df)
    return table


if __name__ == '__main__':
    app.run_server(debug=True)


            
            
