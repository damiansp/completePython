import dash
from   dash import dcc, html
from   dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.express as px


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)
df = pd.DataFrame({f'Col{i + 1}': np.random.rand(30) for i in range(6)})


app.layout = html.Div(
    [html.Div(dcc.Graph(id=f'g{i + 1}', config={'displayModeBar': False}),
              className='four columns')
     for i in range(3)],
    className='row')


def get_fig(df, x, y, selected, selected_local):
    if selected_local and selected_local['range']:
        ranges = selected_local['range']
        selected_bounds = {'x0': ranges['x'][0], 'x1': ranges['x'][1],
                           'y0': ranges['y'][0], 'y1': ranges['y'][1]}
    else:
        selected_bounds = {'x0': df[x].min(), 'x1': df[x].max(),
                           'y0': df[y].min(), 'y1': df[y].max()}
    # Set which points are selected with the 'selected' property and style those
    # points with the 'selected' and 'unselected' attributes
    fig = px.scatter(df, x=df[x], y=df[y], text=df.index)
    fig.update_traces(
        selectedpoints=selected,
        customdata=df.index,
        mode='markers+text',
        marker={'color': 'rgba(116, 217, 0, 0.7)', 'size': 20},
        unselected={'marker': {'opacity': 0.3},
                    'textfont': {'color': 'rgba(0, 0, 0, 0)'}})
    fig.update_layout(margin={'l': 20, 'r': 0, 'b': 15, 't': 5},
                      dragmode='select',
                      hovermode=False)
    fig.add_shape(
        dict({'type': 'rect',
              'line': {'width': 1, 'dash': 'dot', 'color': 'darkgrey'}},
             **selected_bounds))
    return fig


@app.callback(Output('g1', 'figure'),
              Output('g2', 'figure'),
              Output('g3', 'figure'),
              Input('g1', 'selectedData'),
              Input('g2', 'selectedData'),
              Input('g3', 'selectedData'))
def callback(sel1, sel2, sel3):
    selected = df.index
    for s in [sel1, sel2, sel3]:
        if s and s['points']:
            selected = np.intersect1d(selected,
                                      [p['customdata'] for p in s['points']])
    return [get_fig(df, 'Col1', 'Col2', selected, sel1),
            get_fig(df, 'Col3', 'Col4', selected, sel2),
            get_fig(df, 'Col4', 'Col6', selected, sel3)]


if __name__ == '__main__':
    app.run_server(debug=True)


            
            
