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
            # overview page
            html.Div(
                [
                    html.Div(
                        [
                            html.Iframe(
                            width="560",
                            height="315",
                            src="https://www.youtube.com/embed/IQ0mP57Mcxk",
                            ),
                        ],className="iframe"
                    ),
                    html.Br(),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H1("At a Glance:"),
                                    html.Br(),
                                    html.Div(
                                        [
                                           dbc.Col(
                                               [
                                                   html.P(
                                                       html.Ul(
                                                           [
                                                               html.Li("The 4rd Annual WIA Conference"),
                                                               html.Li("Double last year's attendees"),
                                                               html.Li("Expanded to 3 days"),
                                                               html.Li("Had attendees from 15 states and 4 different countries"),
                                                           ]
                                                       )   
                                                   ),
                                               ]
                                           ),
                                           dbc.Col(
                                               [
                                                   html.P(
                                                       html.Ul(
                                                           [
                                                               html.Li("Attracted a diverse and talented pool of attendees"),
                                                               html.Li("Over 10 Fortune 500 Companies represented"),
                                                               html.Li("Provided learning opportunities for both advanced strategic and technical content"),
                                                           ]
                                                       )   
                                                   )
                                                ]
                                            )
                                        ],className="two columns",style={"color":"white"}
                                    )
                                ],className="product"
                            ),
                        ],className="row",
                    )
                ],
                className="sub_page",style={'min-height':'200mm'}
            ),
        ],
        className="page",
    )