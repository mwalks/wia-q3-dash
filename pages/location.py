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

df = pd.read_csv(DATA_PATH.joinpath("shortcut_loc.csv"))

p4 = px.scatter_geo(
    df,
    lat='lat',
    lon='lon',
    size='percent',
    size_max=40,
    opacity=0.7,
    hover_name='city',
    scope='usa',
    title='Attendee Proportions by City',
    color_discrete_map={'': 'orange'},
    width=700,
    height=500,
).update(
    layout=dict(
        title=dict(
            x=0.5
        ),
        geo=dict(
            projection_type='albers usa',
            subunitcolor='gray',
            subunitwidth=0.5,
            countrycolor='gray'
        )
    )
)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # locations page
            html.Div(
                [
                    html.Div([
                        html.Hr(style={"border-top": "2px solid lightgrey",
                                       "margin-top": "0", "margin-bottom": "3.5rem"}),
                        html.H6(
                            "Where do attendees come from?",
                            className="subtitle", style={"margin-left": "10%", "margin-bottom": "25px", "font-size": "2rem"}
                        ),
                        html.Div([
                            dcc.Graph(
                                id="graph4",
                                figure=p4,
                                config={
                                    'displayModeBar': False
                                },
                                style={
                                    "width": "100%", "display": "inline-block", "align": "center"}
                            ),
                        ])
                    ], className="row"
                    ),
                    html.Br(),
                    html.Div(html.I(
                        r'''Attendees come from a diverse range of locations, with most coming from one of over ten cities in Ohio The Columbus community is particularly well-represented at 58%.'''
                    ), className="row", style={"margin-left": "20%", "margin-right": "20%", "text-align": "justify"}
                    ),
                    html.Br(),
                    html.Details([
                        html.Summary('Code:', style={"cursor": "pointer"}),
                        html.Div(
                            dcc.Markdown(r'''
```py
from plotly import express as px
import pandas as pd

# assume data already cleaned and organized
df = pd.read_csv("shortcut_loc.csv")
px.scatter_geo(
    df,
    lat='lat',
    lon='lon',
    size='percent',
    size_max=40,
    opacity=0.7,
    hover_name='city',
    scope='usa',
    title='Attendee Proportions by City',
    color_discrete_map={'':'orange'},
    width=700,
    height=500,
).update(layout=dict(title=dict(x=0.5),geo=dict(projection_type='albers usa',subunitcolor='gray',subunitwidth=0.5,countrycolor='gray')))
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