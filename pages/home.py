import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

buttons = html.Div(
    [
        #dbc.Button("Go to MutAnTs", color="primary", className="me-1", href='mutants'),
        #dbc.Button("Go to MutAnTs", color="secondary", className="me-1", href='mutants'),
        dbc.Button("Explore", color="primary", className="me-1", href='mutants'),
    ]
)

layout = html.Div(
    [
        html.P([
            'MutAnTs ',
            html.B('(Mutation Analysis Tools)'),
            #html.Div(
            ' Viewer is an easy and interactive web server for '
            'querying mutation analysis tools. It combines data visualization techniques and an extensive '
            'list of tools to provide the end user with a simple research platform, involving important aspects such as '
            'the publication journal and its relevance.'
        ]),
        html.P(
            html.Div(
            'The web server was developed in Python, using the Pandas library (version 1.4.2) for data manipulation and '
            'Plotly for creating graphical components. Integration of back-end and front-end environments takes place through '
            'Dash (version 2.4.1).')
        ),
        buttons
    ],
    style={'textAlign': 'justify'},
    #className='col py-3 px-md-5 border bg-light'
    className='col py-3 px-md-5 border'
)