import tkinter as tk 
import numpy as np

ventana = None
frame_tabla = None
frame_grafica = None
frame_but = None
frame_but2 = None
frame_predicciones = None
contenido_cajas = None

def obtener_variables_seleccionadas(estados_checkbuttons, columnas):
    """
    Obtiene las variables seleccionadas a partir de los estados de los Checkbuttons.

    Parameters:
    - estados_checkbuttons (list): Lista de variables BooleanVar asociadas a los Checkbuttons.
    - columnas (list): Lista de nombres de columnas.

    Returns:
    list: Lista de nombres de las variables seleccionadas.
    """
    variables_seleccionadas = [columnas[i] for i in range(len(estados_checkbuttons)) if estados_checkbuttons[i].get()]
    return variables_seleccionadas

def limpiar_interfaz(n,frame_predicciones,frame_grafica,frame_but=None,frame_but2=None,frame_tabla=None):
    """
    Limpia los widgets dentro de los frames de la interfaz gráfica.

    Parameters:
    - n (int): Valor que determina qué partes de la interfaz deben limpiarse (1 o 2).
    - frame_predicciones (tk.Frame): Frame de predicciones.
    - frame_grafica (tk.Frame): Frame de la gráfica.
    - frame_but (tk.Frame, optional): Frame de botones 1.
    - frame_but2 (tk.Frame, optional): Frame de botones 2.
    - frame_tabla (tk.Frame, optional): Frame de la tabla.
    """
    if n==1:
        for widget in frame_tabla.winfo_children():
            widget.destroy()
        for widget in frame_grafica.winfo_children():
            widget.destroy()
        for widget in frame_but2.winfo_children():
            widget.destroy()
        for widget in frame_but.winfo_children():
            widget.destroy()
        for widget in frame_predicciones.winfo_children():
            widget.destroy() 
    elif n==2:
        for widget in frame_grafica.winfo_children():
            widget.destroy()
        for widget in frame_predicciones.winfo_children():
            widget.destroy() 

def obtener_contenido_cajas(contenido_cajas):
    """
    Obtiene el contenido actual de las cajas de entrada.

    Parameters:
    - contenido_cajas (list): Lista de Entry widgets.

    Returns:
    list: Lista de strings, contenido actual de las cajas de entrada.
    """

    contenido_actual = [entrada.get() for entrada in contenido_cajas]
    return contenido_actual

def obtener_y_mostrar_contenido(reg_model,contenido_cajas):
    """
    Obtiene y muestra el contenido actual de las cajas de entrada.

    Parameters:
    - reg_model: Modelo de regresión.
    - contenido_cajas (list): Lista de Entry widgets.

    Returns:
    numpy.ndarray: Predicción del modelo.
    """
    contenido_actual = obtener_contenido_cajas(contenido_cajas)
    print("Contenido actual de las cajas:", contenido_actual)

    # Convertir los valores a un array NumPy
    valores_x = np.array(contenido_actual, dtype=float)

    # Reshape para que sea 2D si es necesario
    if len(valores_x.shape) == 1:
        valores_x = valores_x.reshape(1, -1)

    # Realizar la predicción
    prediccion = reg_model.predict(valores_x)

    return prediccion