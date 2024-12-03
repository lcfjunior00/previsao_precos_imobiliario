import dash_bootstrap_components as dbc
from dash import html

#Formulário de preenchimento das varíaveis:
formulario = dbc.Container([
    html.P("Explicação de cada variável está presente na página Dados", className="text-center mb-3 mt-3"),
    html.P("Preencha as informações abaixo e clique em prever para rodar o modelo", className="text-center mb-5"),
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Label("LotArea"),
                dbc.Input(id='lotarea', type='number', placeholder='Digite o tamanho do imóvel em pés quadrados'),
            ], className='mb-3'),
            dbc.CardGroup([ 
                dbc.Label("TotalBsmtSF"),
                    dbc.Input(id='totalbsmtsf', type='number', placeholder='Digite o tamanho do porão em pés quadrados'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("1stFlrSF"),
                dbc.Input(id='oneflrsf', type='number', placeholder='Digite o tamanho do 1º andar em pés quadrados'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("2ndFlrSF"),
                dbc.Input(id='twoflrsf', type='number', placeholder='Digite o tamanho do 2º andar em pés quadrados'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("GrLivArea"),
                dbc.Input(id='grlivarea', type='number', placeholder='Digite o tamanho da área de vivência em pés quadrado'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("GarageArea"),
                dbc.Input(id='garagearea', type='number', placeholder='Digite o tamanho da área de vivência em pés quadrado'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("WoodDeckSF"),
                dbc.Input(id='wooddecksf', type='number', placeholder='Digite o tamanho do deck de madeira em pés quadrado'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('OpenPorchSF'),
                dbc.Input(id='openporchsf', type='number', placeholder='Digite o tamanho da varanda em pés quadrados'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('OverallQual'),
                dbc.Select(id='overallqual', options=[
                    {'label': '1', 'value': '1'},
                    {'label': '2', 'value': '2'},
                    {'label': '3', 'value': '3'},
                    {'label': '4', 'value': '4'},
                    {'label': '5', 'value': '5'},
                    {'label': '6', 'value': '6'},
                    {'label': '7', 'value': '7'},
                    {'label': '8', 'value': '8'},
                    {'label': '9', 'value': '9'},
                    {'label': '10', 'value': '10'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('OverallCond'),
                dbc.Select(id='overallcond', options=[
                    {'label': '1', 'value': '1'},
                    {'label': '2', 'value': '2'},
                    {'label': '3', 'value': '3'},
                    {'label': '4', 'value': '4'},
                    {'label': '5', 'value': '5'},
                    {'label': '6', 'value': '6'},
                    {'label': '7', 'value': '7'},
                    {'label': '8', 'value': '8'},
                    {'label': '9', 'value': '9'},
                    {'label': '10', 'value': '10'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('BsmtHalfBath'),
                dbc.Input(id='bsmthalfbath', type='number', placeholder='Digite o número de meios banheiros do porão'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('FullBath'),
                dbc.Input(id='fullbath', type='number', placeholder='Digite o número de banheiros acima do solo'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('HalfBath'),
                dbc.Input(id='halfbath', type='number', placeholder='Digite o número de meios banheiros acima do solo'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('TotRmsAbvGrd'),
                dbc.Input(id='totrmsabvgrd', type='number', placeholder='Digite o número de cômodos acima do solo'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Fireplaces'),
                dbc.Input(id='fireplaces', type='number', placeholder='Digite o número de lareiras'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('GarageCars'),
                dbc.Input(id='garagecars', type='number', placeholder='Digite o número máximo de carros na garagem'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('MSZoning'),
                dbc.Select(id='mszoning', options=[
                    {'label': 'Agriculture', 'value': 'A'},
                    {'label': 'Commercial', 'value': 'C'},
                    {'label': 'Floating Village Residential', 'value': 'FV'},
                    {'label': 'Industrial', 'value': 'I'},
                    {'label': 'Residential High Density', 'value': 'RH'},
                    {'label': 'Residential Low Density', 'value': 'RL'},
                    {'label': 'Residential Low Density Park', 'value': 'RP'},
                    {'label': 'Residential Medium Density', 'value': 'RM'}
                ]),
            ], className='mb-3')
        ]),
        dbc.Col([
            dbc.CardGroup([
                dbc.Label('Street'),
                dbc.Select(id='street', options=[
                    {'label': 'Gravel', 'value': 'Grvl'},
                    {'label': 'Paved', 'value': 'Pave'}
                ])
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('LotShape'),
                dbc.Select(id='lotshape', options=[
                    {'label': 'Regular', 'value': 'Reg'},
                    {'label': 'Slightly irregular', 'value': 'IR1'},
                    {'label': 'Moderately Irregular', 'value': 'IR2'},
                    {'label': 'Irregular', 'value': 'IR3'}
                ])
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("LotConfig"),
                dbc.Select(id='lotconfig', options=[
                    {'label': 'Inside lot', 'value': 'Inside'},
                    {'label': 'Corner lot', 'value': 'Corner'},
                    {'label': 'Frontage on 2 sides of property', 'value': 'FR2'},
                    {'label': 'Frontage on 3 sides of property', 'value': 'FR3'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("Neighborhood"),
                dbc.Select(id='neighborhood', options=[
                    {'label': 'Bloomington Heights', 'value': 'Blmngtn'},
                    {'label': 'Bluestem', 'value': 'Blueste'},
                    {'label': 'Briardale', 'value': 'BrDale'},
                    {'label': 'Brookside', 'value': 'BrkSide'},
                    {'label': 'Clear Creek', 'value': 'ClearCr'},
                    {'label': 'College Creek', 'value': 'CollgCr'},
                    {'label': 'Crawford', 'value': 'Crawfor'},
                    {'label': 'Edwards', 'value': 'Edwards'},
                    {'label': 'Gilbert', 'value': 'Gilbert'},
                    {'label': 'Iowa DOT and Rail Road', 'value': 'IDOTRR'},
                    {'label': 'Meadow Village', 'value': 'MeadowV'},
                    {'label': 'Mitchell', 'value': 'Mitchel'},
                    {'label': 'North Ames', 'value': 'Names'},
                    {'label': 'Northridge', 'value': 'NoRidge'},
                    {'label': 'Northpark Villa', 'value': 'NPkVill'},
                    {'label': 'Northridge Heights', 'value': 'NridgHt'},
                    {'label': 'Northwest Ames', 'value': 'NWAmes'},
                    {'label': 'Old Town', 'value': 'OldTown'},
                    {'label': 'South & West of Iowa State University', 'value': 'SWISU'},
                    {'label': 'Sawyer', 'value': 'Sawyer'},
                    {'label': 'Sawyer West', 'value': 'SawyerW'},
                    {'label': 'Somerset', 'value': 'Somerst'},
                    {'label': 'Stone Brook', 'value': 'StoneBr'},
                    {'label': 'Timberland', 'value': 'Timber'},
                    {'label': 'Veenker', 'value': 'Veenker'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("Foundation"),
                dbc.Select(id='foundation', options=[
                    {'label': 'Brick & Tile', 'value': 'BrkTil'},
                    {'label': 'Cinder Block', 'value': 'CBlock'},
                    {'label': 'Poured Contrete', 'value': 'PConc'},
                    {'label': 'Slab', 'value': 'Slab'},
                    {'label': 'Stone', 'value': 'Stone'},
                    {'label': 'Wood', 'value': 'Wood'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("Heating"),
                dbc.Select(id='heating', options=[
                    {'label': 'Floor Furnace', 'value': 'Floor'},
                    {'label': 'Gas forced warm air furnace', 'value': 'GasA'},
                    {'label': 'Gas hot water or steam heat', 'value': 'GasW'},
                    {'label': 'Gravity furnace', 'value': 'Grav'},
                    {'label': 'Hot water or steam heat other than gas', 'value': 'OthW'},
                    {'label': 'Wall furnace', 'value': 'Wall'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("CentralAir"),
                dbc.Select(id='centralair', options=[
                    {'label': 'No', 'value': 'N'},
                    {'label': 'Yes', 'value': 'Y'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("SaleType"),
                dbc.Select(id='saletype', options=[
                    {'label': 'Warranty Deed - Conventional', 'value': 'WD'},
                    {'label': 'Warranty Deed - Cash', 'value': 'CWD'},
                    {'label': 'Warranty Deed - VA Loan', 'value': 'VWD'},
                    {'label': 'Home just constructed and sold', 'value': 'New'},
                    {'label': 'Court Officer Deed/Estate', 'value': 'COD'},
                    {'label': 'Contract 15% Down payment regular terms', 'value': 'Con'},
                    {'label': 'Contract Low Down payment and low interest', 'value': 'ConLw'},
                    {'label': 'Contract Low Interest', 'value': 'ConLI'},
                    {'label': 'Contract Low Down', 'value': 'ConLD'},
                    {'label': 'Other', 'value': 'Oth'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("SaleCondition"),
                dbc.Select(id='salecondition', options=[
                    {'label': 'Normal Sale', 'value': 'Normal'},
                    {'label': 'Abnormal Sale -  trade, foreclosure, short sale', 'value': 'Abnorml'},
                    {'label': 'Adjoining Land Purchase', 'value': 'AdjLand'},
                    {'label': 'Allocation - two linked properties with separate deeds, typically condo with a garage unit', 'value': 'Alloca'},
                    {'label': 'Sale between family members', 'value': 'Family'},
                    {'label': 'Home was not completed when last assessed (associated with New Homes)', 'value': 'Partial'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("ExterQual"),
                dbc.Select(id='exterqual', options=[
                    {'label': 'Excellent', 'value': 'Ex'},
                    {'label': 'Good', 'value': 'Gd'},
                    {'label': 'Average/Typical', 'value': 'TA'},
                    {'label': 'Fair', 'value': 'Fa'},
                    {'label': 'Poor', 'value': 'Po'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("ExterCond"),
                dbc.Select(id='extercond', options=[
                    {'label': 'Excellent', 'value': 'Ex'},
                    {'label': 'Good', 'value': 'Gd'},
                    {'label': 'Average/Typical', 'value': 'TA'},
                    {'label': 'Fair', 'value': 'Fa'},
                    {'label': 'Poor', 'value': 'Po'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("BsmtQual"),
                dbc.Select(id='bsmtqual', options=[
                    {'label': 'Excellent', 'value': 'Ex'},
                    {'label': 'Good', 'value': 'Gd'},
                    {'label': 'Average/Typical', 'value': 'TA'},
                    {'label': 'Fair', 'value': 'Fa'},
                    {'label': 'Poor', 'value': 'Po'},
                    {'label': 'No Basement', 'value': 'NA'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("BsmtCond"),
                dbc.Select(id='bsmtcond', options=[
                    {'label': 'Excellent', 'value': 'Ex'},
                    {'label': 'Good', 'value': 'Gd'},
                    {'label': 'Average/Typical', 'value': 'TA'},
                    {'label': 'Fair', 'value': 'Fa'},
                    {'label': 'Poor', 'value': 'Po'},
                    {'label': 'No Basement', 'value': 'NA'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("BsmtExposure"),
                dbc.Select(id='bsmtexposure', options=[
                    {'label': 'Good Exposure', 'value': 'Gd'},
                    {'label': 'Average Exposure', 'value': 'Av'},
                    {'label': 'Mimimum Exposure', 'value': 'Mn'},
                    {'label': 'No Exposure', 'value': 'No'},
                    {'label': 'No Basement', 'value': 'NA'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("KitchenQual"),
                dbc.Select(id='kitchenqual', options=[
                    {'label': 'Excellent', 'value': 'Ex'},
                    {'label': 'Good', 'value': 'Gd'},
                    {'label': 'Typical/Average', 'value': 'TA'},
                    {'label': 'Fair', 'value': 'Fa'},
                    {'label': 'Poor', 'value': 'Po'}
                ]),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label("GarageFinish"),
                dbc.Select(id='garagefinish', options=[
                    {'label': 'Finished', 'value': 'Fin'},
                    {'label': 'Rough Finished', 'value': 'RFn'},
                    {'label': 'Unfinished', 'value': 'Unf'},
                    {'label': 'No Garage', 'value': 'NA'},
                ]),
            ], className='mb-3'),
            dbc.Button("Prever", id='botao_prever', color='success', n_clicks=0, className='mb-3 mt-3')
        ])
    ])
])

