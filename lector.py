import pandas as pd
import sqlite3

def obtener_nombres_tablas(ruta):
    try:
        # Crear una conexión a la base de datos SQLite
        conn = sqlite3.connect(ruta)

        # Consulta para obtener los nombres de las tablas
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        resultado = conn.execute(query)

        # Obtener nombres de las tablas
        nombres_tablas = [row[0] for row in resultado.fetchall()]

        # Cerrar la conexión
        conn.close()

        return nombres_tablas

    except Exception as e:
        print(f"Error al obtener nombres de tablas: {str(e)}")
        return None

def leer_archivo(ruta):
    if ruta.endswith('.csv'):
        df = pd.read_csv(ruta)
    elif ruta.endswith('.xlsx'):
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