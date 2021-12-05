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
        html.A([html.Img(id = 'logo', 
                         src = app.get_asset_url('github.png'),
                         style = {'height': '35px', 'paddingTop': '7%'}),
                html.Span('Github Repo', style={'fontSize': '2rem', 
                                                'height': '35px', 
                                                'bottom': 0,
                                                'paddingLeft': '4px', 
                                                'color': '#a3a7b0',
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

        Click the [github link](https://github.com/yeununchoo/GHGEmission) in the header for more infomation. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat ante vel nisl pellentesque, id ornare tortor sodales. Pellentesque commodo ligula eu elit elementum porttitor. Proin vitae sem tellus. Phasellus nec enim tellus. Aliquam eget erat fringilla nisl congue porttitor vel vitae felis. Vivamus pellentesque felis sit amet leo fringilla ullamcorper. Donec consequat et urna et malesuada. Proin malesuada magna quis ex feugiat lacinia.

        Maecenas quis imperdiet risus, non tempor dolor. Nulla diam risus, commodo tincidunt lacus id, molestie faucibus mauris. Phasellus arcu nisl, ornare ac mollis quis, tincidunt vitae augue. Sed suscipit, elit vitae posuere faucibus, neque erat congue erat, et consequat nunc magna et dolor. Vivamus ac lectus malesuada, volutpat quam sit amet, congue nisl. Quisque quam nulla, gravida at laoreet ac, rutrum eu elit. Vestibulum sapien enim, varius quis sagittis eget, posuere a est. Vestibulum quis tellus vel nunc varius aliquam lobortis finibus metus. Nam vel tincidunt lacus. Fusce posuere semper orci id dapibus. Aenean in euismod eros, ac cursus diam. Suspendisse ac eleifend est.

        Nullam porttitor tellus eget sem laoreet egestas. Vivamus tristique purus ex, quis accumsan orci lacinia a. Maecenas id imperdiet nunc. In vitae dui sodales, accumsan libero consectetur, porttitor nisl. Quisque in sollicitudin magna. Mauris imperdiet id est ac cursus. Vivamus iaculis, elit sit amet tempus consectetur, nunc quam commodo diam, ut ornare nisl leo non diam. Pellentesque id orci eget urna fermentum pulvinar at in purus. Ut condimentum tempor sapien eu finibus. Mauris mi dolor, tempus accumsan facilisis at, interdum sed enim. Sed iaculis lectus id diam cursus, eu dignissim felis fermentum. Etiam congue nulla non magna pellentesque, nec luctus augue condimentum. Aenean id ligula finibus arcu pharetra faucibus vitae quis ex. Donec cursus pharetra ante vitae dignissim. 

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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
