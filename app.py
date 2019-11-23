# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview, titles, industries, companies, location, experiencelevels
)
from plotly import express as px
import pandas as pd
import numpy as np
import pathlib
import json

# Path
#BASE_PATH = pathlib.Path(__file__).parent.resolve()
#DATA_PATH = BASE_PATH.joinpath(".\data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div([
    dcc.Location(id="url", refresh=False), 
    html.Div(id="page-content"),
    html.Div(id='graph_container')
])

# Update page
@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/venv/titles":
        return titles.create_layout(app)
    elif pathname == "/venv/companies":
        return companies.create_layout(app)
    elif pathname == "/venv/experiencelevels":
        return experiencelevels.create_layout(app)
    elif pathname == "/venv/industries":
        return industries.create_layout(app)
    elif pathname == "/venv/location":
        return location.create_layout(app)
    elif pathname == "/venv/full-view":
        return (
            overview.create_layout(app),
            titles.create_layout(app),
            companies.create_layout(app),
            experiencelevels.create_layout(app),
            industries.create_layout(app),
            location.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)