from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from src.app.dash_app import app
from src.app.paginas import home, dados
import pandas as pd

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('Dados', href='/dados')),
    ],
    brand="Previsão de preços imobiliários",
    brand_href="/home",
    color="primary",
    dark=True,
    fluid=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navegacao,
    html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [Input('url', 'pathname')] 
)

def mostrar_pagina(pathname):
    if pathname == '/dados':
        return dados.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')