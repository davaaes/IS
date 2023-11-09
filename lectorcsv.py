import pandas as pd
def leer_excel():
    dfexcel = pd.read_excel("./archivoscsv\housing.xlsx")
    return dfexcel
def leer_csv():
    dfcsv = pd.read_csv("./archivoscsv\housingcsv.csv")
    return dfcsv
