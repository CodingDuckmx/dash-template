# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from joblib import load
import time
import datetime
from datetime import datetime as dt
# Imports from this application
from app import app

model = load('assets/modelbinlgb.joblib')


# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights


            """
        ),
        dcc.Markdown("""##### Date of the review"""),
        html.Div([dcc.DatePickerSingle(
            id='reviewdate',
            number_of_months_shown=1,
            min_date_allowed=dt(2007, 1, 1),
            max_date_allowed=dt(2018, 12, 31),
            date=datetime.date(2013,7,12)
        )], style={'marginBottom': '10px'}),
        dcc.Markdown("""##### Title of the Kindle book"""),
        html.Div([dcc.Dropdown(
            id='book',
            options=[
                {'label': 'Own Your Self: Master Your Character', 'value': 'B01EKNN4LE'},
                {'label': 'The Man On Table Ten - A Mysterious SciFi Tale', 'value': 'B00CXFH4MC'},
                {'label': 'The Valet and the Stable Groom', 'value': 'B01G7I876W'}
            ],
            value='B01G7I876W'
        )], style={'marginBottom': '10px'}),
        dcc.Markdown("""##### Image uploaded"""),
        dcc.RadioItems(
        id='image',
        options=[
            {'label': 'Yes', 'value': 'True'},
            {'label': 'No', 'value': 'False'},
        ],
        value='False'
        ),
        dcc.Markdown(
            """         
            ##### **Copy/paste or write a short book review below.**
            """
        ),
        dcc.Textarea(
            id='inputreview',
            placeholder='Max length: 50 words',
            value=" I really loved this book. I enjoy so much having a Kindle, so I can read everywhere. ",
            cols=500,
            rows=3,
            maxLength=500,
            style={'width': '100%', 'marginBottom': '1.25em', 'marginTop':'1em'}
        ),
        

        dbc.Button('Get the score asociated to your review!', id='button', n_clicks=1, color='primary',
        style=dict(marginTop=1.75, marginBottom=10)
        ),  
     

    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown("""## Predictions time"""),
        dcc.Markdown(
            """
            ### Instructions

            Select a date between 2007 and 2018.

            Write a review like you've read the book.

            Mark the option,if you would upload a photo to the review.

            Due the complexity of the model, it's accuracy is the 70%, so be patient.

            """),  
        html.Div(id='prediction-content', className='lead', style={'marginBottom': '10px'}),   
    ]
)

cols = ['verified',
        'reviewerID', 
        'asin', 
        'unixReviewTime',
        'vote', 
        'image',
        'reviewyear',
        'reviewmonth',
        'reviewday',
        'season', 
        'len_summary',
        'polarity_sum',
        'subjectivity_sum',
        'polarity_rT',
        'subjectivity_rT',
        'len_reviewText',
        'doesnt',
        'depressing',
        'needed',
        'quit',
        'worthless',
        'captivating',
        'surprisingly',
        'useless',
        'okay',
        'tedious',
        'slow',
        'shallow',
        'loved',
        'dnf',
        'classic',
        'substance',
        'clean',
        'reads',
        'young',
        'basic',
        'editor',
        'rip',
        'written',
        'pathetic',
        'break',
        'forward',
        'heat',
        'idea',
        'sexy',
        'unfinished',
        'words',
        'far',
        'beautiful',
        'authors',
        'make',
        'love',
        'poorly',
        'cozy',
        'quite',
        'disappointment',
        'half',
        'christmas',
        'decent',
        'home',
        'wouldnt',
        'lots',
        'christian',
        'spoiler',
        'cup',
        'expected',
        'lovely',
        'bdsm',
        'pages',
        'want',
        'feelings',
        'absolutely',
        'compelling',
        'potential',
        'omg',
        'light',
        'exciting',
        'inspiring',
        'surprised',
        'meh',
        'read',
        'better',
        'fell',
        'suspense',
        'weak',
        'escape',
        'hot',
        'best',
        'delightful',
        'intense',
        'humor',
        'magic',
        'brilliant',
        'stories',
        'chance',
        'somewhat',
        'waiting',
        'silly',
        'going',
        'powerful',
        'fun',
        'twist',
        'sure',
        'kindle',
        'tale',
        'cute',
        'bother',
        'nope',
        'mystery',
        'isnt',
        'glad',
        'tips',
        'pleasant',
        'entertaining',
        'ended',
        'enjoyable',
        'oh',
        'really',
        'badly',
        'quick',
        'confusing',
        'hilarious',
        'long',
        'moon',
        'erotic',
        'rushed',
        'skip',
        'interesting',
        'thought',
        'im',
        'murder',
        'review',
        'ripoff',
        'drama',
        'zombie',
        'novella',
        'predictable',
        'finally',
        'sorry',
        'hard',
        'addictive',
        'fabulous',
        'sweet',
        'different',
        'dont',
        'true',
        'repetitive',
        'ideas',
        'unbelievable',
        'packed',
        'sad',
        'thats',
        'kids',
        'stars',
        'follow',
        'effort',
        'serial',
        'character',
        'children',
        'makes',
        'arc',
        'recommended',
        'stopped',
        'strong',
        'yes',
        'happened',
        'complete',
        'execution',
        'feel',
        'garbage',
        'wtf',
        'adorable',
        'unexpected',
        'cliffhanger',
        'unique',
        'holiday',
        'girl',
        'enjoy',
        'stop',
        'pay',
        'real',
        'need',
        'reader',
        'loving',
        'bride',
        'disappointed',
        'definitely',
        'star',
        'helpful',
        'job',
        'delicious',
        'continues',
        'epic',
        'hated',
        'contemporary',
        'miss',
        'money',
        'just',
        'action',
        'spoilers',
        'ride',
        'buy',
        'editing',
        'missing',
        'style',
        'man',
        'grammar',
        'say',
        'info',
        'paced',
        'hit',
        'started',
        'worst',
        'trash',
        'holy',
        'page',
        'crazy',
        'twists',
        'secrets',
        'charming',
        'amazing',
        'vampire',
        'sucked',
        'disjointed',
        'outstanding',
        'terrific',
        'boring',
        'summer',
        'getting',
        'didnt',
        'useful',
        'favorite',
        'winner',
        'heart',
        'rock',
        'coming',
        'premise',
        'life',
        'yummy',
        'wild',
        'average',
        'reading',
        'conclusion',
        'right',
        'tried',
        'original',
        'keeps',
        'taste',
        'family',
        'weird',
        'confused',
        'emotional',
        'care',
        'maybe',
        'wrong',
        'tea',
        'super',
        'intriguing',
        'write',
        'highly',
        'let',
        'did',
        'people',
        'author',
        'hooked',
        'information',
        'romance',
        'simple',
        'cool',
        'world',
        'ruined',
        'errors',
        'heartwarming',
        'sequel',
        'guide',
        'mixed',
        'beware',
        'fascinating',
        'childrens',
        'development',
        'hero',
        'soso',
        'satisfying',
        'got',
        'huh',
        'thing',
        'impressed',
        'longer',
        'sense',
        'nicely',
        'gripping',
        'price',
        'informative',
        'recipes',
        'dumb',
        'writer',
        'save',
        'riveting',
        'romantic',
        'addition',
        'characters',
        'perfect',
        'bought',
        'fan',
        'fantastic',
        'typical',
        'night',
        'free',
        'totally',
        'work',
        'funny',
        'juvenile',
        'incredible',
        'ive',
        'erotica',
        'terrible',
        'believable',
        'mind',
        'advice',
        'stupid',
        'liked',
        'hate',
        'dark',
        'annoying',
        'moving',
        'pleasantly',
        'reviewed',
        'ready',
        'fair',
        'awesome',
        'come',
        'short',
        'truly',
        'language',
        'finish',
        'excellent',
        'left',
        'writing',
        'steamy',
        'kind',
        'away',
        'bear',
        'fiction',
        'thumbs',
        'trilogy',
        'lame',
        'mess',
        'suspenseful',
        'resource',
        'friends',
        'pointless',
        'bit',
        'thank',
        'type',
        'blah',
        'strange',
        'second',
        'introduction',
        'plot',
        'beautifully',
        'expecting',
        'paranormal',
        'ridiculous',
        'ugh',
        'opinion',
        'vulgar',
        'great',
        'simply',
        'things',
        'quirky',
        'looking',
        'easy',
        'journey',
        'mc',
        'start',
        'debut',
        'dull',
        'poor',
        'little',
        'wait',
        'sex',
        'way',
        'yuck',
        'adventure',
        'lacking',
        'god',
        'wellwritten',
        'wonderful',
        'total',
        'look',
        'think',
        'porn',
        'worse',
        'beginning',
        'immature',
        'mate',
        'unless',
        'fantasy',
        'finished',
        'lovers',
        'eh',
        'healthy',
        'heroine',
        'zero',
        'stuff',
        'incomplete',
        'enjoyed',
        'refreshing',
        'felt',
        'finding',
        'promise',
        'ya',
        'fast',
        'fall',
        'chapters',
        'alright',
        'dreadful',
        'old',
        'story',
        'western',
        'scifi',
        'wish',
        'bored',
        'extremely',
        'wanted',
        'nan',
        'forever',
        'try',
        'awful',
        'sizzling',
        'historical',
        'disappointing',
        'surprising',
        'damn',
        'series',
        'solid',
        'big',
        'crap',
        'point',
        'novel',
        'ok',
        'kidding',
        'alpha',
        'believe',
        'time',
        'ending',
        'know',
        'waste',
        'collection',
        'pretty',
        'chapter',
        'happy',
        'touching',
        'concept',
        'disgusting',
        'recommend',
        'wasted',
        'title',
        'worth',
        'sample',
        'engaging',
        'thoroughly',
        'edited',
        'gets',
        'pass',
        'hope',
        'honest',
        'lot',
        'wanting',
        'needs',
        'wth',
        'frustrating',
        'lost',
        'horrible',
        'absolute',
        'set',
        'storyline',
        'installment',
        'seriously',
        'yawn',
        'flat',
        'new',
        'surprise',
        'thrilling',
        'day',
        'book',
        'disappoint',
        'rest',
        'bad',
        'nice',
        'books',
        'does',
        'like',
        'continuation',
        'cowboy',
        'reviews',
        'hoping',
        'prequel',
        'line',
        'provoking',
        'wasnt',
        'good',
        'end',
        'thriller',
        'shifter',
        'wow',
        'turner']

listb = list([''] * (len(cols)+1))

my_dict = dict(zip(cols,listb))

review = pd.DataFrame([my_dict])

def clean_numbers_signs(text):

  text = str(text)
  text = text.lower()
  text = re.sub('\[.*?\]','',text) ### get rid of the brackets
  text = re.sub('[%s]' % re.escape(string.punctuation),'',text)  ### get rid of punctation marks.
  text = re.sub('\w*\d\w*', '',text)  ##get rid of the numbers.
  return text

# def tokenization(text):

#   tv = TfidfVectorizer(stop_words=None, lowercase=True)
#   data_tv = tv.fit_transform(text)
#   data_dtm = pd.DataFrame(data_tv.toarray(), columns= tv.get_feature_names())
#   return data_dtm


@app.callback(
    [Output('prediction-content', 'children')],
    [Input('button','n_clicks'),Input('reviewdate', 'date'),Input('book', 'value'),
    Input('image','value'),Input('inputreview','value')],
)

def predict(clicked,reviewdate,book,image,inputreview):
    if clicked:
        textreview = '  '.join([x for x in inputreview.split() if x in cols])
        cleanedreview = clean_numbers_signs(inputreview)
        braqcleanedreview = [clean_numbers_signs(inputreview)]


        tv = TfidfVectorizer(stop_words=None, lowercase=False, analyzer='word', token_pattern=r"(?u)\b\w+\b")
        data_tv = tv.fit_transform(braqcleanedreview)
        tokenized = pd.DataFrame(data_tv.toarray(), columns= tv.get_feature_names())
    

        review['verified'] = True
        review['reviewerID'] = 'A23ZNGL704AW7O'
        review['asin'] = book
        review['unixReviewTime'] = int(time.mktime(dt.strptime(str(reviewdate), "%Y-%m-%d").timetuple()))
        review['vote'] = True
        review['reviewyear'] = pd.to_datetime(reviewdate).year
        review['reviewmonth'] = pd.to_datetime(reviewdate).month
        review['reviewday'] = pd.to_datetime(reviewdate).day
        review['season'] = 'winter'
        review['len_summary'] = len(inputreview.split())
        review['polarity_sum'] = TextBlob(cleanedreview).polarity
        review['subjectivity_sum'] = TextBlob(cleanedreview).subjectivity
        review['polarity_rT'] = TextBlob(cleanedreview).polarity
        review['subjectivity_rT'] = TextBlob(cleanedreview).subjectivity
        review['len_reviewText'] = len(cleanedreview.split())
        
        for i in tokenized.columns.tolist():
            if i in review.columns.tolist():
                review[i]= review[i].apply(lambda x: tokenized.loc[0,i]  if i in review.columns.tolist() else 0)

        review_tomodel = review.replace('',0)
        
        
        y_pred = model.predict(review_tomodel)

        return [f'The prediction is you would use {y_pred} stars on your review.']



layout = dbc.Row([column2, column1])