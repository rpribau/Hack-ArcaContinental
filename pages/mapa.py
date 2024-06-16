import streamlit as st
import folium
from streamlit_folium import folium_static
import numpy as np

def show():
    st.title('Mapa de Monterrey con Marcadores de Clientes')
    
    welcome_text = """

    <div style="font-size:25px; margin-top: 25px; margin-bottom: 20px">
        Bienvenido al mapa de clientes de Arca Continental Digital Nest. Aquí podrás visualizar la ubicación de los clientes activos e inactivos en el Area Metropolitana de Monterrey. 
    </div>
    
    <div style="font-size:28px; margin-top: 10px;">
        <b><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
        <path d="M8 16s7-4.5 7-11A7 7 0 0 0 8 0a7 7 0 0 0-7 5c0 6.5 7 11 7 11zm0-8a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
        </svg> Pin verde: Cliente Activo</b>
        </div>

    <div style="font-size:28px; margin-top: 10px;">
        <b><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
    <path d="M8 16s7-4.5 7-11A7 7 0 0 0 8 0a7 7 0 0 0-7 5c0 6.5 7 11 7 11zm0-8a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
    </svg> Pin rojo: Cliente Inactivo</b>
    </div>

    """

    st.markdown(welcome_text, unsafe_allow_html=True)
    
    # Crear un mapa centrado en Monterrey
    m = folium.Map(location=[25.6866, -100.3161], zoom_start=12)
    
    # Generar 10 ubicaciones aleatorias en Monterrey
    locations = generate_random_locations(10)
    
    # Colocar marcadores en las ubicaciones generadas
    for i, loc in enumerate(locations):
        if i < 3:
            # Primeros 3 marcadores en rojo
            color = 'red'
        else:
            # Los siguientes 7 marcadores en verde
            color = 'green'
        
        folium.Marker(location=loc, popup=f'Marcador {i+1}', icon=folium.Icon(color=color)).add_to(m)
    
    # Mostrar el mapa
    folium_static(m)

def generate_random_locations(num_locations):
    # Generar coordenadas aleatorias dentro de un rango aproximado de Monterrey
    latitudes = np.random.uniform(25.55, 25.85, size=num_locations)
    longitudes = np.random.uniform(-100.45, -100.05, size=num_locations)
    locations = list(zip(latitudes, longitudes))
    return locations

