import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modelos import *

class TestRegresion(unittest.TestCase):


    def setUp(self):
        archivo_csv='housingcsv.csv'
        self.df = pd.read_csv(archivo_csv)


    def test_regresion1(self):
    
        columna_indep = ['latitude']
        columnas_dep = ['longitude']       
        
        result =regresion(columna_indep,columnas_dep, self.df)

    
        assert result is not None
    

if __name__ == '__main__':
    unittest.main()
