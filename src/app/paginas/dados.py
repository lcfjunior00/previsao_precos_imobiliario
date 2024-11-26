from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from assets.assets_dados import home_left_1, home_left_2, home_right

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card(
                    home_left_1, color='terciary', outline=True, className='d-flex justify-content-center mb-3'
                ),
                dbc.Card(
                    home_left_2, color='terciary', outline=True
                )
            ]),
            dbc.Col([
                dbc.Card(
                    home_right, color='terciary', outline=True
                )
            ])
        ], className='mt-3')
    ], fluid=True)
])