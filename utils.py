import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("WIA_logo.jpg"),
                        className="logo",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Women in Analytics 2020 Conference: Q3 Attendee Report")],
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
            html.Div(
                [
                    html.H4("3 Days | 1200+ Attendees | 47 Speakers")
                ],
                className="statbanner"
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Titles",
                href="/dash-financial-report/titles",
                className="tab first",
            ),
            dcc.Link(
                "Companies",
                href="/dash-financial-report/companies",
                className="tab",
            ),
            dcc.Link(
                "Experience Levels",
                href="/dash-financial-report/experience-levels",
                className="tab",
            ),
            dcc.Link(
                "Industries", href="/dash-financial-report/industries",
                className="tab"
            ),
            dcc.Link(
                "Location",
                href="/dash-financial-report/location",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table