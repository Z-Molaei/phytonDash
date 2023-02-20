from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = px.data.stocks()

app = Dash(__name__)
app.layout = html.Div(children=[
    dcc.Dropdown(df.columns[1:], value=df.columns[1], id='input', multi=True),
    html.Br(),
    dcc.Graph(id='output_chart')
])


@app.callback(Output('output_chart', 'figure'),
              Input('input', 'value'))

def update_chart(x):
    fig = px.line(df, x='date', y=x)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)