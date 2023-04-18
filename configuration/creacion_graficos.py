import plotly.graph_objs as go
from datos_extraidos import dic_valores

class graficos:
    #Funcion imprimir graficos valores
    def grafico_valor(valor_input):

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
        return(fig)

    def grafico_valor_resumen(valor_input):
        trace1 = go.Scatter(
                            x = dic_valores[valor_input]['Date'],
                            y = dic_valores[valor_input]['Open'],
                            name = 'citations',
                            mode= 'lines',
                            marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                            )

        data = [trace1]

        layout = dict(title = dict(text=f'PRECIO DE APERTURA {valor_input}', x=0.5),
                    xaxis= dict(title= 'FECHA',ticklen= 5),
                    yaxis= dict(title= 'VALOR DE APERTURA (€)',ticklen= 5)
                )

        fig = go.Figure(data = data, layout=layout)

        return(fig)