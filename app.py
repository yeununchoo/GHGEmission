import dash
from dash import dcc # dash core components
from dash import html
import plotly.express as px

import numpy as np
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', '/assets/style.css']

def page_header():
    """
    Returns the page header as a dash `html.Div`
    """

    return html.Div(id='header', children=[
        html.Div([html.H3('Estimating Weekly Greenhouse Gas Emission')],
                 className="ten columns"),
        html.A(html.Img(id = 'logo', 
                         src = app.get_asset_url('github.png'),
                         style = {'height': '35px', 'paddingTop': '10%', 'float':'right'}
                         ),
               className="two columns",
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
        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

def static_section():
    """
    Returns static section
    """
    return html.Div(children=[dcc.Markdown('''
        ## Greenhouse Gas Emission vs GDP
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat ante vel nisl pellentesque, id ornare tortor sodales. Pellentesque commodo ligula eu elit elementum porttitor. Proin vitae sem tellus. Phasellus nec enim tellus. Aliquam eget erat fringilla nisl congue porttitor vel vitae felis. Vivamus pellentesque felis sit amet leo fringilla ullamcorper. Donec consequat et urna et malesuada. Proin malesuada magna quis ex feugiat lacinia.

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

#https://www.w3schools.com/colors/colors_picker.asp?color=23272c

def static_figure():
    """
    Returns the static ghg vs gdp scatter plot
    """
    
    df_static = pd.read_parquet("results/df_static.parquet")  
    fig_scatter = px.scatter(df_static, 
                             x = "GDP", 
                             y = "GHG", 
                             color = "Country",
                             hover_data = ["Year"], 
                             log_x = True, 
                             log_y = True,
                             #title = "GH Gas Emission vs GDP",
                             labels={'GDP':'GDP, Billion USD', 
                                     'GHG':'GHG, Tonnes of CO2 Equivalent'}, 
                             height = 700
                            )
                            
    fig_scatter.update_layout(legend=dict(
                              orientation="h",
                              yanchor="bottom",
                              y=1.02,
                              xanchor="right",
                              x=1))
                              
    fig_scatter.update_layout(font=dict(size = 20))
                              
    fig_scatter.update_layout(template='plotly_dark',
                              plot_bgcolor='#2d3339',
                              paper_bgcolor='#5b6571')
    
    fig_scatter.update_xaxes(gridcolor='#717e8e')
    fig_scatter.update_yaxes(gridcolor='#717e8e')
    
    return html.Div(children=[dcc.Graph(figure = fig_scatter, 
                                        className = 'offset-by-one nine columns', 
                                        style={'paddingLeft': '5%'})], 
                    className="row")

def weekly_section():
    """
    Returns static section
    """
    return html.Div(children=[dcc.Markdown('''
        ## Weekly Estimation
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat ante vel nisl pellentesque, id ornare tortor sodales. Pellentesque commodo ligula eu elit elementum porttitor. Proin vitae sem tellus. Phasellus nec enim tellus. Aliquam eget erat fringilla nisl congue porttitor vel vitae felis. Vivamus pellentesque felis sit amet leo fringilla ullamcorper. Donec consequat et urna et malesuada. Proin malesuada magna quis ex feugiat lacinia.

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

def weekly_figure():
    """
    Returns the static ghg vs gdp scatter plot
    """
    
    df_weekly = pd.read_parquet("results/df_weekly.parquet")  
    fig_bar = px.bar(df_weekly, 
               x = "Week", 
               y = "GHG_weekly", 
               color = "Country",
               #title = "Weekly GH Gas Emission Prediction", 
               labels={'GHG_weekly':'GHG, Tonnes of CO2 Equivalent'},
               height = 700
              )

    fig_bar.update_layout(xaxis_type='category')
    
    fig_bar.update_layout(legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1)) 
    
    fig_bar.update_layout(font=dict(size = 20))
    
    fig_bar.update_layout(template='plotly_dark',
                          plot_bgcolor='#2d3339',
                          paper_bgcolor='#5b6571')
    
    fig_bar.update_xaxes(showgrid = False)
    fig_bar.update_yaxes(gridcolor='#717e8e', 
                         layer = 'above traces')
    
    return html.Div(children=[dcc.Graph(figure = fig_bar, 
                                        className = 'offset-by-one nine columns', 
                                        style={'paddingLeft': '5%'})], 
                    className="row")

def inforgraphic():
    """
    Returns static section
    """
    return html.Div(children=
        [dcc.Markdown('''
            ## Better Understand Carbon Footprint
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat ante vel nisl pellentesque, id ornare tortor sodales. Pellentesque commodo ligula eu elit elementum porttitor. Proin vitae sem tellus. Phasellus nec enim tellus. Aliquam eget erat fringilla nisl congue porttitor vel vitae felis. Vivamus pellentesque felis sit amet leo fringilla ullamcorper. Donec consequat et urna et malesuada. Proin malesuada magna quis ex feugiat lacinia.

            ''', 
                className='eleven columns', 
                style={'paddingLeft': '5%'}
            ),
            html.Img(src=app.get_asset_url('infographic.png'),
                     className='offset-by-one nine columns', 
                     style={'paddingLeft': '5%'}
            )
        ], className="row")

def conclusion():
    """
    Returns conclusion in markdown
    """
    return html.Div(children=[dcc.Markdown('''
        ## Future Works
        
        This website is currently under conustruction.

        Click the [github link](https://github.com/yeununchoo/GHGEmission) in the header for more infomation. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat ante vel nisl pellentesque, id ornare tortor sodales. Pellentesque commodo ligula eu elit elementum porttitor. Proin vitae sem tellus. Phasellus nec enim tellus. Aliquam eget erat fringilla nisl congue porttitor vel vitae felis. Vivamus pellentesque felis sit amet leo fringilla ullamcorper. Donec consequat et urna et malesuada. Proin malesuada magna quis ex feugiat lacinia.

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

def references():
    """
    Returns conclusion in markdown
    """
    return html.Div(children=[dcc.Markdown('''
        ## References
        
        - OECD Weekly GDP Tracker
        - OECD Greenhouse Gas Emissions
        - IMF GDP 
        - Greenhouse Gas Equivalencies Calculator, US Environmental Protection Agency 

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.Div([
        page_header(),
        html.Hr(),
        description(),
        static_section(),
        static_figure(),
        weekly_section(),
        weekly_figure(),
        inforgraphic(),
        conclusion(),
        references(),
    ], className='row', id='content')
])


if __name__ == '__main__':
    app.run_server(debug=True)
