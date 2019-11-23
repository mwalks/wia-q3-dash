# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import pathlib
from dash.dependencies import Input, Output
from utils import Header, make_dash_table
from plotly import express as px
from PIL import Image

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("..\data").resolve()

# the bar polar plot
p3 = px.bar_polar(
    pd.read_csv(DATA_PATH.joinpath("shortcut_ind.csv")),
    r='Frequency',
    theta='Industry',
    barnorm='percent',
    color_discrete_map={'': px.colors.sequential.Sunsetdark},
    width=750,
    height=550,
    start_angle=95,
    title='Industry of Attendees (%)'
).update(layout=dict(images=[dict(
    source=Image.open(BASE_PATH.joinpath(r'''..\assets''').joinpath("WIA_logo.jpg")),
    xref="paper", yref="paper",
    x=0.470, y=0.450,
    sizex=0.1, sizey=0.1,
    xanchor="left", yanchor="bottom"
)],
    title=dict(
    x=0.5
),
    font_size=13,
    polar=dict(
    sector=[89, 435],
    hole=0.15,
    bargap=0.3,
    radialaxis=dict(
        gridcolor="lightgray",
        showline=False,
        tickangle=90,
        ticksuffix="%"
    ),
    angularaxis=dict(
        gridcolor="gray"
    ),
    gridshape="circular",
    bgcolor="white"
)
)
)


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # industry page
            html.Div(
                [
                    html.Div([
                        html.Hr(style={"border-top": "2px solid lightgrey",
                                       "margin-top": "0", "margin-bottom": "3.5rem"}),
                        html.H6(
                            "What industries do attendees work in?",
                            className="subtitle", style={"margin-left": "10%", "margin-bottom": "25px", "font-size": "2rem"}
                        ),
                        dbc.Row([
                            dcc.Graph(
                                    id="graph3",
                                    figure=p3,
                                    config={
                                        'displayModeBar': False
                                    },
                                    style={"width":"100%","display": "inline-block","align":"center"}
                                ),
                        ])
                    ], className="row"
                    ),
                    html.Br(),
                    html.Div(html.I(
                        r'''The industry with most representation is healthcare / life sciences / pharmaceuticals at 27%, followed by insurance,and then other and manufacturing.'''
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
from PIL import Image

#assume data cleaned already
df = q3_analysis_work.industry.value_counts().to_frame() .reset_index().rename(columns={"index":"Industry","industry":"Frequency"})

px.bar_polar(
    df,
    r='Frequency',
    theta='Industry',
    barnorm='percent',
    color_discrete_map={'':px.colors.sequential.Sunsetdark},
    width=800,
    height=550,
    start_angle=95,
    title='Industry of Attendees (%)'
    ).update(layout=dict(images=[dict(
        source=Image.open(pathlib.Path("testing.ipynb").parent.resolve().joinpath("assets").joinpath("WIA_logo.jpg")),
        xref="paper", yref="paper",
        x=0.461, y=0.452,
        sizex=0.1, sizey=0.1,
        xanchor="left", yanchor="bottom"
    )],
    title=dict(
        x=0.5
        ),
        font_size=13,
        polar=dict(
                sector=[89,435],
                hole=0.15,
                bargap=0.3,
                radialaxis=dict(
                    gridcolor="lightgray",
                    showline=False,
                    tickangle=90,
                    ticksuffix="%"
                ),
                angularaxis=dict(
                        gridcolor="gray"
                    ),
                    gridshape="circular",
                    bgcolor="white"
                    )
                )
            )
```
'''
                                         ), className="row", style={"overflow": "scroll", "height": "400px"}
                        )
                    ]),
                    html.P(
                        [
                            "More detailed code can be found at ",
                            html.A("https://github.com/mwalks/wia-q3-dash",
                                   href="https://github.com/mwalks/wia-q3-dash"),
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
