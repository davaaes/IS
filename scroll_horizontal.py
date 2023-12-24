import tkinter as tk
from tkinter import ttk

def configurar_scroll_horizontal(parent_frame):
    # Función para manejar el desplazamiento horizontal del lienzo
    def on_horizontal_scroll(*args):
        canvas.xview(*args)

    # Crear una barra de desplazamiento horizontal
    scrollbar_horizontal = ttk.Scrollbar(parent_frame, orient="horizontal", command=on_horizontal_scroll)
    scrollbar_horizontal.pack(side='top', fill='x')

    # Crear un lienzo que se conectará a la barra de desplazamiento
    canvas = tk.Canvas(parent_frame, xscrollcommand=scrollbar_horizontal.set, highlightthickness=0)
    canvas.pack(side='bottom', fill="both", expand=True)

    # Crear un marco secundario en el lienzo
    second_frame = tk.Frame(canvas)

    return canvas,second_frame
def configurar_marco_scroll(canvas,second_frame):
    # Crear la ventana en el lienzo para el marco secundario
    canvas.create_window((0, 0), window=second_frame, anchor='nw')

    # Vincular la función de configuración del lienzo al evento de configuración del marco secundario
    second_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))