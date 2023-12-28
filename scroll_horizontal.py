import tkinter as tk
from tkinter import ttk

def configurar_scroll_horizontal(parent_frame):
    """
    Configura el desplazamiento horizontal para un lienzo en un marco principal.

    Parameters:
    - parent_frame (tkinter.Frame): Marco principal al que se aplicará el desplazamiento horizontal.

    Returns:
    tuple: Tupla con el lienzo y el marco secundario configurados.
    """
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
    """
    Configura el marco secundario en el lienzo para permitir el desplazamiento.

    Parameters:
    - canvas (tkinter.Canvas): Lienzo al que se conectará el marco secundario.
    - second_frame (tkinter.Frame): Marco secundario que se configurará en el lienzo.
    """
    # Crear la ventana en el lienzo para el marco secundario
    canvas.create_window((0, 0), window=second_frame, anchor='nw')

    # Vincular la función de configuración del lienzo al evento de configuración del marco secundario
    second_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))