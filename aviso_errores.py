import tkinter as tk
from tkinter import filedialog, messagebox
from modelos import Modelo


def mostrar_error(mensaje):
    tk.messagebox.showerror("Error", mensaje)

def mostrar_info(mensaje):
    tk.messagebox.showinfo("Éxito", mensaje)

def validar_variables_seleccionadas(list_vi):
    if len(list_vi) == 0:
        mostrar_error("Seleccione al menos una variable independiente.")
        return False
    return True

def validar_variable_objetivo(opcion_seleccionada):
    if not opcion_seleccionada.get():
        mostrar_error("Seleccione una variable objetivo.")
        return False
    return True

def validar_variable_ocean_proximity(list_vi, lista_vo):
    if "ocean_proximity" in list_vi or "ocean_proximity" in lista_vo:
        mostrar_error("La variable ocean_proximity no puede usarse como variable ya que es una cadena de texto.")
        return False
    return True

