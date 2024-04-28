import plotly.express as px
import plotly.graph_objects as go

# grafiaca de barras
def plot_bar_chart(data):
    families = [item[0] for item in data]
    counts = [item[1] for item in data]
    
    fig = px.bar(
        x=counts,
        y=families,
        labels={'y': 'Familia', 'x': 'Numero de observaciones'},
        color_discrete_sequence=["forestgreen"] * len(families), 
        title='Top 10 especies de aves mas observadas en el caribe'
    )
    fig.update_layout(
        margin=dict(l=40, r=40, t=40, b=40), 
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=False, autorange='reversed', title=''),  # Elimina el título del eje Y
        xaxis=dict(title_standoff=25, title=''),  # Elimina el título del eje X
        title={
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=14)
        }
    )
    fig.update_traces(marker_color='forestgreen')
    return fig


# grafica de pastel
def plot_pie_chart(data):
    types_of_records = [item[0] for item in data]
    counts = [item[1] for item in data]
    fig = go.Figure(data=[
        go.Pie(
            labels=types_of_records,
            values=counts,
            hole=0.4,
            marker=dict(colors=px.colors.sequential.Greens[-6:] ), 
            textinfo='label+percent', 
            insidetextorientation='radial'
        )
    ])
    fig.update_layout(
        margin=dict(l=40, r=40, t=40, b=40), 
        plot_bgcolor='white',
        title={'text': 'Proporción de categorias de riesgo', 
            'x': 0.5, 
            'y': 0.95, 
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=14)
        },
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig


# grafica de burbujas
def plot_bubble_chart(data):
    departamentos = [item[0] for item in data]
    especies_unicas = [item[1] for item in data]
    observaciones_total = [item[2] for item in data]
    fig = px.scatter(
        x=departamentos,
        y=especies_unicas,
        size=observaciones_total,
        color=especies_unicas,
        size_max=80,
        labels={'x': 'Departamento', 'y': 'Especies Únicas', 'size': 'Observaciones Totales'},
        color_continuous_scale=px.colors.sequential.Greens
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20), 
        title={'text':'Observaciones Totales por Departamento','x': 0.5},
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        xaxis=dict(title=''),  # Elimina el título del eje X
        yaxis=dict(title='')  # Elimina el título del eje Y
    )
    fig.update_yaxes(visible=False, showticklabels=False)
    return fig


# grafica de linea
def plot_line_chart(data):
    dates = [f"{int(item[0])}-{int(item[1]):02d}" for item in data] 
    counts = [item[2] for item in data]

    fig = px.line(
        x=dates,
        y=counts,  
        labels={'x': 'Año', 'y': 'numero de registros'},
    )

    fig.update_traces(line=dict(color='green'))  
    fig.update_layout(
        title={'text': 'Número de Registros por Año', 'x': 0.5}, 
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        xaxis=dict(title=''),  # Elimina el título del eje X
        yaxis=dict(title='')  # Elimina el título del eje Y
    )
    return fig


# grafica de indicadores
def plot_indicators_chart(data):
    # Determina el valor máximo para la escala del gauge
    max_value = max(count for _, count in data)
    # Define las propiedades del texto para los títulos de los gauges
    title_font = dict(family='Arial', size=10, color='black')
    # Define las propiedades del texto para los números en los gauges
    number_font = dict(family='Arial', size=40, color='darkblue')
    # Configuración de la figura con espacio adicional
    fig_height_per_gauge = 200  # Altura por gauge, ajusta según sea necesario
    total_gauges = 3  # Número total de gauges
    fig = go.Figure()
    # Añade un gauge para cada institución en 'data'
    for index, (institution, count) in enumerate(data):
        fig.add_trace(go.Indicator(
            mode='gauge+number',
            value=count,
            title={'text': institution, 'font': title_font},
            number={'font': number_font},
            domain={'row': index, 'column': 0},
            gauge=dict(
                axis=dict(range=[0, max_value], tickwidth=2, tickcolor='darkblue'),
                bar=dict(color='darkblue'),
                steps=[
                    dict(range=[0, max_value/3], color='lightgreen'),
                    dict(range=[max_value/3, 2*max_value/3], color='green'),
                    dict(range=[2*max_value/3, max_value], color='darkgreen'),
                ],
            )
        ))

    fig.update_layout(
        grid=dict(rows=total_gauges, columns=1, pattern='independent'),
        title=dict(text='Top 3 Empresas', x=0.5, y=0.95, font=dict(size=14)),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=70, b=10),
        height=fig_height_per_gauge * total_gauges
    )
    return fig

# grafica de mapa
def plot_map_chart(data):
    # Extrae las coordenadas geográficas y calcula el centro del mapa
    latitudes = [item[0] for item in data]
    longitudes = [item[1] for item in data]
    center_lat = sum(latitudes) / len(latitudes)
    center_lon = sum(longitudes) / len(longitudes)

    # Calcula el rango de visualización para centrarse en el punto de interés
    zoom_factor = 20  # Este factor determina cuánto se "acercará" el mapa. Disminuye el valor para acercar más.
    lat_range = [center_lat - zoom_factor, center_lat + zoom_factor]
    lon_range = [center_lon - zoom_factor, center_lon + zoom_factor]

    # Crea el mapa usando Plotly Express
    fig = px.scatter_geo(
        lat=latitudes,
        lon=longitudes,
        title='Distribución Geográfica de las Observaciones'
    )

    # Configura el layout del mapa para ajustar el nivel de zoom
    fig.update_layout(
        geo=dict(
            showland=True,
            landcolor="rgb(217, 217, 217)",
            countrycolor="rgb(204, 204, 204)",
            showcountries=True,
            showocean=True,
            oceancolor="rgb(179, 205, 227)",
            projection=dict(
                type="equirectangular"
            ),
            center=dict(
                lat=center_lat, 
                lon=center_lon
            ),
            lataxis_range=lat_range,  # Ajusta el rango de latitud para acercar el mapa
            lonaxis_range=lon_range,  # Ajusta el rango de longitud para acercar el mapa
        ),
        margin=dict(l=0, r=0, t=50, b=0)
    )

    return fig