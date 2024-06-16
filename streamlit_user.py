import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Arca Continental Digital Nest",
    page_icon="binoculars-fill",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Clientes", "Tendencias", "Mapa", "Cerrar Sesión"],
        icons=["file-person-fill", "person-circle", "graph-up", "pin-map-fill", "box-arrow-in-right"],
        menu_icon="heart-eyes-fill",
        default_index=0,
    )

welcome_text = """
<div style="font-size:25px; margin-top: 25px; " >
    Bienvenido a la plataforma de Arca Continental Digital Nest. Aquí podrás encontrar información relevante y detallada sobre los clientes, tendencias en cuanto al volumen de ventas de cada producto, y mucho más.
</div>

<div style="font-size:35px; margin-top: 50px;">
    <b>Resumen general:</b>
</div>
"""

if selected == "Home":
    st.title("Arca Continental Digital Nest - ToolKit")
    st.markdown(welcome_text, unsafe_allow_html=True)

elif selected == "Clientes":
    st.title("Clientes")
    st.write("Estos son los datos de cada uno de los clientes que hay disponibles en la base de datos.")

elif selected == "Tendencias":
    st.title("Contact")
    st.write("Contact us at")

elif selected == "Mapa":
    st.title("Mapa")
    st.write("Aquí podrás encontrar un mapa interactivo con la ubicación de cada uno de los clientes.")


elif selected == "Cerrar Sesión":
    st.title("Cerrar Sesión")
    st.write("Hasta luego!")


# Run the app with:
# streamlit run streamlit_user.py
