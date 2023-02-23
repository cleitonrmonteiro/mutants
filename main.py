from dash import Dash, html, dcc
import dash

import dash_bootstrap_components as dbc

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = Dash(__name__,  external_stylesheets=external_stylesheets, use_pages=True)

#app = Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
#app = Dash(__name__,  external_stylesheets=[dbc.themes.FLATLY], use_pages=True)
app = Dash(__name__,  external_stylesheets=[dbc.themes.SANDSTONE], use_pages=True)

#app = Dash(__name__,  use_pages=True)
#app = Dash(__name__, suppress_callback_exceptions=True)

#inserindo a navbar
navbar = dbc.NavbarSimple(
    children=[
        #dbc.NavItem(dbc.NavLink("About", href="/")),
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        #dbc.NavItem(dbc.NavLink("Go to MutAnTs", href="mutants")),
        dbc.NavItem(dbc.NavLink("Explore", href="mutants")),
        #dbc.NavItem(dbc.NavLink("Get started", href="mutants")),
        dbc.NavItem(dbc.NavLink("Help", href=""))
    ],
    brand="MutAnTs Viewer",
    brand_href="/",
    color="primary",
    #color="black",
    dark=True,
)

app.layout = html.Div([
	#html.H1('Multi-page app with Dash Pages'),
    navbar,
    #html.Div(
    #    [
    #        html.Div(
    #            dcc.Link(
    #                #f"{page['name']} - {page['path']}", href=page["relative_path"]
    #                f"{page['name']}", href=page["relative_path"]
    #            )
    #        )
    #        for page in dash.page_registry.values()
    #    ]
    #),
	dash.page_container
])

if __name__ == '__main__':
	#app.run_server(debug=True)
    app.run()