import streamlit as st

def show():
    st.title("Arca Continental Digital Nest - ToolKit")
    welcome_text = """
    <div style="font-size:25px; margin-top: 25px;">
        Bienvenido a la plataforma de Arca Continental Digital Nest. Aquí podrás encontrar información relevante y detallada sobre los clientes, tendencias en cuanto al volumen de ventas de cada producto, y mucho más.
    </div>

    <div style="font-size:35px; margin-top: 50px;">
        <b>Resumen general:</b>
    </div>
    """
    st.markdown(welcome_text, unsafe_allow_html=True)
