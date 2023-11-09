# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:19:21 2023

@author: Jacobo
"""
import lectorcsv as l
import pandas as pd
def seleccionar_columnas(df):
    X = input("ingresa el nombre de la columna: ")
    while X not in df.columns or not pd.api.types.is_numeric_dtype(df[X]):
        if X not in df.columns:
            print("La columna no existe. Prueba otra vez: ")
        else:
            print("La columna no tiene datos numéricos, indica otra columna ")
        X = input("ingresa el nombre de la  columna: ")
    return df[X]

