import tkinter as tk
from tkinter import filedialog, messagebox
from modelos import Modelo


def mostrar_error(mensaje):
    """
    Muestra un cuadro de diálogo de error con el mensaje especificado.

    Parameters:
    - mensaje (str): Mensaje de error a mostrar.
    """
    tk.messagebox.showerror("Error", mensaje)

def mostrar_info(mensaje):
    """
    Muestra un cuadro de diálogo informativo con el mensaje especificado.

    Parameters:
    - mensaje (str): Mensaje informativo a mostrar.
    """
    tk.messagebox.showinfo("Éxito", mensaje)

def validar_variables_seleccionadas(list_vi):
    """
    Valida si al menos una variable independiente ha sido seleccionada.

    Parameters:
    - list_vi (list): Lista de variables independientes seleccionadas.

    Returns:
    bool: True si al menos una variable independiente está seleccionada, False de lo contrario.
    """
    if len(list_vi) == 0:
        mostrar_error("Seleccione al menos una variable independiente.")
        return False
    return True

def validar_variable_objetivo(opcion_seleccionada):
    """
    Valida si se ha seleccionado una variable objetivo.

    Parameters:
    - opcion_seleccionada (tkinter.StringVar): Variable de control que almacena la opción seleccionada.

    Returns:
    bool: True si se ha seleccionado una variable objetivo, False de lo contrario.
    """
    if not opcion_seleccionada.get():
        mostrar_error("Seleccione una variable objetivo.")
        return False
    return True

def validar_variable_ocean_proximity(list_vi, lista_vo):
    """
    Valida si la variable ocean_proximity está presente en las variables independientes o en la variable objetivo.

    Parameters:
    - list_vi (list): Lista de variables independientes.
    - lista_vo (list): Lista de variables objetivo.

    Returns:
    bool: True si la variable ocean_proximity no está presente en list_vi ni en lista_vo, False de lo contrario.
    """
    if "ocean_proximity" in list_vi or "ocean_proximity" in lista_vo:
        mostrar_error("La variable ocean_proximity no puede usarse como variable ya que es una cadena de texto.")
        return False
    return True

