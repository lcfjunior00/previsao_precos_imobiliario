from dash import html
import dash_bootstrap_components as dbc
from assets.imagens import logo_kaggle, imagem_competicao_houseprices, imagem_mapa_iowa
from assets.urls import url_houseprices

home_left_1 = [
    dbc.CardHeader("Origem:"),
    dbc.CardBody([
            html.P('Competição Kaggle chamada: House Prices - Advanced Regression Techniques (link abaixo)', className="card-text mb-3"),
            dbc.Button([html.Img(src=logo_kaggle, alt='Logo', style={'height': '20px', 'marginRight': '5px'}),
            ],
            target='_blank',
            href=url_houseprices,
            color='light',
            id='botao-com-logo',
            className='d-flex justify-content-center mb-3'  # Para alinhar a imagem e o texto
            ),
            html.Img(src=imagem_competicao_houseprices, style={'width': '100%', 'height': 'auto'}, className='mb-3'),
            html.H2("Descrição da competição:", style={'font-size': '18px'}, className='mt-3'),
            html.P('Peça a um comprador de imóveis para descrever a casa dos seus sonhos, e ele provavelmente não começará com a altura do teto do porão ou a proximidade de uma ferrovia leste-oeste. Mas o conjunto de dados desta competição prova que muito mais influencia as negociações de preços do que o número de quartos ou uma cerca branca.'),
            html.P('Os dados do DataSet são de imóveis residenciais localizados na cidade de Ames, no estado norte-americano de Iowa (em vermelho na imagem abaixo).', className='mb-3'),
        dbc.Container([
            html.Img(src=imagem_mapa_iowa)
            ],style={'textAlign': 'center'})
    ]),
]

home_left_2 = [
    dbc.CardHeader('DataSet inicial:'),
    dbc.CardBody([
        html.P('Número de linhas: 1.460'),
        html.P('Número de colunas: 81')
    ])
]

home_right = [
    dbc.CardHeader("Dicionário de dados (somente features selecionadas):"),
    dbc.CardBody([
            html.P('1.  LotArea: Tamanho da área do imóvel em pés quadrados.'),
            html.P('2.  TotalBsmtSF: Total de pés quadrados de área do porão.'),
            html.P('3.  1stFlrSF: Tamanho da área do 1º andar em pés quadrados.'),
            html.P('4.  2ndFlrSF: Tamanho da área do 2º andar em pés quadrados.'),
            html.P('5.  GrLivArea: Área habitável acima do nível do solo em pés quadrados.'),
            html.P('6.  GarageArea: Tamanho da garagem em pés quadrados.'),
            html.P('7.  WoodDeckSF: Área do deck de madeira em pés quadrados.'),
            html.P('8.  OpenPorchSF: Área de varanda aberta em pés quadrados.'),
            html.P('9.  OverallQual: Avalia o material geral e o acabamento da casa.'),
            html.P('10. OverallCond: Avalia o estado geral da casa.'),
            html.P('11. BsmtHalfBath: Meios banheiros no porão.'),
            html.P('12. FullBath: Banheiros completos acima do nível do solo.'),
            html.P('13. HalfBath: Meios banheiros no porão.'),
            html.P('14. TotRmsAbvGrd: Total de cômodos acima do nível do solo (não inclui banheiros).'),
            html.P('15. Fireplaces: Número de lareiras.'),
            html.P('16. GarageCars: Máximo número de carros na garagem.'),
            html.P('17. MSZoning: Identifica a classificação geral de zoneamento da venda.'),
            html.P('18. Street: Tipo de acesso rodoviário à propriedade.'),
            html.P('19. LotShape: Forma geral da propriedade.'),
            html.P('20. LotConfig: Configuração de lote.'),
            html.P('21. Neighborhood: Bairro.'),
            html.P('22. Foundation: Tipo de fundação.'),
            html.P('23. Heating: Tipo de aquecedor.'),
            html.P('24. CentralAir: Ar condicionado central?'),
            html.P('25. SaleType: Tipo de venda.'),
            html.P('26. SaleCondition: Condição de venda.'),
            html.P('27. ExterQual: Avalia a qualidade do material no exterior.'),
            html.P('28. ExterCond: Avalia a condição atual do material no exterior.'),
            html.P('29. BsmtQual: Altura do porão.'),
            html.P('30. BsmtCond: Avalia a qualidade geral do porão.'),
            html.P('31. BsmtExposure: Refere-se a muros de saída ou de nível de jardim.'),
            html.P('32. KitchenQual: Qualidade da cozinha.'),
            html.P('33. GarageFinish: Acabamento interior da garagem.')
        ]),
]