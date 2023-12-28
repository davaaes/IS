import pandas as pd
import sqlite3

def leer_archivo(ruta):
    """
    Lee un archivo en formato CSV, Excel o SQLite y devuelve un DataFrame de Pandas.

    Parameters:
    - ruta (str): Ruta del archivo a leer.

    Returns:
    pd.DataFrame or None: DataFrame de Pandas que contiene los datos del archivo, o None si hay un error.
    """
    if ruta.endswith('.csv'):
        # Si la ruta termina con '.csv', lee el archivo CSV utilizando pandas
        df = pd.read_csv(ruta)
    elif ruta.endswith('.xlsx'):
        # Si la ruta termina con '.xlsx', lee el archivo Excel utilizando pandas
        df = pd.read_excel(ruta)
    elif ruta.endswith('.db'):
        try:
            # Obtener nombres de las tablas
            nombres_tablas = obtener_nombres_tablas(ruta)

            if nombres_tablas is not None and len(nombres_tablas) > 0:
                # Tomar el primer nombre de la tabla (puedes ajustar esto según tus necesidades)
                nombre_tabla = nombres_tablas[0]

                # Crear una conexión a la base de datos SQLite
                conn = sqlite3.connect(ruta)

                # Leer los datos de la tabla en un DataFrame de Pandas
                query = f"SELECT * FROM {nombre_tabla}"
                df = pd.read_sql_query(query, conn)

                # Cerrar la conexión
                conn.close()
            else:
                print("No se encontraron tablas en la base de datos.")
                df = None

        except Exception as e:
            print(f"Error al leer el archivo SQLite: {str(e)}")
            df = None
    else:
        print("Formato de archivo no compatible. Utilice archivos CSV, Excel o SQLite.")
        df = None

    return df

# Definir la función para obtener los nombres de las tablas en una base de datos SQLite
def obtener_nombres_tablas(ruta):
    """
    Obtiene los nombres de las tablas en una base de datos SQLite.

    Parameters:
    - ruta (str): Ruta del archivo de la base de datos SQLite.

    Returns:
    list or None: Lista de nombres de tablas, o None si hay un error.
    """
    try:
        # Conectar a la base de datos SQLite usando 'sqlite3.connect'
        with sqlite3.connect(ruta) as conn:
            # Definir la consulta SQL para obtener los nombres de las tablas
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            # Ejecutar la consulta y obtener el resultado
            resultado = conn.execute(query)
            # Extraer los nombres de las tablas de las filas del resultado
            return [row[0] for row in resultado.fetchall()]
    except Exception as e:
        # Capturar cualquier excepción y elevar un RuntimeError con un mensaje descriptivo
        raise RuntimeError(f"Error al obtener nombres de tablas: {str(e)}")
