import yfinance as yf
import datetime
import pandas as pd
import os


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

#Definimos la clase que estructura los datos extraidos
class datos_extraidos:
    def __init__():
        pass
    def datos_extraidos():
        #Asignamos CSV a los índices del IBEX35
        ACS= pd.read_csv('data_ibex35/ACS.MC.csv')
        ACX= pd.read_csv('data_ibex35/ACX.MC.csv')
        AENA= pd.read_csv('data_ibex35/AENA.MC.csv')
        AMS= pd.read_csv('data_ibex35/AMS.MC.csv')
        ANA= pd.read_csv('data_ibex35/ANA.MC.csv')
        ANE= pd.read_csv('data_ibex35/ANE.MC.csv')
        BBVA= pd.read_csv('data_ibex35/BBVA.MC.csv')
        BKT= pd.read_csv('data_ibex35/BKT.MC.csv')
        CABK= pd.read_csv('data_ibex35/CABK.MC.csv')
        CLNX= pd.read_csv('data_ibex35/CLNX.MC.csv')
        COL= pd.read_csv('data_ibex35/COL.MC.csv')
        ELE= pd.read_csv('data_ibex35/ELE.MC.csv')
        ENG= pd.read_csv('data_ibex35/ENG.MC.csv')
        FDR= pd.read_csv('data_ibex35/FDR.MC.csv')
        FER= pd.read_csv('data_ibex35/FER.MC.csv')
        GRF= pd.read_csv('data_ibex35/GRF.MC.csv')
        IAG= pd.read_csv('data_ibex35/IAG.MC.csv')
        IBE= pd.read_csv('data_ibex35/IBE.MC.csv')
        ITX= pd.read_csv('data_ibex35/ITX.MC.csv')
        LOG= pd.read_csv('data_ibex35/LOG.MC.csv')
        MAP= pd.read_csv('data_ibex35/MAP.MC.csv')
        MEL= pd.read_csv('data_ibex35/MEL.MC.csv')
        MTS= pd.read_csv('data_ibex35/MTS.MC.csv')
        NTGY= pd.read_csv('data_ibex35/NTGY.MC.csv')
        RED= pd.read_csv('data_ibex35/RED.MC.csv')
        SAB= pd.read_csv('data_ibex35/SAB.MC.csv')
        SAN= pd.read_csv('data_ibex35/SAN.MC.csv')
        TEF= pd.read_csv('data_ibex35/TEF.MC.csv')
        UNI= pd.read_csv('data_ibex35/UNI.MC.csv')

        #Agrupación de variables
        valores=[ACS,ACX,AENA,AMS,ANA,ANE,BBVA,BKT,CABK,CLNX,COL,
                ELE,ENG,FDR,FER,GRF,IAG,IBE,ITX,
                LOG,MAP,MEL,MTS,NTGY,RED,SAB,SAN,TEF,UNI]
        valores_name=["ACS","ACX","AENA","AMS","ANA","ANE","BBVA","BKT","CABK","CLNX","COL",
                "ELE","ENG","FDR","FER","GRF","IAG","IBE","ITX",
                "LOG","MAP","MEL","MTS","NTGY","RED","SAB","SAN","TEF","UNI"]
        dic_valores = {nombre: valor for nombre, valor in zip(valores_name, valores)}

        return(valores, valores_name, dic_valores)




