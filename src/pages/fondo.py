import dash
from dash import html

dash.register_page(__name__,path="/",name="fondo")

layout = html.Div([
    html.Div(
        html.Img(src="assets/fondo2.jpeg", 
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
