import pandas as pd
def leer_archivo(archivo):
    if archivo.endswith('.csv'):
        return pd.read_csv(archivo)
    elif archivo.endswith('.xlsx') or archivo.endswith('.xls'):
        return pd.read_excel(archivo)
    else:
        raise ValueError("Formato de archivo no compatible. Debe ser CSV o Excel.")
