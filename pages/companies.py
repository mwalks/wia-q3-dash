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
            # companies page
            html.Div(
                [
                    html.Hr(style={"border-top":"2px solid lightgrey","margin-top":"0","margin-bottom":"3.5rem"}),
                    html.Div([
                        html.H6(
                            "What companies are the most represented?",
                            className="subtitle",style={"margin-left":"10%","margin-bottom":"25px","font-size":"2rem"}
                        ),
                        html.A(
                            html.Img(id="wia-titles",
                            src=app.get_asset_url("wia_company_wordcloud.png"),
                            style={"margin":"auto","width":"90%","display":"block"}
                            )
                        )
                    ],className="row"
                    ),
                    html.Br(),
                    html.Div(html.I('''The companies with the most
representation are currently CoverMyMeds, Nationwide Insurance, The James Cancer Hospital of The Ohio State
University, Honda, and Alliance Data. If you click on \"Industries\" you\'ll see the presence of these companies reflected in the industries represented.'''),className="row",style={"margin-left":"10%","margin-right":"10%","text-align":"justify"}
                    ),
                    html.Br(),
                    html.Details([
                                html.Summary('Code:',style={"cursor":"pointer"}),
                                html.Div(
                                    dcc.Markdown(r'''
```py
import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import PIL.ImageOps
import random
from wordcloud import ImageColorGenerator
WNL = nltk.WordNetLemmatizer()

#data assumed to be cleaned at this point
#note some imports not used for this word cloud but useful for others

df2 = q3_analysis_work['company'].dropna(how='all').astype(str)

def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(240, 99%%, %d%%)" % random.randint(20, 80)
# -----
 
# Set word cloud params and instantiate the word cloud.
# The height and width only affect the output image file.
WC_height = 500
WC_width = 1000
WC_max_words = 100

#generate word cloud
wc = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width, background_color="white",prefer_horizontal=0.7)
 
wc.generate_from_frequencies(dict(df2.value_counts()))

plt.imshow(wc.recolor(color_func=blue_color_func, random_state=5),interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("wia_company_wordcloud.png")
```
'''
                                    ),className="row",style={"overflow":"scroll","height":"400px"}
                                )
                    ]),
                    html.Br(),
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