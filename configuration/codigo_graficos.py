import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import iplot



def grafico_valor(valor_input, dic_valores):
    #FUNCION QUE DEVUELVE EL GRAFICO COMPLETO PARA CADA VALOR
    layout = dict(
        title = dict(text=valor_input, x=0.5),
        xaxis=dict(
            title='Fecha'
        ),
        yaxis=dict(
            title='Valor (€)'
        )
    )
    fig = go.Figure(data=[go.Candlestick(x=dic_valores[valor_input]['Date'],
                    open=dic_valores[valor_input]['Open'],
                    high=dic_valores[valor_input]['High'],
                    low=dic_valores[valor_input]['Low'],
                    close=dic_valores[valor_input]['Close'])],layout=layout
                    )
    return(fig)#Le he quitado iplot(fig)

def grafico_valor_resumido(valor_input, dic_valores):
    #FUNCION QUE DEVUELVE EL GRAFICO COMPLETO PARA CADA VALOR
    trace1 = go.Scatter(x=dic_valores[valor_input]["Date"],
                     y=dic_valores[valor_input]["Open"]
                    )
    data=[trace1]
    layout = dict(
        title = dict(text="Precio de apertura"+" "+ valor_input, x=0.4),
        xaxis=dict(
            title='Fecha'
        ),
        yaxis=dict(
            title='Valor (€)'
        )
    )
    fig=go.Figure(data=data, layout=layout)
    return(fig)#Le he quitado iplot(fig)


def grafico_suma_ibex35(df_media_IBEX35):
    #Función de devuelve un gráfico de las medias de aperturas de todos los valores de Ibex35
    trace1 = go.Scatter(
                        x = df_media_IBEX35['Date'],
                        y = df_media_IBEX35['Open'],
                        name = 'Precio de apertura total de los valores',
                        mode= 'lines',
                        line=dict(color='rgba(16, 112, 2, 0.8)', width=2),
                        )

    data = [trace1]

    layout = dict(title = dict(text='Precio de apertura total IBEX 35',
                            font=dict(size=24)),
                xaxis= dict(title= 'Fecha',ticklen= 5, tickfont=dict(size=16), 
                            showgrid=True, gridwidth=1, gridcolor='lightgrey',
                            zeroline=True, zerolinecolor='grey', zerolinewidth=1),
                yaxis= dict(title= 'Precio de apertura total (€)',ticklen= 5, tickfont=dict(size=16),
                            showgrid=True, gridwidth=1, gridcolor='lightgrey', 
                            range=[df_media_IBEX35['Open'].min()*0.95, df_media_IBEX35['Open'].max()*1.05],
                            zeroline=True, zerolinecolor='grey', zerolinewidth=1),
                plot_bgcolor='white',
                margin=dict(l=80, r=80, t=80, b=80),
                hovermode='x',
                legend=dict(x=0.02, y=1.1, orientation="h", bordercolor="black", borderwidth=1,
                            font=dict(size=16)),
                )

    fig = go.Figure(data = data, layout=layout)

    fig.update_layout(
        autosize=True,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(size=16)
    )

    return(fig)#Le he quitado iplot(fig)

def grafico_descenso_por_valor(df_descenso_empresa):
    # Devuelve un grafico de barras con el descenso del valor por empresa el el momento pico COVID
    # Crear gráfico de barras
    fig = px.bar(df_descenso_empresa, x=df_descenso_empresa["Empresa"], y='Valor')

    # Calcular la media de los valores de la columna 'Valor'
    mean_value = df_descenso_empresa['Valor'].mean()

    # Agregar una línea horizontal en y=35.61
    fig.add_shape(type="line",
                  x0=-0.5,
                  y0=35.61,
                  x1=len(df_descenso_empresa["Empresa"])-0.5,
                  y1=35.61,
                  line=dict(color="red", width=2))

    # Personalizar el diseño del gráfico
    fig.update_layout(title = dict(text='Descenso por valor en la caída pico de COVID',
                            font=dict(size=24)),
                      autosize=False,
                      paper_bgcolor='white',
                      plot_bgcolor='white', 
                      font=dict(size=16),
                      showlegend=True,
                      xaxis_title="Índice",
                      yaxis_title="Descenso 17/02/2020-16/03/2020 (%)")

    # Mostrar el gráfico
    return (fig)
def grafico_descenso_por_valor_categoria(df_descenso_empresa):
    # Crear gráfico de barras con colores por categoría
    fig = px.bar(df_descenso_empresa, x=df_descenso_empresa["Empresa"], y='Valor', color='categoria')

    fig.add_shape(type="line",
                  x0=-0.5,
                  y0=35.61,
                  x1=len(df_descenso_empresa["Empresa"])-0.5,
                  y1=35.61,
                  line=dict(color="red", width=2))

    # Personalizar el diseño del gráfico
    fig.update_layout(title=dict(text='Descenso por valor en la caída pico de COVID',
                            font=dict(size=24)),
                      autosize=False,
                      paper_bgcolor='white',
                      plot_bgcolor='white', 
                      font=dict(size=16),
                      showlegend=True,
                      xaxis_title="Índice",
                      yaxis_title="Descenso 17/02/2020-16/03/2020 (%)")

    # Mostrar el gráfico
    return(fig)#Le he quitado fig.show

def grafico_precio_apertura(valor, dic_valores):
  caida = dic_valores[valor][(dic_valores[valor].index > 110) & (dic_valores[valor].index < 116)]
  # MEDIA DEL PRECIO DE APERTURA DEL IBEX35
  trace1 = go.Scatter(
                      x = caida['Date'],
                      y = caida['Open'],
                      name = 'citations',
                      mode= 'lines',
                      marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                      )
  data = [trace1]

  layout = dict(title = dict(text=f'PRECIO DE APERTURA {valor}', x=0.5),
              xaxis= dict(title= 'FECHA',ticklen= 5),
              yaxis= dict(title= 'PRECIO DE APERTURA',ticklen= 5)
            )

  fig = go.Figure(data = data, layout=layout)

  return(fig)


