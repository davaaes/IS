import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modelos import *

# Definir una clase que hereda de unittest.TestCase para realizar pruebas
class TestRegresion(unittest.TestCase):

    # Método setUp que se ejecuta antes de cada método de prueba
    def setUp(self):
        # Definir la ruta del archivo CSV para la prueba
        archivo_csv = 'housingcsv.csv'
        # Leer el archivo CSV y asignar el DataFrame a self.df para su uso en las pruebas
        self.df = pd.read_csv(archivo_csv)

    # Método de prueba para la función de regresión con una configuración específica
    def test_regresion1(self):
        # Definir las columnas independientes y dependientes para la prueba
        columna_indep = ['latitude']
        columnas_dep = ['longitude']       
        # Llamar a la función de regresión con la configuración específica y el DataFrame
        result = regresion(columna_indep, columnas_dep, self.df)
        # Afirmar que el resultado no es nulo
        self.assertIsNotNone(result)

# Si este archivo es el archivo principal que se ejecuta
if __name__ == '__main__':
    # Ejecutar todas las pruebas definidas en la clase TestRegresion
    unittest.main()
