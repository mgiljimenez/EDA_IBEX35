#Importamos las librerias necesarias
from configuration.invest_config import invest
from configuration.creacion_graficos import graficos
from configuration.datos_extraidos import valores, valores_name, dic_valores
import pandas as pd
import plotly as py
import plotly.graph_objs as go
import streamlit as st


#Inicializamos streamlit

st.set_page_config(page_title="EDA IBEX35", page_icon="💰")

st.sidebar.title("EDA IBEX 35")
st.sidebar.image("img\imagen2.jpg")
menu=st.sidebar.selectbox("Menú", ["Inicio","Valores", "Análisis"])

if menu == "Inicio":
    st.title("Inicio")
    st.image("img\imagen6.jpg")
    st.markdown("""Este trabajo consiste en un **EDA** *(Exploratory Data Analysis)* desarrollado por **Miguel Gil Jimenez** durante el **Bootcamp de Data Science** en The Bridge.
                Nos centramos en analizar los valores del IBEX35 para comprobar si han recuperado su actividad normal tras la influecia que tuvo el COVID en los mercados.
                Para ello se extraen los datos de la API yfinance.""")
    st.info("Datos del creador")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/miguel-gil-jimenez)")
    st.markdown("- [GitHub](https://github.com/mgiljimenez)")
                    
    st.info("Especificaciones del EDA")
    st.markdown("""
| | |
|-|-|
| Hipótesis | Los valores del IBEX35 han recuperado su normalidad pre-Covid |
| Fuente de Datos | [Api yfinance](https://pypi.org/project/yfinance/) |
| Repositorio del proyecto | [Repositorio](https://github.com/mgiljimenez/EDA_IBEX35) |
| README | [Acceder al README](https://pypi.org/project/yfinance/) |
| Memoria del trabajo | [Acceder a la memoria del trabajo](https://github.com/mgiljimenez/EDA_IBEX35) |
""")


if menu == "Valores":
    filtro_valor = st.sidebar.selectbox("Seleccione el valor", valores_name)
    tipo_grafico=st.sidebar.radio("Seleccione tipo de gráfico:",options=["Detallado","Resumen"])
    if tipo_grafico=="Detallado":
        st.plotly_chart(graficos.grafico_valor(filtro_valor))
    elif tipo_grafico=="Resumen":
        st.plotly_chart(graficos.grafico_valor_resumen(filtro_valor))

if menu =="Análisis":
    st.write("Hola")