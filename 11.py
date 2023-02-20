from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.iris()

app = Dash(__name__)
app.layout = html.Div(children=[
    html.Label('X axes: '),
    dcc.RadioItems(df.columns[:4], value=df.columns[0], id='i1'),
    html.Br(),
    html.Label('Y axes: '),
    dcc.RadioItems(df.columns[:4], value=df.columns[1], id='i2'),
    html.Br(),
    dcc.Graph(id='chart')
])

@app.callback(Output('chart', 'figure'),
              Input('i1', 'value'),
              Input('i2', 'value'))

def update(x, y):
    fig = px.scatter(df, x=x, y=y, color='species')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)