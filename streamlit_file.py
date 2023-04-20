#Importamos las librerias necesarias
from configuration.invest_config import invest, datos_extraidos
from configuration.codigo_graficos import grafico_valor,grafico_suma_ibex35, grafico_descenso_por_valor, grafico_descenso_por_valor_categoria, grafico_valor_resumido
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

#Calculo media ibex35 para grafico posterior
#Sacamos la suma de evolución de todos los valores del IBEX35
#Extramos precios de apertura
dict_open={}
n=1
for i in valores:
    dict_open[n]=i["Open"]
    n+=1
df_suma_total=pd.DataFrame(dict_open).sum(axis=1)
df_suma_IBEX35=pd.concat([dic_valores["BBVA"]["Date"], df_suma_total], axis=1)
df_suma_IBEX35=df_suma_IBEX35.rename(columns={0:"Open"})

#Inicializamos streamlit

st.set_page_config(page_title="EDA IBEX35", page_icon="💰")

st.sidebar.title("EDA IBEX 35")
menu=st.sidebar.selectbox("Menú", ["Inicio","Valores", "Análisis época confinamiento", "Análisis hasta actualidad","Conclusión"])

if menu == "Inicio":
    st.sidebar.image("img/foto_bar.jpg")
    st.title("Inicio")
    st.markdown("""Este trabajo consiste en un **EDA** *(Exploratory Data Analysis)* desarrollado por **Miguel Gil Jimenez** durante el **Bootcamp de Data Science** en The Bridge.
                Nos centramos en analizar los valores del IBEX35 para comprobar si han recuperado su actividad normal tras la influecia que tuvo el COVID en los mercados.
                Para ello se extraen los datos de la API yfinance.""")
    st.image("img/img_prin.jpg")
    st.info("Datos del creador")
    st.markdown("- Miguel Gil Jimenez")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/miguel-gil-jimenez)")
    st.markdown("- [GitHub](https://github.com/mgiljimenez)")

    st.info("Objetivo")
    st.write("En este estudio se pretende investigar la influencia que ha tenido el COVID en el IBEX35 tanto de una forma general como en cada uno de los valores. Para ello estudiaremos detalladamente el impacto que tuvo el confinamiento en la bolsa y cómo fue su posterior desarrollo hasta la actualidad.")
    st.info("Hipótesis")
    st.write("Es cierto que la pandemia produjo un gran descenso de los valores de mercado, sin embargo, no es el primer acontecimiento histórico que produce este tipo de fenómeno y se ha demostrado que a largo plazo se acaban recuperando los niveles precios al acontecimiento. Por lo tanto, ¿han recuperado ya los valores su situación Pre-Covid? Consideramos que sí, que ya se ha recuperado la normalidad o se está alcanzando en la actualidad, sin embargo procedemos a demostrar esta hipótesis mediante este EDA.")
    st.info("Fuente de Datos")
    st.markdown("La fuente de datos usada para realizar este análisis es la de [Yahoo Finance](https://es.finance.yahoo.com/). Para acceder a estos datos se ha hecho uso de la API [yfinance](https://pypi.org/project/yfinance/).")
    st.info("Resumen Datos EDA")
    st.markdown("""
| | |
|-|-|
| Hipótesis | Los valores del IBEX35 han recuperado su normalidad pre-Covid |
| Fuente de Datos | [Api yfinance](https://pypi.org/project/yfinance/) |
| Repositorio del proyecto | [Repositorio](https://github.com/mgiljimenez/EDA_IBEX35) |
| README | [Acceder al README](https://github.com/mgiljimenez/EDA_IBEX35/blob/main/README.md) |
| Memoria del trabajo | [Acceder a la memoria del trabajo](https://github.com/mgiljimenez/EDA_IBEX35) |
""")



elif menu == "Valores":
    st.sidebar.image("img/foto_bar.jpg")
    st.info("FILTRE EL VALOR Y TIPO DE GRÁFICO A MOSTRAR")
    filtro_valor = st.sidebar.selectbox("Seleccione el valor", valores_name)
    tipo_grafico=st.sidebar.radio("Seleccione tipo de gráfico:",options=["Detallado","Resumen"])
    if tipo_grafico=="Detallado":
        st.plotly_chart(grafico_valor(filtro_valor, dic_valores))
    elif tipo_grafico=="Resumen":
        st.plotly_chart(grafico_valor_resumido(filtro_valor, dic_valores))

elif menu =="Análisis época confinamiento":
    st.sidebar.image("img/foto_bar.jpg")
    st.plotly_chart(grafico_suma_ibex35(df_suma_IBEX35,))
    st.write("""Al observar esta gráfica de la evolución de la suma de los precios de apertura de los valores del IBEX35 desde 2018 hasta 2023 podemos observar que en 2020 se produce una drástica caída del precio. Tal y como podíamos imaginar, esto es consecuencia del COVID, ya que el máximo del valor en 2020 se alcanza el 17/02/2020, coincidiendo 2 días antes la declaración de confinamiento en España. 
El valor mínimo lo llega a alcanzar el 16/03/2020, cuando los valores parecen empezar a recuperarse hasta días de hoy. Esta caída de 1 mes supuso un decrecimiento del valor de precio de apertura del IBEX35 del -35,61%.
Si nos centramos en esta franja de fechas donde se produce la “caída pico” del IBEX35 provocada por el COVID podemos observar en qué porcentaje se reduce el precio de cada acción. Se cumple que en este mes, todos los valores disminuyen su precio, sin haber ninguno que aumente su valor. Se calcula en porcentaje, ya que al tener cada valor un precio considerablemente diferente las reducciones no serían proporcionales y por tanto no las podríamos comparar.
En el siguiente gráfico podemos observar esta caída por acción y la media de todas ellas. (-35,61%)
""")
    dif_valores_pico={}
    for valor in dic_valores:
        try:
            max_value=float(dic_valores[valor]["Open"][dic_valores[valor].index==111].head(1))
            min_value=float(dic_valores[valor]["Open"][dic_valores[valor].index==115].head(1))
            dif=100-(min_value*100/max_value)
            dif_valores_pico[valor]=dif
        except:
            pass
    df_descenso_empresa = pd.DataFrame(dif_valores_pico.items(), columns=['Empresa', 'Valor'])
    st.plotly_chart(grafico_descenso_por_valor(df_descenso_empresa))
    st.write("""Observando este gráfico llegamos a la conclusión de que hay un grupo de empresas cuyos valores disminuyen mucho menos que la media en la “caída pico” del COVID, mientras otras superan considerablemente la media como por ejemplo IAG con un 70,8% de pérdida.
Para intentar llegar a una conclusión de por qué cada una se comporta de esa forma, agrupamos cada uno de los valores según el sector al que se dedica.
""")
    #Diccionario clasificacion valores por sector
    sectores={"Banca":["BBVA","BKT","CABK","SAN","SAB", "UNI"],
            "Software":["CLNX","TEF","AMS","LOG"],
            "Energia":["IBE","NTGY","RED","ENG","ELE","ANE","ANA"],
            "Movilidad":["AENA","IAG","FER"],
            "Industrial":["MTS","ACX","ACS"],
            "Otros":["MAP","MEL","ITX","GRF","FDR","COL"],
            }
    sectores_invertido = {valor: clave for clave, valores in sectores.items() for valor in valores}
    lista_categoria=[]
    for empresa in df_descenso_empresa["Empresa"]:
        lista_categoria.append(sectores_invertido[empresa])
    df_descenso_empresa["categoria"]=lista_categoria
    st.plotly_chart(grafico_descenso_por_valor_categoria(df_descenso_empresa))
    st.write("""Al observar el gráfico superior podemos concluir que el sector de la energía es el que menos sufre esta caída. En la categoría “Otros” se han agrupado el resto de empresas que no pertenecen a un sector de gran peso en el IBEX 35, no obstante es importante comentar que el valor “GRF”, el cual sufre una caída de tan solo 24,67% se dedica al sector farmacéutico y hospitalario. Esta puede ser la explicación, debido a la demanda de productos y servicios sanitarios durante la pandemia.
Observamos de nuevo que “IAG” es el valor que más disminuye durante esta caída, ya que pertenece al sector la movilidad, en concreto de la aviación, que se vio completamente paralizada por culpa del confinamiento mundial a causa del COVID.
""")
    
    descenso_IBEX_35_pico=745.290393-479.870191
    descenso_por_valor_pico={}

    for valor in dic_valores:
        try:
            descenso_por_valor_pico[valor]=100-(dic_valores[valor]["Open"][115]*100)/dic_valores[valor]["Open"][111]
        except:
            pass

    df_descenso_porcentaje = pd.DataFrame(descenso_por_valor_pico.items(), columns=['Empresa', 'Valor'])

    ls_categoria=[]
    for empresa in df_descenso_porcentaje["Empresa"]:
        ls_categoria.append(sectores_invertido[empresa])

    df_descenso_porcentaje["Categoria"]=ls_categoria
    df_descenso_categoria=df_descenso_porcentaje.groupby("Categoria").mean()
    ls_porcentaje_descenso_categoria=[]
    valor_total_descenso=sum(df_descenso_categoria["Valor"])
    for valor in df_descenso_categoria["Valor"]:
        ls_porcentaje_descenso_categoria.append(valor*100/valor_total_descenso)
    df_descenso_categoria["descenso_porcentual"]=ls_porcentaje_descenso_categoria
    # Crear el gráfico circular con Plotly
    fig = go.Figure(data=[go.Pie(labels=df_descenso_categoria.index, values=df_descenso_categoria['descenso_porcentual'])])

    fig.update_layout(
        title={
            'text': "Distribución del descenso por sector",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        width=600,
        height=500,
    )
    # Mostrar el gráfico
    st.plotly_chart(fig)
    st.write("""En este gráfico se representan los sectores que más influyeron en la caída del IBEX35, categorizando por sector y dándole el mismo peso a todos, debido a que el sector de la Banca es el que más empresas tiene y por tanto el que más influye en proporción en los cambios totales del IBEX35. De este modo vemos de nuevo que la Movilidad es el sector más castigado, es decir, el que devolvería un peor resultado en caso de inversión, debido a las reducciones de movilidad al principio de la pandemia. 
Por otro lado, los sectores del Software y la Energía fueron los más beneficiados en esta franja de tiempo, reduciéndose sus valores tan solo un 14,5% y 13% respectivamente.
""")
elif menu=="Análisis hasta actualidad":
    st.sidebar.image("img/foto_bar.jpg")
    trazos_empresas = []
    for nombre, datos in dic_valores.items():
        trazo = go.Scatter(
            x=datos['Date'],
            y=datos['Volume'],
            name=nombre,
            line=dict(width=2),
            hovertemplate='%{y:.2f} unidades<br>%{x|%d-%m-%Y}<extra></extra>'
        )
        trazos_empresas.append(trazo)
    layout = go.Layout(
        title=dict(text="EVOLUCIÓN DEL VOLUMEN", x=0.5),
        xaxis=dict(title='Fecha'),
        yaxis=dict(title='Volumen'),
        legend=dict(orientation='h', y=1.05)
    )
    fig = go.Figure(data=trazos_empresas, layout=layout)
    st.plotly_chart(fig)
    st.write("""En este gráfico podemos observar la evolución del volumen de los valores desde 2018 hasta 2023. Todos los valores siguen una distribución aproximadamente cíclica y bastante estable, sin embargo, al observar la evolución del volumen de “IAG”, podemos comprobar que se produce un cambio drástico en su tendencia que coincide con el inicio del confinamiento en España. """)
    indice_volumen=st.selectbox("Seleccione el valor para mostrar sus datos", valores_name)

    caida_minimo=100-(dic_valores[indice_volumen]["Open"][115]*100/dic_valores[indice_volumen]["Open"][111])
    caida_actual=100-(dic_valores[indice_volumen]["Open"][275]*100/dic_valores[indice_volumen]["Open"][111])
    caida_minimo=round(caida_minimo*(-1),2)
    caida_actual=round(caida_actual*(-1),2)
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Variación en la caída pico", value=str(caida_minimo)+"%")
    with col2:
        st.metric(label="Variación inicio caida-actual", value=str(caida_actual)+"%")


    def grafico_evolucion_volumen(valor, dic_valores):
        #Gráfico de evolución del volumen
        caida = dic_valores[valor]
        # MEDIA DEL PRECIO DE APERTURA DEL IBEX35
        trace1 = go.Scatter(
                            x = caida['Date'],
                            y = caida['Volume'],
                            name = 'citations',
                            mode= 'lines',
                            marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                            )

        data = [trace1]

        layout = dict(title = dict(text=f'VOLUMEN {valor}', x=0.5),
                    xaxis= dict(title= 'FECHA',ticklen= 5),
                    yaxis= dict(title= 'VOLUMEN',ticklen= 5)
                    )

        fig = go.Figure(data = data, layout=layout)
        return(fig)
    st.plotly_chart(grafico_evolucion_volumen(indice_volumen, dic_valores))
    st.plotly_chart(grafico_valor(indice_volumen, dic_valores))

        



elif menu =="Conclusión":
    st.sidebar.image("img/foto_bar.jpg")
    variacion_inicio_actual={}

    for empresa in dic_valores:
        try:
            caida_actual=100-(dic_valores[empresa]["Open"][275]*100/dic_valores[empresa]["Open"][111])
            caida_actual=round(caida_actual*(-1),2)
            variacion_inicio_actual[empresa]=caida_actual
        except:
            pass
    valores = list(variacion_inicio_actual.values())
    empresas = list(variacion_inicio_actual.keys())
    trace = go.Bar(x=empresas, y=valores)
    layout = go.Layout(title='Variación de cada valor (Actual respecto a Pre-Covid)')
    fig1 = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig1)
    labels = ['Superiores a Pre-Covid', 'Inferiores a Pre-Covid']
    values = [35.71, 64.29]
    trace = go.Pie(labels=labels, values=values)
    layout = go.Layout(title='Distribución de empresas según su valor actual respecto a su situación Pre-Covid')
    fig2 = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig2)

    st.write("""Podemos observar que tan solo un 35.7% ha recuperado sus niveles precovid, siendo el mayor beneficiado Acciona, empresa de energías renovables.
             """)
    st.write("""Como conclusión podemos decir que el descenso de la caída pico supuso un -35,61% pero desde el inicio de la caída hasta la actualidad se ha incrementado el precio un 0,64% lo que significa que el IBEX35 ya está recuperando su normalidad. Sin embargo al observar cada valor individualmente comprobarmos que existen mucha diferencias y no crecen en conjunto, sino que unas aumentan su valor considerablemente, mientras otras se han estancado.""")
