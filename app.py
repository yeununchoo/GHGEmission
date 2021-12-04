import dash
from dash import dcc # dash core components
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H2(children='Greetings!'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [5, 7, 2], 'type': 'line'},
            ],
            'layout': {
                'title': 'Example Graph'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
