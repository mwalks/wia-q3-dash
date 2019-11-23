# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import pathlib
from dash.dependencies import Input, Output
from utils import Header, make_dash_table, get_header, get_menu

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("..\data").resolve()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([
                html.Div(
                    [
                        html.Div(
                            [
                                html.A(
                                    html.Img(id="wia-link",
                                             src=app.get_asset_url(
                                                 "WIA_logo.jpg"),
                                             className="logo",
                                             ), href="https://womeninanalytics.com", style={"transition-duration": "1s"}
                                ),
                            ],
                            className="row",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [html.H5(
                                        "Women in Analytics 2020 Conference: Q3 Report")],
                                    className="seven columns main-title",
                                ),
                                html.Div(
                                    [
                                        dcc.Link(
                                            "Full View",
                                            href="/venv/full-view",
                                            className="full-view-link",
                                        )
                                    ],
                                    className="five columns",
                                ),
                            ],
                            className="twelve columns",
                            style={"padding-left": "0"},
                        ),
                        html.Div([
                            html.A("authored by Matthew Walker",
                                   href='https://www.linkedin.com/in/matthew-j-walker-osu/',
                                   style={'padding-left': '10%'}
                                   ),
                        ]),
                        html.Div(
                            [html.H3(
                                [
                                    "3 Days | 1200+ Attendees | 47 Speakers"
                                ],
                            )
                            ],
                            className="statbanner"
                        ),
                    ],
                    className="row",
                ),
                get_menu()
            ]),
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
                        ], className="iframe"
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
                                                                html.Li(
                                                                    "The 4rd Annual WIA Conference"),
                                                                html.Li(
                                                                    "Double last year's attendees"),
                                                                html.Li(
                                                                    "Expanded to 3 days"),
                                                                html.Li(
                                                                    "Had attendees from 15 states and 4 different countries"),
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
                                                                html.Li(
                                                                    "Attracted a diverse and talented pool of attendees"),
                                                                html.Li(
                                                                    "Over 10 Fortune 500 Companies represented"),
                                                                html.Li(
                                                                    "Provided learning opportunities for both advanced strategic and technical content"),
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ], className="two columns", style={"color": "white"}
                                    )
                                ], className="product"
                            ),
                        ], className="row",
                    )
                ],
                className="sub_page", style={'min-height': '200mm'}
            ),
        ],
        className="page",
    )
