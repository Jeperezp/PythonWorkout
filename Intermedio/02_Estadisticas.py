"""
Especificación: Desarrolla un programa que lea un archivo CSV que contenga datos numéricos y calcule estadísticas básicas como la media, la mediana y la desviación estándar de cada columna. Luego, escribe los resultados en un archivo de texto.
Manejo de errores: Asegúrate de manejar posibles errores al abrir el archivo CSV o al calcular las estadísticas.
"""
import pandas as pd
import requests

url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"

def Connection_DatosAbiertos(start:str,end:str, url:str):
    """
    establishing a connection to Datos Abiertos

    parameters:

    start (str): start day of query 'yyyy-mm-dd'
    end (str): end day of query 'yyyy-mm-dd'
    url (str): URL of API

    Returns:
    DataFrame
    """
    
    all_data = []
    start = f"{start}T00:00:00"
    end = f"{end}T23:59:59"
    params = {
    "$limit": 1000000,
    "$offset": 0,
    "$where": f"fecha_reporte_web >= '{start}' and fecha_reporte_web <='{end}'"
    }
    while True:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Check for any errors in the response
            data = response.json()  # Convert the response to JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            data = []

        if not data:  # No more data to fetch, break out of the loop
            break
        all_data.extend(data)
        params["$offset"] += len(data)  # Move the offset for the next request
    df = pd.DataFrame(all_data)
    return df

df_datos = Connection_DatosAbiertos('2021-01-01','2021-06-30',url)

df_datos["fecha_reporte_web"] = pd.to_datetime(df_datos["fecha_reporte_web"])
df_datos["fecha_de_notificaci_n"] = pd.to_datetime(df_datos["fecha_de_notificaci_n"])
df_datos["id_de_caso"] = df_datos["id_de_caso"].astype('int16')
df_datos['edad'] = df_datos['edad'].astype('int8')

df_datos['Mes'] = df_datos["fecha_reporte_web"].dt.month
df_datos['Ahno'] = df_datos["fecha_reporte_web"].dt.year

df = df_datos.groupby(['Mes','Ahno','departamento_nom', 'ciudad_municipio_nom', 'sexo']).agg({
    'id_de_caso': 'count','edad':['min','max',pd.Series.var]  # Edad mínima, máxima y varianza
}).reset_index()

df.columns = ['Mes','Ahno', 'departamento_nom', 'ciudad_municipio_nom', 'sexo', 'Cantidad_casos', 'Edad_minima', 'Edad_Maxima', 'Varianza']
df.to_csv('Datos.txt', sep='|', index = False)
