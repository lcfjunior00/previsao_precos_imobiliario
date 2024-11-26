from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np
from app import app
import catboost
from assets.assets_home import formulario

layout = html.Div([
    formulario,
    html.Div(id='previsao')
])

@app.callback(
    Output('previsao', 'children'),
   [Input('botao_prever', 'n_clicks')],
   [State('lotarea', 'value'),
    State('totalbsmtsf', 'value'),
    State('oneflrsf', 'value'),
    State('twoflrsf', 'value'),
    State('grlivarea', 'value'),
    State('garagearea', 'value'),
    State('wooddecksf', 'value'),
    State('openporchsf', 'value'),
    State('overallqual', 'value'),
    State('overallcond', 'value'),
    State('bsmthalfbath', 'value'),
    State('fullbath', 'value'),
    State('halfbath', 'value'),
    State('totrmsabvgrd', 'value'),
    State('fireplaces', 'value'),
    State('garagecars', 'value'),
    State('mszoning', 'value'),
    State('street', 'value'),
    State('lotshape', 'value'),
    State('lotconfig', 'value'),
    State('neighborhood', 'value'),
    State('foundation', 'value'),
    State('heating', 'value'),
    State('centralair', 'value'),
    State('saletype', 'value'),
    State('salecondition', 'value'),
    State('exterqual', 'value'),
    State('extercond', 'value'),
    State('bsmtqual', 'value'),
    State('bsmtcond', 'value'),
    State('bsmtexposure', 'value'),
    State('kitchenqual', 'value'),
    State('garagefinish', 'value')
])

#Função prever:
def prever_preco(n_clicks, lotarea, totalbsmtSF, oneflrsf, twoflrsf, grlivarea, garagearea, wooddecksf, openporchsf, overallqual, overallcond, bsmthalfbath, fullbath, halfbath, totrmsabvgrd, fireplaces, garagecars, mszoning, street, lotshape, lotconfig, neighborhood, foundation, heating, centralair, saletype, salecondition, exterqual, extercond, bsmtqual, bsmtcond, bsmtexposure, kitchenqual, garagefinish):
    '''
    Essa função irá receber todos os estados colhidos nos inputs, criar um dataframe e 
    fazer a predição do valor do imóvel.
    '''
    #Carrega modelo:
    modelo = joblib.load(r'C:/Users/luizc/OneDrive/Documentos/Junior/Profissional/CV/Portifólio Ciência de Dados/Projetos/Previsão_de_precos_imobiliarios_deploy/previsao_precos_imobiliario/models/cat_best_model.pkl')


    #Esse if impede que a página tente prever um valor mesmo sem ter um click no botão.
    if n_clicks == 0 or n_clicks is None:
        return ''
    
    entradas_usuario = pd.DataFrame(
       data=[[lotarea, totalbsmtSF, oneflrsf, twoflrsf, grlivarea, garagearea, wooddecksf, openporchsf,
           overallqual, overallcond, bsmthalfbath, fullbath, halfbath, totrmsabvgrd, fireplaces,
           garagecars, mszoning, street, lotshape, lotconfig, neighborhood, foundation, heating,
           centralair, saletype, salecondition, exterqual, extercond, bsmtqual, bsmtcond, bsmtexposure,
           kitchenqual, garagefinish]],
       columns=['LotArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 
           'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'OverallQual', 'OverallCond', 
           'BsmtHalfBath', 'FullBath', 'HalfBath', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 
           'MSZoning', 'Street', 'LotShape', 'LotConfig', 'Neighborhood', 'Foundation', 
           'Heating', 'CentralAir', 'SaleType', 'SaleCondition', 'ExterQual', 'ExterCond', 
           'BsmtQual', 'BsmtCond', 'BsmtExposure', 'KitchenQual', 'GarageFinish']
    )

    var_int = ['LotArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 
           'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'OverallQual', 'OverallCond', 
           'BsmtHalfBath', 'FullBath', 'HalfBath', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars']

    var_str = ['MSZoning', 'Street', 'LotShape', 'LotConfig', 'Neighborhood', 'Foundation', 
              'Heating', 'CentralAir', 'SaleType', 'SaleCondition', 'ExterQual', 'ExterCond', 
              'BsmtQual', 'BsmtCond', 'BsmtExposure', 'KitchenQual', 'GarageFinish']

    for col in var_int:
        entradas_usuario[col] = entradas_usuario[col].astype(np.int64)

    for col in var_str:
        entradas_usuario[col] = entradas_usuario[col].astype(str)

    try:
        previsao = modelo.predict(entradas_usuario)[0]
        alerta = dbc.Alert(f'Preço previsto: US$ {previsao:.2f}', className='d-flex justify-content-center mb-5', color='light')
        return alerta
    except Exception as e:
        alerta = dbc.Alert(f'Erro na previsão: {str(e)}', color='danger', className='d-flex justify-content-center mb-5')
        return alerta