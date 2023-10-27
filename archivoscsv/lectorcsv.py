import pandas as pd

dfexcel = pd.read_excel("./archivoscsv\housing.xlsx")

print(dfexcel)

dfcsv = pd.read_csv("./archivoscsv\housingcsv.csv")

print(dfcsv)