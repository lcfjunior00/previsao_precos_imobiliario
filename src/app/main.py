from dash import Dash, html, dcc # type: ignore
import dash_bootstrap_components as dbc # type: ignore
from dash.dependencies import Input, Output # type: ignore
from app import app
from paginas import home, dados
import pandas as pd

from src import models

navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('Dados', href='/dados')),
        dbc.NavItem(dbc.NavLink('Modelos', href='/modelos'))
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
    elif pathname == '/modelos':
        return models.layout
    else:
        return home.layout


app.run_server(debug=False, port=8080, host='0.0.0.0')