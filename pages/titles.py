# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import pathlib
from dash.dependencies import Input, Output
from utils import Header, make_dash_table

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("..\data").resolve()

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # title page
            html.Div(
                [
                    html.Div([
                        html.Hr(style={"border-top":"2px solid lightgrey","margin-top":"0","margin-bottom":"3.5rem"}),
                        html.H6(
                            "What job titles do attendees list most commonly?",
                            className="subtitle",style={"margin-left":"10%","margin-bottom":"25px","font-size":"2rem"}
                        ),
                        html.A(
                            html.Img(id="wia-titles",
                            src=app.get_asset_url("wia_title_wordcloud.png"),
                            style={"margin":"auto","width":"90%","display":"block"}
                            )
                        )
                    ],className="row"
                    ),
                    html.Br(),
                    html.Div(html.I(
                        r'''The job titles are almost unique per attendee, but around 20% of them have a title that could be classified
in general as “Data Analyst.” You can see by the word cloud that titles involving data, analytics, analyst,
manager, system, senior, specialist, associate, product, business, and consultant stand out.'''
                        ),className="row",style={"margin-left":"10%","margin-right":"10%","text-align":"justify"}
                    ),
                    html.Br(),
                    html.Details([
                                html.Summary('Code:',style={"cursor":"pointer"}),
                                html.Div(
                                    dcc.Markdown(r'''
```py
import numpy as np
import io
import pandas as pd
from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models
import gensim
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from PIL import Image
import PIL.ImageOps
import random
import nltk
import re
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from operator import itemgetter
WNL = nltk.WordNetLemmatizer()

#data assumed to be cleaned by this point

df2 = q3_analysis_work['job_title'].dropna(how='all').astype(str)
df2 = " ".join(job_title for job_title in df2)
stopwords = set(STOPWORDS)
stopwords.update(["I", "on", "and", "good", "etc", "make", "better", "depending"])
# Generate a word cloud image
text_content = [WNL.lemmatize(str(df2)) for t in df2]
tokens = nltk.word_tokenize(str(df2))
text = nltk.Text(tokens)
# Remove extra chars and remove stop words.
text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text]
text_content = [word for word in text_content if word not in stopwords]

# After the punctuation above is removed it still leaves empty entries in the list.
# Remove any entries where the len is zero.
text_content = [s for s in text_content if len(s) != 0]

# Best to get the lemmas of each word to reduce the number of similar words
# on the word cloud. The default lemmatize method is noun, but this could be
# expanded.
# ex: The lemma of 'characters' is 'character'.
text_content = [WNL.lemmatize(t) for t in text_content]

# setup and score the bigrams using the raw frequency.
finder = BigramCollocationFinder.from_words(text_content)
bigram_measures = BigramAssocMeasures()
scored = finder.score_ngrams(bigram_measures.raw_freq)
# By default finder.score_ngrams is sorted, however don't rely on this default behavior.
# Sort highest to lowest based on the score.
scoredList = sorted(scored, key=itemgetter(1), reverse=True)

# word_dict is the dictionary we'll use for the word cloud.
# Load dictionary with the FOR loop below.
# The dictionary will look like this with the bigram and the score from above.
# word_dict = {'bigram A': 0.000697411,
#             'bigram B': 0.000524882}

word_dict = {}

listLen = len(scoredList)

# Get the bigram and make a contiguous string for the dictionary key. 
# Set the key to the scored value. 
for i in range(listLen):
    word_dict[' '.join(scoredList[i][0])] = scoredList[i][1]

word_dict.update({'Analyst Data':0,'Data Analytics':0})
def red_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 99%%, %d%%)" % random.randint(40, 70)
# -----

# Set word cloud params and instantiate the word cloud.
# The height and width only affect the output image file.
WC_height = 500
WC_width = 1000
WC_max_words = 100

wc = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width,stopwords=stopwords, background_color="white")

wc.generate_from_frequencies(word_dict)

plt.imshow(wc.recolor(color_func=red_color_func, random_state=5), interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("wia_title_wordcloud.png")
```
'''
                                    ),className="row",style={"overflow":"scroll","height":"400px"}
                                )
                    ]),
                    html.P(
                        [
                            "More detailed code can be found at ",
                            html.A("https://github.com/mwalks",
                            href="https://github.com/mwalks"),
                            html.Br(),
                            "THANK YOU FOR YOUR SUPPORT!"
                        ],style={"color":"grey","text-size":"1.3rem","text-align":"center"}
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )