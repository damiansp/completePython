import ssl

import dash
import dash_core_components as dcc
import dash_html_components as html
from   dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

ssl._create_default_https_context = ssl._create_unverified_context


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/'
                 'gapminderDataFiveYear.csv')
app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(id='year-slider',
               min=df.year.min(),
               max=df.year.max(),
               value=df.year.min(),
               marks={str(year): str(year) for year in df.year.unique()},
               step=None)])


@app.callback(Output('graph-with-slider', 'figure'),
              Input('year-slider', 'value'))
def update_figure(year):
    filtered_df = df[df.year == year]
    fig = px.scatter(filtered_df,
                     x='gdpPercap',
                     y='lifeExp',
                     size='pop',
                     color='continent',
                     hover_name='country',
                     log_x=True,
                     size_max=55)
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
