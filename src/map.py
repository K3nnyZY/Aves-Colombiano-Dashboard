import folium
from folium.plugins import FastMarkerCluster
import psycopg2
import json

# Establece la conexión con la base de datos
conn = psycopg2.connect(
    host="localhost",
    user="aves",
    password="aves12345",
    database="aves-colombia-db",
    port=5433
)
cursor = conn.cursor()

# Ejecuta el query para obtener las coordenadas geográficas y los nombres de las especies
cursor.execute("""
SELECT decimalLatitude, decimalLongitude, species
FROM aves
WHERE decimalLatitude IS NOT NULL AND decimalLongitude IS NOT NULL;
""")
datos = cursor.fetchall()

# Cierra la conexión con la base de datos
cursor.close()
conn.close()

# Leer los datos geográficos desde un archivo JSON para Colombia
with open("colombia.json", "r") as file:
    data_colombia = json.load(file)

# Extraer latitudes, longitudes y especies de los datos
latitudes = [item[0] for item in datos]
longitudes = [item[1] for item in datos]
species = [item[2] for item in datos]

# Crear un mapa centrado en una ubicación inicial en Colombia
mapa = folium.Map(location=[9.60971, -75.08175], zoom_start=7) 

# Opcionalmente, añadir un choropleth
choropleth = folium.Choropleth(
    geo_data=data_colombia,
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
).add_to(mapa)


icon_create_function = '''
function(cluster) {
    return L.divIcon({
        html: '<div style="background-color: rgba(50, 205, 50, 0.8); border-radius: 50%; color: white; display: flex; justify-content: center; align-items: center; width: 40px; height: 40px;">' + cluster.getChildCount() + '</div>',
        className: "marker-cluster-custom",
        iconSize: L.point(40, 40, true)
    });
}
'''

marker_cluster = FastMarkerCluster(
    list(zip(latitudes, longitudes)),
    icon_create_function=icon_create_function
).add_to(mapa)

# Guardar el mapa como archivo HTML
mapa.save('mapa.html') 
