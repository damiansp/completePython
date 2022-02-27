import ssl

import dash
import dash_html_components as html
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
data_url = (
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv'
)
df = pd.read_csv(data_url)


def generate_table(df, max_rows=10):
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in df.columns])),
        html.Tbody([
            html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
            for i in range(min(len(df), max_rows))])])
    return table


ex_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=ex_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Ag Exports (2011)'),
    generate_table(df)])


if __name__ == '__main__':
    app.run_server(debug=True)
