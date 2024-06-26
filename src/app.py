import dash
from dash import html, dcc

app = dash.Dash(__name__, use_pages=True)

orden_paginas = [
    {"name": "Introducción", "relative_path": "/introduction"},
    {"name": "Descripción de datos", "relative_path": "/description"},
    {"name": "Dashboard", "relative_path": "/dash_page"},
]

app.layout = html.Div(
    [
        dash.page_container,  # Contenedor principal de páginas
        
        # Contenedor de los enlaces/botones, que ahora está al final
        html.Div(
            [
                dcc.Link(
                    page["name"], 
                    href=page["relative_path"], 
                    className="custom-link"
                )
                for page in orden_paginas
            ],
            className="link-container"  # Clase para el nuevo contenedor
        ),

        html.Div(
            "Aves del Caribe Colombiano",
            id='nombre-aves',
        ),
        
        html.Div(
            "Kenny Zhu, Shadia Jaafar y Mariana Castañeda",
            id='nombre-contenedor',
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
