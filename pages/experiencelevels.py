# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import pathlib
from dash.dependencies import Input, Output
from utils import Header, make_dash_table
import plotly.express as px
import numpy as np

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("..\data").resolve()

# Prepare graphs with pre-agg data

p = px.histogram(
    pd.read_csv(DATA_PATH.joinpath("shortcut_tech_exp.csv")),
    x='Technical Expertise',
    y='Frequency',
    histnorm="percent",
    histfunc="sum",
    color_discrete_map={'': ['gray', 'gray', 'indianred', 'gray', 'gray']},
    labels={'Frequency': r'Attendees (%)'},
    category_orders={'Technical Expertise': [
        'Basic Knowledge', 'Novice', 'Intermediate', 'Advanced', 'Expert']},
    title="Reported Technical Expertise",
    height=520,
)
p2 = px.histogram(
    pd.read_csv(DATA_PATH.joinpath("shortcut_an_exp.csv")),
    x='Analytics Experience',
    y='Frequency',
    histnorm="percent",
    histfunc="sum",
    color_discrete_map={'': ['gray', 'indianred', 'gray', 'gray']},
    labels={'Frequency': r'Attendees (%)'},
    category_orders={'Analytics Experience': [
        '< 1 Year', '2-4 Years', '5-9 Years', '10+ Years']},
    title="Reported Experience in Analytics",
    height=500
)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # title page
            html.Div(
                [
                    html.Div([
                        html.Hr(style={"border-top": "2px solid lightgrey",
                                       "margin-top": "0", "margin-bottom": "3.5rem"}),
                        html.H6(
                            "How confident are attendees about levels of experience?",
                            className="subtitle", style={"margin-left": "10%", "margin-bottom": "25px", "font-size": "2rem"}
                        ),
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(
                                    id="graph",
                                    figure=p,
                                    config={
                                        'displayModeBar': False
                                    },
                                    style={"width":"50%","display": "inline-block"}
                                ),
                            ],),
                            dbc.Col([
                                dcc.Graph(
                                    id="graph2",
                                    figure=p2,
                                    config={
                                        'displayModeBar': False
                                    },
                                    style={"width":"50%","display": "inline-block"}
                                ),
                            ],)
                        ],className='two columns')
                    ], className="row"
                    ),
                    html.Br(),
                    html.Div(html.I(
                        r'''Most of the registered attendees consider their technical expertise to be novice or intermediate, whereas
21.5% consider they have advanced expertise. Few considder themselves to be "experts." Additionally, most of the attendees have between 2 and 9 year of
experience in analytics. There is a well-balanced distribution of both early career and more experienced professionals.'''
                    ), className="row", style={"margin-left": "10%", "margin-right": "10%", "text-align": "justify"}
                    ),
                    html.Br(),
                    html.Details([
                        html.Summary('Code:', style={"cursor": "pointer"}),
                        html.Div(
                            dcc.Markdown(r'''
```py
import pandas as pd
from plotly import express as px

#assume data cleaned by this point
#aggregates value counts to a new df for plotly express
df = q3_analysis_work.technical_expertise.value_counts().to_frame().reset_index().rename(columns={"index":"Technical Expertise","technical_expertise":"Frequency"})

#plotting the histogram of technical expertise
px.histogram(
    df,
    x='Technical Expertise',
    y='Frequency',
    histnorm="percent",
    histfunc="sum",
    color_discrete_map={'':['gray','gray','indianred','gray','gray']},
    labels={'Frequency':r'of Attendees (%)'},
    category_orders={'Technical Expertise':['Basic Knowledge','Novice','Intermediate','Advanced','Expert']},
    title="Reported Technical Expertise")

#plotting the histogram of analytics experience

df = q3_analysis_work.analytics_experience.value_counts().to_frame().reset_index().rename(columns={"index":"Analytics Experience","analytics_experience":"Frequency"})
px.histogram(
    df,
    x='Analytics Experience',
    y='Frequency',
    histnorm="percent",
    histfunc="sum",
    color_discrete_map={'':['gray','indianred','gray','gray']},
    labels={'Frequency':r'of Attendees (%)'},
    category_orders={'Analytics Experience':['< 1 Year','2-4 Years','5-9 Years','10+ Years']},
    title="Reported Experience in Analytics")
```
'''
                                         ), className="row", style={"overflow": "scroll", "height": "400px"}
                        )
                    ]),
                    html.P(
                        [
                            "More detailed code can be found at ",
                            html.A("https://github.com/mwalks",
                                   href="https://github.com/mwalks"),
                            html.Br(),
                            "THANK YOU FOR YOUR SUPPORT!"
                        ], style={"color": "grey", "text-size": "1.3rem", "text-align": "center"}
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
