import unittest
import pandas as pd
from lector import leer_archivo
from modelos import *

class TestArchivo(unittest.TestCase):
    def test_leer_archivo_con_archivo_csv(self):
        ruta = 'housingcsv.csv'
        df = leer_archivo(ruta)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsNotNone(df)

    def test_leer_archivo_con_archivo_xlsx(self):
        ruta_xlsx = 'housing.xlsx'
        df_xlsx = leer_archivo(ruta_xlsx)
        self.assertIsInstance(df_xlsx, pd.DataFrame)
        self.assertIsNotNone(df_xlsx)

    def test_leer_archivo_con_archivo_db(self):
        ruta_db = 'housing.db'
        df_db = leer_archivo(ruta_db)
        self.assertIsInstance(df_db, pd.DataFrame)
        self.assertIsNotNone(df_db)

if __name__ == '__main__':
    unittest.main()