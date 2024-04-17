import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from connection import fetch_data
from graph import *

data1 = fetch_data("""   
    SELECT stateprovince AS Departamentos, COUNT(*) AS Cantidad_de_Aves
    FROM aves_colombia
    GROUP BY stateprovince
    ORDER BY Cantidad_de_Aves DESC""")

fig1 = plot_bar_chart(data1) 
fig1.update_layout(
    width=500,  # Ancho de la gráfica en píxeles
    height=300  # Altura de la gráfica en píxeles
)

fig2 = plot_pie_chart(data1)  
fig2.update_layout(
    width=450,  # Ancho de la gráfica en píxeles
    height=450  # Altura de la gráfica en píxeles
)  

data2 = fetch_data("""
    SELECT stateprovince AS Departamento, COUNT(DISTINCT species) AS Especies_Unicas, COUNT(*) AS Observaciones_Total
    FROM aves_colombia
    GROUP BY stateprovince
    ORDER BY Especies_Unicas DESC""")

fig3 = plot_bubble_chart(data2)
fig3.update_layout(
    width=600,  # Ancho de la gráfica en píxeles
    height=400  # Altura de la gráfica en píxeles
)

##########################################################################################################################################
app = dash.Dash(__name__)

app.layout = html.Div([
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
        "Kenny Zhu, Shadia Jaafar y Mariana Castañeda",
        id='nombre-contenedor'
    ),
])
if __name__ == '__main__':
    app.run_server(debug=True)
