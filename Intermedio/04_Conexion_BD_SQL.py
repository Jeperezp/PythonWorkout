import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

Server = os.getenv('Servidor')
user = os.getenv('Usuario')
Password = os.getenv('contrasena')
DataBase = os.getenv('DataBase')
Query = os.getenv('Consulta_sql')

def conexion_bd(Query:str) -> pd.DataFrame:
    """
    Connects to a database SOLIP using the provided configuration parameters and executes a SQL query.

    Parameters:
    Query (str): SQL query to execute on the database.
    Returns:
    pandas.DataFrame: DataFrame containing the results of the SQL query.

    Raises:
    Exception: If an error occurs during the connection or execution of the query.

    Example:
    >>> conexion_bd("SELECT * FROM example_table")
    """
    
    try:
        # Establish a connection to the database using the provided DSN, username, and password from the configuration.
        conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={Server};DATABASE={DataBase};UID={user};PWD={Password}")
        # Execute the SQL query and store the results in a DataFrame.
        df = pd.read_sql(Query, conn,)
        return df
    except Exception as e:
        # If an error occurs, print the error message.
        print(e)
    finally:
        # Close the connection to the database, regardless of whether there was an error or not.
        conn.close()


df = conexion_bd(Query=Query)
print(df)
df.to_csv('Archivo_salida.txt', sep='|',index=False)

