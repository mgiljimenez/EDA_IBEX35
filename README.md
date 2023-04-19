# EDA Recuperación de los valores del IBEX35 tras el COVID

Este proyecto consiste en un **EDA** (Exploratory data analysis) acerca de distorsión de los valores del IBEX35 durante el COVID y su posterior desarollo.

El análisis se realiza como proyecto que forma parte del **Bootcamp de Data Science** desarrollado en The Bridge.

## Autor ✒️

* **Miguel Gil Jimenez** 
- [LinkedIn](https://www.linkedin.com/in/miguel-gil-jimenez)
- [GitHub](https://github.com/mgiljimenez)

## Análisis realizados ⌨️
Fuente de datos oficial usada para la realización del EDA

- [Yahoo! Finance](https://es.finance.yahoo.com/)
Para acceder a los datos de la web se ha hecho uso de la API [yfinance](https://pypi.org/project/yfinance/).

## Análisis realizados ⌨️

En esta sección se explican los diferentes análisis llevados a cabo con el fin de comprobar o desmentir la hipótesis inicial del proyecto.

| Análisis | Objetivo |
|----------|----------|
| Evolución general del IBEX35 desde 2018 hasta 2023    | Identificación de anomalías producidas por el COVID   |
| Descenso por valor en la anomalía identificada    | Identificación de los valores con mayor pérdida   |
| Agrupación de los valores en descenso por sector de la empresa    | Identificación de los sectores más afectados por el COVID   |
| Distribución de la pérdida de valores en % según el sector    | Identificación de los sectores más afectados por el COVID   |
| Búsqueda de anomalías a partir del periodo de recuperación    | Identificación de anomalías mediante Precio de apertura y Volumen   |


## Archivos 📦

| Archivo | Especificaciones |
|----------|----------|
| main.ipynb    | Jupyter Notebook con el desarollo principal del EDA   |
| presentacion.pptx    | Powerpoint para la exposición de datos finales   |
| streamlit_file.py    | Streamlit para la visualización de resultados   |
| README.md    | Especificaciones y resumen del proyecto   |
| requirements.txt    | Librerías y versiones usadas   |

_Este comando te permitirá abrir la página desarrollada en streamlit:_
```
streamlit run streamlit_file.py
```

