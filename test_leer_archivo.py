import unittest
import pandas as pd
from lector import leer_archivo
from modelos import *

# Definir una clase que hereda de unittest.TestCase para realizar pruebas
class TestArchivo(unittest.TestCase):
    # Definir un método de prueba para leer un archivo CSV
    def test_leer_archivo_con_archivo_csv(self):
        # Definir la ruta del archivo CSV
        ruta = 'housingcsv.csv'
        # Llamar a la función leer_archivo con la ruta del archivo CSV
        df = leer_archivo(ruta)
        # Verificar que el resultado sea una instancia de DataFrame de pandas
        self.assertIsInstance(df, pd.DataFrame)
        # Verificar que el DataFrame no sea nulo
        self.assertIsNotNone(df)

    # Definir un método de prueba para leer un archivo XLSX
    def test_leer_archivo_con_archivo_xlsx(self):
        # Definir la ruta del archivo XLSX
        ruta_xlsx = 'housing.xlsx'
        # Llamar a la función leer_archivo con la ruta del archivo XLSX
        df_xlsx = leer_archivo(ruta_xlsx)
        # Verificar que el resultado sea una instancia de DataFrame de pandas
        self.assertIsInstance(df_xlsx, pd.DataFrame)
        # Verificar que el DataFrame no sea nulo
        self.assertIsNotNone(df_xlsx)

    # Definir un método de prueba para leer un archivo de base de datos
    def test_leer_archivo_con_archivo_db(self):
        # Definir la ruta del archivo de base de datos
        ruta_db = 'housing.db'
        # Llamar a la función leer_archivo con la ruta del archivo de base de datos
        df_db = leer_archivo(ruta_db)
        # Verificar que el resultado sea una instancia de DataFrame de pandas
        self.assertIsInstance(df_db, pd.DataFrame)
        # Verificar que el DataFrame no sea nulo
        self.assertIsNotNone(df_db)

# Si este archivo es el archivo principal que se ejecuta
if __name__ == '__main__':
    # Ejecutar todas las pruebas definidas en la clase TestArchivo
    unittest.main()