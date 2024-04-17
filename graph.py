import plotly.express as px
import plotly.graph_objects as go

# Gráfico de barras
def plot_bar_chart(data):
    departamentos = [item[0] for item in data]
    cantidades = [item[1] for item in data]
    fig = px.bar(
        x=departamentos,
        y=cantidades,
        labels={'x': 'Departamentos', 'y': 'Cantidad de Aves'},
        color_discrete_sequence=["steelblue"]*len(departamentos)  # Asigna el color fijo

    )
    fig.update_layout(
        margin=dict(l=40, r=40, t=40, b=40), # Estos valores puedes ajustarlos según tus preferencias
        paper_bgcolor='rgba(0,0,0,0)', # Hace el color de fondo del "papel" transparente
        yaxis=dict(gridcolor='white'),
        title={
            'text': 'Cantidad de Aves por Departamento',
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    return fig

# Gráfico de torta
def plot_pie_chart(data):
    departamentos = [item[0] for item in data]
    cantidades = [item[1] for item in data]
    fig = go.Figure(data=[
        go.Pie(labels=departamentos, values=cantidades, hole=.4, marker=dict(colors=px.colors.sequential.Blues[::-1]))
    ])
    fig.update_layout(
        margin=dict(l=40, r=40, t=40, b=40), # Estos valores puedes ajustarlos según tus preferencias
        plot_bgcolor='white',
        title={'text': 'Proporción de especies de aves por departamento', 'x': 0.5, 'y': 0.95},
        paper_bgcolor='rgba(0,0,0,0)', # Hace el color de fondo del "papel" transparente
)
    return fig

# Gráfico de burbujas
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
    )
    fig.update_layout(
        title={'text':'Especies Únicas y Observaciones Totales por Departamento','x': 0.5},
        paper_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(visible=False, showticklabels=False)
    return fig