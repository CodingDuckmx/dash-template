# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## For more details I recomend you to read my post on Medium.


            """
        ),
        html.Div([
            html.Div(id='page-2-content'),
            html.Br(),
            dcc.Link('Read the post', href='https://medium.com/@CodingDuckMx/predicting-kindle-books-reviews-3be74232e5d7'),
        ])
    ],
)

column2 = dbc.Col([

html.Img(src='assets/kindle_app_ad.jpg', className='img-kindle_app_ad')

])

layout = dbc.Row([column2, column1])



