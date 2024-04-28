import dash
from dash import dcc, html
from connection import fetch_data
from graph import *

data1 = fetch_data("""   
    SELECT species, COUNT(*) AS count
    FROM aves
    GROUP BY species
    ORDER BY count DESC
    LIMIT 10""")

fig1 = plot_bar_chart(data1) 
fig1.update_layout(
    width=400,  # Ancho de la gráfica en píxeles
    height=300  # Altura de la gráfica en píxeles
)

data3 = fetch_data("""    
    SELECT iucnRedListCategory, COUNT(*) AS count
    FROM aves
    WHERE iucnRedListCategory IS NOT NULL
    GROUP BY iucnRedListCategory;""")

fig2 = plot_pie_chart(data3)  
fig2.update_layout(
    width=270,  # Ancho de la gráfica en píxeles
    height=380  # Altura de la gráfica en píxeles
)  

data2 = fetch_data("""
    SELECT stateprovince AS Departamento, COUNT(DISTINCT species) AS Especies_Unicas, COUNT(*) AS Observaciones_Total
    FROM aves
    GROUP BY stateprovince
    ORDER BY Observaciones_Total DESC""")

fig3 = plot_bubble_chart(data2)
fig3.update_layout(
    width=700,  # Ancho de la gráfica en píxeles
    height=320  # Altura de la gráfica en píxeles
)

data4 = fetch_data("""
    SELECT EXTRACT(YEAR FROM eventDate) AS year, EXTRACT(MONTH FROM eventDate) AS month, COUNT(*) AS count
    FROM aves
    GROUP BY year, month
    ORDER BY year, month;""")

fig4 = plot_line_chart(data4)
fig4.update_layout(
    width=750,  # Ancho de la gráfica en píxeles
    height=300  # Altura de la gráfica en píxeles
)

data5 = fetch_data("""
SELECT institutionCode, COUNT(*) AS count
FROM aves
GROUP BY institutionCode
ORDER BY count DESC
LIMIT 3;
""")

fig5 = plot_indicators_chart(data5)
fig5.update_layout(
    width=250,  # Ancho de la gráfica en píxeles
    height=430  # Altura de la gráfica en píxeles
)

total_registros_data = fetch_data("""
SELECT COUNT(*) AS total_registros 
FROM aves;
""")
total_registros = total_registros_data[0][0]

numero_especies_data = fetch_data("""
SELECT COUNT(DISTINCT species) AS numero_especies
FROM aves;
""")
numero_especies = numero_especies_data[0][0]

##########################################################################################################################################
dash.register_page(__name__,path="/dash_page",name = "Dashboard")

layout = html.Div([
    html.Div(
        dcc.Graph(
            id='mi-grafica',
            figure=fig1
        ),
        id='grafica-contenedor1'
    ),
    html.Div(
        dcc.Graph(
        id='mi-grafica2', 
        figure=fig2
        ), 
        id = 'grafica-contenedor2'
    ),
    html.Div(
        dcc.Graph(
            id='mi-grafica3',
            figure=fig3
        ),
        id='grafica-contenedor3'
    ),
    html.Div(
        dcc.Graph(
            id='mi-grafica4',
            figure=fig4
        ),
        id='grafica-contenedor4'
    ),
    html.Div(
        dcc.Graph(
            id='mi-grafica5',
            figure=fig5
        ),
        id='grafica-contenedor5'
    ),
    html.Div(id='map-container', children=[
        html.Iframe(srcDoc=open('src/assets/mapa.html', 'r').read(), width='100%', height='100%')
    ]),

    html.Div(
        className='tarjeta',
        id='tarjeta-total-registros',
        children=[
            html.H3('Total Registros'),
            html.P(str(total_registros))
        ]
    ),

    html.Div(
        className='tarjeta',
        id='tarjeta-numero-especies',
        children=[
            html.H3('Número Especies'),
            html.P(str(numero_especies))
        ]
    ),
])