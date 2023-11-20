import pandas as pd

def leer_archivo(ruta):
    if ruta.endswith('.csv'):
        df = pd.read_csv(ruta)
    elif ruta.endswith('.xlsx'):
        df = pd.read_excel(ruta)
    return df