# Importar las bibliotecas necesarias
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear una figura con Plotly Express
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Iniciar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Hello Dash', className='title'),
    html.Div(children='''Dash: A web application framework for Python.''', className='description'),
    dcc.Graph(
        figure=fig
    )
], className='container')

# Correr el servido
if __name__ == '__main__':
    app.run_server(debug=True)
