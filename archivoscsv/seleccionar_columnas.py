# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:19:21 2023

@author: Jacobo
"""
import pandas as pd

df = pd.read_excel("./archivoscsv\housing.xlsx")  # O pd.read_csv("housing.csv") si prefieres el archivo CSV

columna1 = input("ingresa el nombre de la primera columna: ")
while columna1 not in df.columns or not pd.api.types.is_numeric_dtype(df[columna1]):
    if columna1 not in df.columns:
        print("La columna no existe. Prueba otra vez: ")
    else:
        print("La columna no tiene datos numéricos, indica otra columna ")
    columna1 = input("ingresa el nombre de la primera columna: ")

columna2 = input("ingresa el nombre de la segunda columna: ")
while columna2 not in df.columns or not pd.api.types.is_numeric_dtype(df[columna2]) or columna2 == columna1:
    if columna2 not in df.columns:
        print("La columna no existe. Prueba otra vez: ")
    elif not pd.api.types.is_numeric_dtype(df[columna2]):
        print("La columna no tiene datos numéricos, indica otra columna ")
    else:
        print("La segunda columna no puede ser igual a la primera. Por favor, intenta de nuevo.")
    columna2 = input("ingresa el nombre de la segunda columna: ")