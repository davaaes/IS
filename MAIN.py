import tkinter as tk
from tkinter import filedialog

global archivo

def cargar_archivo():
    
    global archivo

    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        entrada_texto.config(state='normal')  # Habilitar el cuadro de texto
        entrada_texto.delete(0, tk.END)  # Limpiar el contenido actual
        entrada_texto.insert(0, archivo)  # Insertar la ruta del archivo seleccionado
        entrada_texto.config(state='disabled')  # Volver a deshabilitar el cuadro de texto


ventana = tk.Tk()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}") 

entrada_texto = tk.Entry(ventana,state='disabled', width=40)
entrada_texto.pack(pady=10)

# Botón para cargar un archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack(pady=10)




















ventana.mainloop()