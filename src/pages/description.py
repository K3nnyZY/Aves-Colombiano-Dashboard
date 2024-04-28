import dash
from dash import html

dash.register_page(__name__,path="/description",name="Descripción de datos")

layout = html.Div([
    html.Div(
        html.Img(src="assets/description.png", 
                 style={'width': '100%',
                        'height': '100%',
                        'margin': '0',
                        'padding': '0',
                        'object-fit': 'cover',
                        'background-position': 'center',
                        'background-repeat': 'no-repeat',
                        'background-size': 'cover'}),
    ),
])
