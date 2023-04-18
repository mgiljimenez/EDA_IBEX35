import pandas as pd
from invest_config import invest
import os

#Leemos cuales son los índices actuales del IBEX35 y sacamos sus códigos
ibex35=pd.read_csv("configuration/codigos_ibex35.csv")
codigos_ibex35=ibex35["codigo"]

#Creación de un CSV para cada valor del ibex35 entre 2018-01-01 y 2023-04-17 con frecuencia semanal
#Guardados en data_ibex35
for codigo in codigos_ibex35:
    data=invest(codigo,"2018-01-01","2023-04-17","1wk")
    df_data=data.resultados()
    ruta="data_ibex35/"+codigo+".csv"
    df_data.to_csv(ruta)

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

