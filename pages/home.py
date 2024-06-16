import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Texto de bienvenida

# Función para cargar datos (con caché para mejorar el rendimiento)
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

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

    st.subheader("Surtido inteligente")
    st.write("Aquí podrás encontrar un resumen general de los datos de los clientes, tendencias y ubicaciones en un solo lugar.")
    st.subheader("Clientes")
    st.write("Los 10 clientes con mayores ventas son:")

    if st.button('Ver clientes'):
        df = load_data('C:/Users/rprie/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\Desktop\Hack-ArcaContinental/data/sales_clean.csv')

        # Top 10 clientes con mayores ventas
        top_customers = df.groupby('customer_id')['amount'].sum().nlargest(10)
            
            # Gráfico de barras de los 10 clientes con mayores ventas
        fig, ax = plt.subplots()
        top_customers.plot(kind='bar', ax=ax)
        ax.set_ylabel('Monto')
        ax.set_title('Top 10 clientes con mayores ventas')
            # Cambiar nombre de las etiquetas del eje x por cliente 1, cliente 2, etc.
        ax.set_xticklabels(['Clte ' + str(i) for i in range(1, 11)])

            # Cambiar el tamaño del gráfico
        plt.tight_layout()

# Grafica tendencia de los clientes que mejoraron sus ventas
        
        # Mostrar gráfico en Streamlit
        st.pyplot(fig)

    st.subheader("Tendencias")
    st.write("Los clientes que mejoraron sus ventas son:")

    if st.button('Ver tendencias'):
        df = load_data('C:/Users/rprie/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\Desktop\Hack-ArcaContinental/data/sales_clean.csv')
        df.groupby('customer_id')['amount'].sum().plot(kind='line')
        plt.title('Tendencia de los clientes que mejoraron sus ventas')
        plt.xlabel('Cliente')
        plt.ylabel('Monto')
        plt.grid()
        st.pyplot()
   

        




        st.markdown(welcome_text, unsafe_allow_html=True)

