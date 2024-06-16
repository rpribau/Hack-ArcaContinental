import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)


def show():
    st.title("Tendencias")
    st.write("Aquí podrás encontrar tendencias en el volumen de ventas.")

    if st.button('Ver Ventas'):
        df = load_data('C:/Users/rprie/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\Desktop\Hack-ArcaContinental/data/sales_clean.csv')



       