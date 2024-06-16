import streamlit as st
from streamlit_option_menu import option_menu

st.set_option("client.showSidebarNavigation", False)

# Configuración de la página
st.set_page_config(
    page_title="Arca Continental Digital Nest",
    page_icon="binoculars-fill",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Definir la barra lateral
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Clientes", "Tendencias", "Mapa", "Cerrar Sesión"],
        icons=["house", "people", "graph-up", "map", "box-arrow-right"],
        menu_icon="cast",
        default_index=0,
    )

# Cargar la página correspondiente
if selected == "Home":
    import pages.home as home
    home.show()
elif selected == "Clientes":
    import pages.clientes as clientes
    clientes.show()
elif selected == "Tendencias":
    import pages.tendencias as tendencias
    tendencias.show()
elif selected == "Mapa":
    import pages.mapa as mapa
    mapa.show()
elif selected == "Cerrar Sesión":
    import pages.cerrar_sesion as cerrar_sesion
    cerrar_sesion.show()
