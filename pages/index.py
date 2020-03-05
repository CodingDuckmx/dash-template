# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Kindle Books' Reviews Metrics   

            I got a dataset of 2 million of Kindle Book reviews. Because the size of the data, I took a random sample of 10% and this what I got to show.

            ✅ The metrics are quite interesting as you can see in the next pages, although is a challenge dealing with such sample.

            ❌ The complexcity of the dataset and the ambitious it is, may required some other tools more powerfull to predict the score of the ebooks, based on the summary of the review.

            """
        ),
        dcc.Link(dbc.Button('Explore the data', color='primary'), href='/insights')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        # dcc.Graph(figure=fig),
        html.Img(src='assets/kindle_enviroment .jpg', className='img-sentimental_analysis')
    ]
)

layout = dbc.Row([column1, column2])