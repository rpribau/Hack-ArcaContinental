import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

def show():
    st.title("Clientes")
    st.write("Estos son los datos de cada uno de los clientes que hay disponibles en la base de datos.")
    st.write("Grafica de fidelidad de los clientes")

    if st.button('Ver fidelidad de los clientes'):
        df = load_data('C:/Users/rprie/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\Desktop\Hack-ArcaContinental/data/sales_clean.csv')

        # Grafica de fidelidad de los clientes
        fidelidad=df.groupby('customer_id')['year'].nunique().value_counts().plot(kind='bar')
        plt.title('Fidelidad de los clientes')
        plt.xlabel('Años')
        plt.ylabel('Clientes')
        plt.grid()
        st.pyplot()
    st.write("Esta visualizacion captura la fidelidad de los clientes a lo largo de los años.")
    


    