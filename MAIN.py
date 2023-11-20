import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import lectorcsv as l

def cargar_archivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        entrada_texto.config(state='normal')  # Habilitar el cuadro de texto
        entrada_texto.delete(0, tk.END)  # Limpiar el contenido actual
        entrada_texto.insert(0, archivo)  # Insertar la ruta del archivo seleccionado
        entrada_texto.config(state='disabled')  # Volver a deshabilitar el cuadro de texto

        # Utilizar la ruta del archivo con la función leer_archivo
        dataframe = l.leer_archivo(archivo)

        if dataframe is not None:
            print("Archivo leído exitosamente.")

            # Crear un Frame para la tabla
            frame_tabla = tk.Frame(ventana)
            frame_tabla.pack(pady=20, padx=20)

            # Crear un Treeview para mostrar la tabla
            treeview = ttk.Treeview(frame_tabla)
            treeview["columns"] = tuple(dataframe.columns)
            
            # Configurar encabezados
            for column in dataframe.columns:
                treeview.heading(column, text=column)
            
            # Insertar datos
            for i, row in dataframe.iterrows():
                treeview.insert("", i, values=tuple(row))
            
            # Agregar barras de desplazamiento vertical y horizontal dentro del Treeview
            yscroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=treeview.yview)
            yscroll.pack(side="right", fill="y")
            treeview.configure(yscrollcommand=yscroll.set)

            xscroll = ttk.Scrollbar(frame_tabla, orient="horizontal", command=treeview.xview)
            xscroll.pack(side="bottom", fill="x")
            treeview.configure(xscrollcommand=xscroll.set)
            
            # Centrar la tabla en el Frame
            treeview.pack()
    crear_checkbuttons()
def crear_checkbuttons():
    # Leer las columnas desde el archivo
    # Cambia 'ruta/del/archivo.csv' con la ruta correcta de tu archivo
    frame_but = tk.Frame(ventana)
    frame_but.pack(pady=20, padx=20)
    datos=l.leer_archivo(archivo)
    columnas = list(datos.columns)

    # Crear una nueva ventana para los Checkbuttons

    # Variable para almacenar el estado de cada Checkbutton
    estados_checkbuttons = [tk.BooleanVar() for _ in range(len(columnas))]

    # Crear Checkbuttons dinámicamente en columnas
    for i, columna in enumerate(columnas):
        checkbutton = ttk.Checkbutton(frame_but, text=columna, variable=estados_checkbuttons[i])
        checkbutton.grid(row=0, column=i, sticky="w")


    columnos = list(datos.columns)

    # Crear una nueva ventana para los Radiobuttons


    # Variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()

    # Crear Radiobuttons dinámicamente en columnas
    for i, columna in enumerate(columnos):
        radiobutton = ttk.Radiobutton(frame_but, text=columna, variable=opcion_seleccionada, value=columna)
        radiobutton.grid(row=1, column=i, sticky="w")
# Crear ventana y otros elementos





ventana = tk.Tk()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

entrada_texto = tk.Entry(ventana, state='disabled', width=40)
entrada_texto.pack(pady=10)

# Botón para cargar un archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack(pady=10)

ventana.mainloop()

