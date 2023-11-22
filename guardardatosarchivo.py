import json

# Función para guardar datos en un archivo
def guardar_datos(data, archivo):
    with open(archivo, 'w') as file:
        json.dump(data, file)


def agregar_datos(data, archivo):
    with open(archivo, 'a') as file:
        json.dump(data, file)
        file.write('\n')

#Función para leer datos desde un archivo
def leer_datos(archivo):
    with open(archivo, 'r') as file:
        data = json.load(file)
    return data

def leer_datos2(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
    return contenido

# Datos de ejemplo para guardar
datos_a_guardar = {
    'nombre': 'Juan',
    'edad': 19,
    'ciudad': 'A Coruna'
}

# Nombre del archivo
nombre_archivo = 'practica1\IS\guardardatos.txt'

# Guardar datos en el archivo
#guardar_datos(datos_a_guardar, nombre_archivo)

# Agregar datos en el archivo
agregar_datos(datos_a_guardar, nombre_archivo)

# Leer datos desde el archivo
#datos_recuperados = leer_datos(nombre_archivo)
datos_recuperados2 = leer_datos2(nombre_archivo)


# Mostrar los datos recuperados
print("Datos recuperados:", datos_recuperados2)
