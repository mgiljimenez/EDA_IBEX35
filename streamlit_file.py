#Importamos las librerias necesarias
from configuration.invest_config import invest, datos_extraidos
from configuration.codigo_graficos import grafico_valor,grafico_valor_resumido, grafico_media_ibex35, grafico_descenso_por_valor, grafico_descenso_por_valor_categoria
import numpy as np
import pandas as pd
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
import streamlit as st


carga_datos=datos_extraidos.datos_extraidos()
valores=carga_datos[0]
valores_name=carga_datos[1]
dic_valores=carga_datos[2]

#Inicializamos streamlit

st.set_page_config(page_title="EDA IBEX35", page_icon="💰")

st.sidebar.title("EDA IBEX 35")
menu=st.sidebar.selectbox("Menú", ["Inicio","Valores", "Análisis"])

if menu == "Inicio":
    st.title("Inicio")
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
        st.plotly_chart(grafico_valor(filtro_valor, dic_valores))
    elif tipo_grafico=="Resumen":
        st.plotly_chart(grafico_valor_resumido(filtro_valor, dic_valores))

if menu =="Análisis":
    st.write("Hola")