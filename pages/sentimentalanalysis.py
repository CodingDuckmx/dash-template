import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Sentimental Analysis 

            I used TexBlob to measure the subjectivity and polarity of the reviews, classified by the score.
            I plot them expecting to use this to predict scores, but all scores are distributed along the space, almost.
            So it turns interesenting to take a look, at least, at this moment.
       
            """
        ),
    ],
    md=4,
)

column2 = dbc.Col([

html.Img(src='assets/sentimental_analysis.png', className='img-sentimental_analysis')

])

layout = dbc.Row([column1, column2])
