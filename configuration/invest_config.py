import yfinance as yf
import datetime


#Definimos clase invest,mediante la que se extraen los datos de yfinance
class invest:
    def __init__(self, symbol, start_date, end_date, frequency):
        """
            -symbol="AMZN"
            -start_date="2020-01-01"
            -end_date = "2023-02-05"
            -frequency=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        """

        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency
    
    def resultados(self):
        '''
        Devuelve un Dataframe con todos los datos
            -Input: None
            -Output: Resultados
        '''
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date, interval=self.frequency)
        return data

    def to_csv(self, nombre_csv):
        '''
        Crea un CSV con todos los datos.
            -Input: nombre_csv.csv
            -Output: Creación de un CSV con todos los datos
        '''
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date, interval=self.frequency)
        data.to_csv(nombre_csv, header=True, index=True)
        print(f"Archivo guardado en: {nombre_csv}")




