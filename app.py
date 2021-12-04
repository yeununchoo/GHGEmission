import dash
from dash import dcc # dash core components
from dash import html


COLORS = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', '/assets/style.css']

def page_header():
    """
    Returns the page header as a dash `html.Div`
    """
    return html.Div(id='header', children=[
        html.Div([html.H3('Estimating Weekly Greenhouse Gas Emission')],
                 className="ten columns"),
        html.A([html.Img(id='logo', src=app.get_asset_url('github.png'),
                         style={'height': '35px', 'paddingTop': '7%'}),
                html.Span('Github Repo', style={'fontSize': '2rem', 'height': '35px', 'bottom': 0,
                                                'paddingLeft': '4px', 'color': '#a3a7b0',
                                                'textDecoration': 'none'})],
               className="two columns row",
               href='https://github.com/yeununchoo/GHGEmission'),
    ], className="row")


def description():
    """
    Returns overall project description in markdown
    """
    return html.Div(children=[dcc.Markdown('''
        # Estimating Weekly Greenhouse Gas Emission
        

        This website is currently under conustruction.

        Click the github link in the header for more infomation. 

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.Div([
        page_header(),
        html.Hr(),
        description(),
    ], className='row', id='content')
])


if __name__ == '__main__':
    app.run_server(debug=True)
