# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from joblib import load
import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from datetime import datetime as dt

# Imports from this application
from app import app

# dash = load('assets/dash.joblib')
model = load('assets/model.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions Time

            """  
        ),
        dcc.Markdown(
            """
            
            Select the book you are reviweing:
            
            """
        ),
        dcc.Dropdown(
            id = 'books',
             options=[
                     {'label': 'The Valet and the Stable Groom', 'value': 'opt1'},
                     {'label': 'The Man On Table Ten - A Mysterious SF Tale', 'value': 'opt2'},
                     {'label': 'Own Your Self: Master Your Character', 'value': 'opt3'}
             ],
            value = 'opt1'
        ),
        dcc.Markdown("""##### Date of the review."""),
        html.Div([dcc.DatePickerSingle(
            id='reg_date',
            number_of_months_shown=1,
            min_date_allowed=dt(1998, 9, 1),
            max_date_allowed=dt(2018, 7, 30),
            date=dt(1999, 5, 10)
        )], style={'marginBottom': '10px'}),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """

            
            ##### **Copy/paste or write a short book review below.**
            """
        ),
        dcc.Textarea(
            id='input-box',
            placeholder='Max length: 50 words',
            value="I really loved this book. I enjoy so much having a Kindle, so I can read everywhere.",
            cols=500,
            rows=3,
            maxLength=500,
            style={'width': '100%', 'marginBottom': '1.25em', 'marginTop':'1em'}
        ),
        dbc.Button('Get the score asociated to your review!', id='button', n_clicks=1, color='primary', 
                   style=dict(marginTop=1.75, marginBottom=10)
        ),
        dcc.Markdown('##### Score associated predicted:', style={'marginBottom': '0'}), 
        html.Div(id='prediction-label', className='lead', 
                 style={'marginBottom': '0', 'fontWeight': 'bold', 'fontSize': '18px'}),
    ],
    md=6,
)

layout = dbc.Row([column1, column2])


@app.callback(
    [Output('prediction-label', 'children')],
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')]
)



# def clean_numbers_signs(resena):
#     resena = str(resena)
#     resena = resena.lower()
#     resena = re.sub('\[.*?\]','',resena) ### get rid of the brackets
#     resena = re.sub('[%s]' % re.escape(string.punctuation),'',resena)  ### get rid of punctation marks.
#     resena = re.sub('\w*\d\w*', '',resena)  ##get rid of the numbers.
#     return resena

# round1 = lambda x: clean_numbers_signs(x)



# def cleanning(dataframe):
#     dataframe['summary'] = dataframe['summary'].apply(round1)
#     dataframe['len_summary'] = dataframe['summary'].apply(lenreview)
#     dataframe['polarity_sum'] = dataframe['summary'].apply(pol)
#     dataframe['subjectivity_sum'] = dataframe['summary'].apply(sub)
#     dataframe['reviewText'] = dataframe['reviewText'].apply(round1)
#     dataframe['polarity_rT'] = dataframe['reviewText'].apply(pol)
#     dataframe['subjectivity_rT'] = dataframe['reviewText'].apply(sub)  
#     dataframe['len_reviewText'] = dataframe['reviewText'].apply(lenreview)
#     return dataframe

# ### Tokenization  of text

# def tokenization(resena):
#     tv = TfidfVectorizer(stop_words='english', lowercase=True)
#     data_tv = tv.fit_transform(resena.summary)
#     data_dtm = pd.DataFrame(data_tv.toarray(), columns= tv.get_feature_names())
#     return data_dtm


# cols = ['reviewID',
#           'overall', 
#           'verified',
#           'reviewerID', 
#           'asin', 
#           'reviewText',
#           'summary', 
#           'unixReviewTime',
#           'vote', 
#           'image',
#           'reviewyear',
#           'reviewmonth',
#           'reviewday',
#           'season', 
#           'len_summary',
#           'polarity_sum',
#           'subjectivity_sum',
#           'polarity_rT',
#           'subjectivity_rT',
#           'len_reviewText',
#           'doesnt',
#           'depressing',
#           'needed',
#           'quit',
#           'worthless',
#           'captivating',
#           'surprisingly',
#           'useless',
#           'okay',
#           'tedious',
#           'slow',
#           'shallow',
#           'loved',
#           'dnf',
#           'classic',
#           'substance',
#           'clean',
#           'reads',
#           'young',
#           'basic',
#           'editor',
#           'rip',
#           'written',
#           'pathetic',
#           'break',
#           'forward',
#           'heat',
#           'idea',
#           'sexy',
#           'unfinished',
#           'words',
#           'far',
#           'beautiful',
#           'authors',
#           'make',
#           'love',
#           'poorly',
#           'cozy',
#           'quite',
#           'disappointment',
#           'half',
#           'christmas',
#           'decent',
#           'home',
#           'wouldnt',
#           'lots',
#           'christian',
#           'spoiler',
#           'cup',
#           'expected',
#           'lovely',
#           'bdsm',
#           'pages',
#           'want',
#           'feelings',
#           'absolutely',
#           'compelling',
#           'potential',
#           'omg',
#           'light',
#           'exciting',
#           'inspiring',
#           'surprised',
#           'meh',
#           'read',
#           'better',
#           'fell',
#           'suspense',
#           'weak',
#           'escape',
#           'hot',
#           'best',
#           'delightful',
#           'intense',
#           'humor',
#           'magic',
#           'brilliant',
#           'stories',
#           'chance',
#           'somewhat',
#           'waiting',
#           'silly',
#           'going',
#           'powerful',
#           'fun',
#           'twist',
#           'sure',
#           'kindle',
#           'tale',
#           'cute',
#           'bother',
#           'nope',
#           'mystery',
#           'isnt',
#           'glad',
#           'tips',
#           'pleasant',
#           'entertaining',
#           'ended',
#           'enjoyable',
#           'oh',
#           'really',
#           'badly',
#           'quick',
#           'confusing',
#           'hilarious',
#           'long',
#           'moon',
#           'erotic',
#           'rushed',
#           'skip',
#           'interesting',
#           'thought',
#           'im',
#           'murder',
#           'review',
#           'ripoff',
#           'drama',
#           'zombie',
#           'novella',
#           'predictable',
#           'finally',
#           'sorry',
#           'hard',
#           'addictive',
#           'fabulous',
#           'sweet',
#           'different',
#           'dont',
#           'true',
#           'repetitive',
#           'ideas',
#           'unbelievable',
#           'packed',
#           'sad',
#           'thats',
#           'kids',
#           'stars',
#           'follow',
#           'effort',
#           'serial',
#           'character',
#           'children',
#           'makes',
#           'arc',
#           'recommended',
#           'stopped',
#           'strong',
#           'yes',
#           'happened',
#           'complete',
#           'execution',
#           'feel',
#           'garbage',
#           'wtf',
#           'adorable',
#           'unexpected',
#           'cliffhanger',
#           'unique',
#           'holiday',
#           'girl',
#           'enjoy',
#           'stop',
#           'pay',
#           'real',
#           'need',
#           'reader',
#           'loving',
#           'bride',
#           'disappointed',
#           'definitely',
#           'star',
#           'helpful',
#           'job',
#           'delicious',
#           'continues',
#           'epic',
#           'hated',
#           'contemporary',
#           'miss',
#           'money',
#           'just',
#           'action',
#           'spoilers',
#           'ride',
#           'buy',
#           'editing',
#           'missing',
#           'style',
#           'man',
#           'grammar',
#           'say',
#           'info',
#           'paced',
#           'hit',
#           'started',
#           'worst',
#           'trash',
#           'holy',
#           'page',
#           'crazy',
#           'twists',
#           'secrets',
#           'charming',
#           'amazing',
#           'vampire',
#           'sucked',
#           'disjointed',
#           'outstanding',
#           'terrific',
#           'boring',
#           'summer',
#           'getting',
#           'didnt',
#           'useful',
#           'favorite',
#           'winner',
#           'heart',
#           'rock',
#           'coming',
#           'premise',
#           'life',
#           'yummy',
#           'wild',
#           'average',
#           'reading',
#           'conclusion',
#           'right',
#           'tried',
#           'original',
#           'keeps',
#           'taste',
#           'family',
#           'weird',
#           'confused',
#           'emotional',
#           'care',
#           'maybe',
#           'wrong',
#           'tea',
#           'super',
#           'intriguing',
#           'write',
#           'highly',
#           'let',
#           'did',
#           'people',
#           'author',
#           'hooked',
#           'information',
#           'romance',
#           'simple',
#           'cool',
#           'world',
#           'ruined',
#           'errors',
#           'heartwarming',
#           'sequel',
#           'guide',
#           'mixed',
#           'beware',
#           'fascinating',
#           'childrens',
#           'development',
#           'hero',
#           'soso',
#           'satisfying',
#           'got',
#           'huh',
#           'thing',
#           'impressed',
#           'longer',
#           'sense',
#           'nicely',
#           'gripping',
#           'price',
#           'informative',
#           'recipes',
#           'dumb',
#           'writer',
#           'save',
#           'riveting',
#           'romantic',
#           'addition',
#           'characters',
#           'perfect',
#           'bought',
#           'fan',
#           'fantastic',
#           'typical',
#           'night',
#           'free',
#           'totally',
#           'work',
#           'funny',
#           'juvenile',
#           'incredible',
#           'ive',
#           'erotica',
#           'terrible',
#           'believable',
#           'mind',
#           'advice',
#           'stupid',
#           'liked',
#           'hate',
#           'dark',
#           'annoying',
#           'moving',
#           'pleasantly',
#           'reviewed',
#           'ready',
#           'fair',
#           'awesome',
#           'come',
#           'short',
#           'truly',
#           'language',
#           'finish',
#           'excellent',
#           'left',
#           'writing',
#           'steamy',
#           'kind',
#           'away',
#           'bear',
#           'fiction',
#           'thumbs',
#           'trilogy',
#           'lame',
#           'mess',
#           'suspenseful',
#           'resource',
#           'friends',
#           'pointless',
#           'bit',
#           'thank',
#           'type',
#           'blah',
#           'strange',
#           'second',
#           'introduction',
#           'plot',
#           'beautifully',
#           'expecting',
#           'paranormal',
#           'ridiculous',
#           'ugh',
#           'opinion',
#           'vulgar',
#           'great',
#           'simply',
#           'things',
#           'quirky',
#           'looking',
#           'easy',
#           'journey',
#           'mc',
#           'start',
#           'debut',
#           'dull',
#           'poor',
#           'little',
#           'wait',
#           'sex',
#           'way',
#           'yuck',
#           'adventure',
#           'lacking',
#           'god',
#           'wellwritten',
#           'wonderful',
#           'total',
#           'look',
#           'think',
#           'porn',
#           'worse',
#           'beginning',
#           'immature',
#           'mate',
#           'unless',
#           'fantasy',
#           'finished',
#           'lovers',
#           'eh',
#           'healthy',
#           'heroine',
#           'zero',
#           'stuff',
#           'incomplete',
#           'enjoyed',
#           'refreshing',
#           'felt',
#           'finding',
#           'promise',
#           'ya',
#           'fast',
#           'fall',
#           'chapters',
#           'alright',
#           'dreadful',
#           'old',
#           'story',
#           'western',
#           'scifi',
#           'wish',
#           'bored',
#           'extremely',
#           'wanted',
#           'nan',
#           'forever',
#           'try',
#           'awful',
#           'sizzling',
#           'historical',
#           'disappointing',
#           'surprising',
#           'damn',
#           'series',
#           'solid',
#           'big',
#           'crap',
#           'point',
#           'novel',
#           'ok',
#           'kidding',
#           'alpha',
#           'believe',
#           'time',
#           'ending',
#           'know',
#           'waste',
#           'collection',
#           'pretty',
#           'chapter',
#           'happy',
#           'touching',
#           'concept',
#           'disgusting',
#           'recommend',
#           'wasted',
#           'title',
#           'worth',
#           'sample',
#           'engaging',
#           'thoroughly',
#           'edited',
#           'gets',
#           'pass',
#           'hope',
#           'honest',
#           'lot',
#           'wanting',
#           'needs',
#           'wth',
#           'frustrating',
#           'lost',
#           'horrible',
#           'absolute',
#           'set',
#           'storyline',
#           'installment',
#           'seriously',
#           'yawn',
#           'flat',
#           'new',
#           'surprise',
#           'thrilling',
#           'day',
#           'book',
#           'disappoint',
#           'rest',
#           'bad',
#           'nice',
#           'books',
#           'does',
#           'like',
#           'continuation',
#           'cowboy',
#           'reviews',
#           'hoping',
#           'prequel',
#           'line',
#           'provoking',
#           'wasnt',
#           'good',
#           'end',
#           'thriller',
#           'shifter',
#           'wow',
#           'turner']

# listb = list([''] * (len(cols)+1))

# my_dict = dict(zip(cols,listb))

# review = pd.DataFrame([my_dict])

# review['verified'] = 0.77124
# review['reviewerID'] = -1.274913
# review['asin'] = -0.28899
# review['reviewText'] = 'summary'
# review['summary'] = 'resena'
# review['unixReviewTime'] = -0.732434
# review['vote'] = -0.167452
# review['image'] = -0.02452
# review['reviewyear'] =0.758958
# review['reviewmonth'] = -0.963222
# review['reviewday'] = 0.821380
# review['season'] = -1.291608

# def len_of_review(resena):
#     len_sum = len(resena.split())
#     return len_sum

# lenreview = lambda x : len(x.split())  

# ###Sentimental Analysis

# pol = lambda x: TextBlob(x).sentiment.polarity
# sub = lambda x: TextBlob(x).sentiment.subjectivity

# def dash(resena):
#     resena = cleanning(resena)
#     tokenization(resena)

  
  
#     ### Build a function that fills out the word columns:
  
#     for i in tokenization(review).columns.tolist():
#         if i in resena.columns.tolist():
#             resena[i]= resena[i].apply(lambda x: tokenization(review).loc[0,i]  if i in resena.columns.tolist() else 0)

#     review_tomodel = resena.drop(columns=['reviewID', 'overall','reviewText','summary'])
#     review_tomodel = review_tomodel.replace('',0)


  
#     return review_tomodel



def predict(clicked, text):
    if clicked:

        text = [text]
        # review_tomodel = dash(text)
            
        # y_pred = model.predict(review_tomodel)
        y_pred = 5  ###erase
        output = [f'The prediction is {y_pred} stars.']
    return output




