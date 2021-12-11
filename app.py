import dash
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output, State

import plotly.express as px

import numpy as np
import pandas as pd

#https://www.w3schools.com/colors/colors_picker.asp?color=23272c

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
        
        Let’s try to estimate weekly greenhouse gas emissions. Have you thought of how many tonnes of CO2 are released into the atmosphere every week? 

        If you have wondered about it, welcome to our website. We are three students from Brown University’s Data Science Masters program. This website was created with Python, Plotly Dash, and Heroku as a part of a homework project for the course DATA1050: “Data Engineering”. This is an open-source project, and you are welcome to visit our Github [repository](https://github.com/yeununchoo/GHGEmission) for more details. 

        Using the public data on greenhouse gas emissions and GDP from the OECD and IMF across several recent years and countries, we have been able to build some interesting visualizations and regression models on how much greenhouse gases emissions each country in each year can expect based on the amount of GDP they generate. Our work focuses on the G7 countries in the past 5 years before the pandemic, from 2015 to 2019. Through the figures and information on the website, we hope to raise awareness about how industrial and personal behaviors can affect GHG, thereby empowering people and corporations to take more actions to combat climate change and protect the environment. 

        We hope more people can join us in having a moment to think about how our daily or industrial activities can add to GHG emissions and affect our environment negatively. 
        ''', 
            className='eleven columns', 
            style={'paddingLeft': '5%'}
            )
            ], 
        className="row")

def static_section():
    """
    Returns static section
    """
    return html.Div(children=[dcc.Markdown('''
        ## Greenhouse Gas Emission vs GDP
        
        Here is our interactive plot for the relationship between GHG and GDP. The GHG data is from the OECD and the GDP data is from the IMF. Here, you can see the data for the G7 countries from the years 2015 to 2019. 

        Please click on the radio buttons here to select different greenhouse gases of your interest, and as you make a selection, you can see a different graph generated for each country. This plot is updated whenever new data become available from the OECD. If you come back to our website every week, even if you select the same kind of greenhouse gases, you will get a new graph, because the data is continuously updated!
        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

def static_radio_button():
    """
    Returns radio buttons
    """
    return html.Div(children = [
            dcc.Markdown('''
                Choose the greenhouse gas here
                ''', 
                className='offset-by-one nine columns', 
                style={'paddingLeft': '5%'}),    
            dcc.RadioItems(
                id = 'static_ghg',
                options=[
                    {'label': 'Total Greenhouse Gases', 'value': 'GHG'},
                    {'label': 'Carbon Dioxide', 'value': 'CO2'},
                    {'label': 'Methane', 'value': 'CH4'},
                    {'label': 'Nitrous Oxide', 'value': 'N2O'},
                    {'label': 'Hydrofluocarbons', 'value': 'HFC'},
                    {'label': 'Perfluorocarbons', 'value': 'PFC'},
                    {'label': 'Sulphur Hexaflouride', 'value': 'SF6'},
                ],
                value='GHG',
                labelStyle={'font-size': '2rem'}, 
                className="offset-by-two seven columns"
            ), 
            dcc.Markdown('''
                Also, you can click on the country name on the graph to include/exclude it.
                
                Emission vs GDP  
                ''', 
                className='offset-by-one nine columns', 
                style={'paddingLeft': '5%'})]
            )

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
        
        Here is our interactive plot for the analysis we have performed on the dynamic data from the OECD, combined with the previous GHG vs GDP analysis. In this analysis, we use the weekly GDP data to estimately weekly GHG emission. More precisely, after performing a log-log regression of GHG on GDP, we use the estimated coefficients from this model and create an interactive bar plot, with the independent variable being the GDP and the dependent variable being the weekly GHG emission, and the color of the dots being each of the G7 countries.

        Please click on the radio buttons here to select different greenhouse gases of your interest, and as you make a selection, you can see a different graph generated for each country. This plot is updated whenever new data become available from the OECD. If you come back to our website every week, even if you select the same kind of greenhouse gases, you will get a new graph, because the data is continuously updated!
        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")
        
def weekly_radio_button():
    """
    Returns radio buttons
    """
    return html.Div(children = [
            dcc.Markdown('''
                Choose the greenhouse gas here
                ''', 
                className='offset-by-one nine columns', 
                style={'paddingLeft': '5%'}),    
            dcc.RadioItems(
                id = 'weekly_ghg',
                options=[
                    {'label': 'Total Greenhouse Gases', 'value': 'GHG'},
                    {'label': 'Carbon Dioxide', 'value': 'CO2'},
                    {'label': 'Methane', 'value': 'CH4'},
                    {'label': 'Nitrous Oxide', 'value': 'N2O'},
                    {'label': 'Hydrofluocarbons', 'value': 'HFC'},
                    {'label': 'Perfluorocarbons', 'value': 'PFC'},
                    {'label': 'Sulphur Hexaflouride', 'value': 'SF6'},
                ],
                value='GHG',
                labelStyle={'font-size': '2rem'}, 
                className="offset-by-two seven columns"
            ),
            dcc.Markdown('''
            
                Also, you can click on the country name on the graph to include/exclude it.
                            
                Greenhouse Emission Estimates
                ''', 
                className='offset-by-one nine columns', 
                style={'paddingLeft': '5%'})]
            )

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
            
            It is hard to make an intuitive sense of 10kg of CO2 is, right? Or even a tonne of CO2? We believe that it is important to give those intuitive meanings to the numbers. Hope this infographic could help you with that. 
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
        ## Fore More
        For more information, please visit our Github [repository](https://github.com/yeununchoo/GHGEmission). 
        
        Thank you for visiting our website. Bye!
        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

def references():
    """
    Returns conclusion in markdown
    """
    return html.Div(children=[dcc.Markdown('''
        ## References
        
        - [OECD Weekly GDP Tracker](https://www.oecd.org/economy/weekly-tracker-of-gdp-growth/)
        - [OECD Greenhouse Gas Emissions](https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG)
        - [IMF GDP](https://www.imf.org/external/datamapper/NGDPD@WEO/OEMDC/ADVEC/WEOWORLD) 
        - [Greenhouse Gas Equivalencies Calculator](https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator), US Environmental Protection Agency 

        ''', className='eleven columns', style={'paddingLeft': '5%'})], className="row")

#####################################################################
# 
# app 
#
#####################################################################

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.Div([
        page_header(),
        html.Hr(),
        description(),
        static_section(),
        static_radio_button(),
        html.Div(id='static_fig'),
        weekly_section(),
        weekly_radio_button(),
        html.Div(id='weekly_fig'),
        inforgraphic(),
        conclusion(),
        references(),
    ], className='row', id='content')
])

#####################################################################
# 
# responsive callbacks 
#
#####################################################################

@app.callback(
    Output(component_id='static_fig', component_property='children'),
    Input(component_id='static_ghg', component_property='value'),
)
def static_figure_responsive(ghg):
    """
    Returns the static ghg vs gdp scatter plot
    """
    
    ghg = str(ghg)
    
    df_static = pd.read_parquet("results/df_static.parquet")  
    fig_scatter = px.scatter(df_static, 
                             x = "GDP", 
                             y = ghg, 
                             color = "Country",
                             hover_data = ["Year"], 
                             log_x = True, 
                             log_y = True,
                             #title = "GH Gas Emission vs GDP",
                             labels={'GDP':'GDP, Billion USD', 
                                     f'{ghg}':f'{ghg}, Tonnes of CO2 Equivalent'}, 
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

@app.callback(
    Output(component_id='weekly_fig', component_property='children'),
    Input(component_id='weekly_ghg', component_property='value'),
)
def weekly_figure_responsive(ghg):
    """
    Returns the static ghg vs gdp scatter plot
    """
    
    ghg = str(ghg)
    
    df_weekly = pd.read_parquet("results/df_weekly.parquet")  
    fig_bar = px.bar(df_weekly, 
               x = "Week", 
               y = f"{ghg}_weekly", 
               color = "Country",
               #title = "Weekly GH Gas Emission Prediction", 
               labels={f'{ghg}_weekly':f'{ghg}, Tonnes of CO2 Equivalent'},
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

if __name__ == '__main__':
    app.run_server(debug=True)
