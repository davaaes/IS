import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import lector as l
from modelos import *

global estados_checkbuttons, opcion_seleccionada 


def mostrar_modelo():
    global estados_checkbuttons, opcion_seleccionada,columnas,dataframe
    lista_vo=[opcion_seleccionada.get()]
    list_vi=[]
    for i in range(len(estados_checkbuttons)):
        if estados_checkbuttons[i].get()==True:
            list_vi.append(columnas[i])
    if len(list_vi)==0:
        tk.messagebox.showerror("Error", "Seleccione al menos una variable independiente.")
        return

    # Verificar si se ha seleccionado una variable objetivo
    if not opcion_seleccionada.get():
        tk.messagebox.showerror("Error", "Seleccione una variable objetivo.")
        return
    if "ocean_proximity" in list_vi or "ocean_proximity" in lista_vo:
        tk.messagebox.showerror("Error", "La variable ocean_proximity no puede usarse como variable ya que es una cadena de texto.")
        return
    fig,error,formula= regresion(lista_vo, list_vi, dataframe)
    mostrar_formula(error,formula)
    plot_grafico(fig)

def mostrar_formula(error,formula):
    formula_error = tk.Label(ventana, text=f"Formula={formula}\nError={error}")
    formula_error.pack()

def plot_grafico(fig):
    fig.set_size_inches(6, 3)
    frame_grafica = tk.Frame(ventana,width=500, height=300)
    frame_grafica.pack(pady=10, padx=10)
    # Crea el lienzo de Tkinter para la figura de Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

def guardar_modelo():
    global dataframe, opcion_seleccionada,estados_checkbuttons
    lista_vo=[opcion_seleccionada.get()]
    list_vi=[]
    for i in range(len(estados_checkbuttons)):
        if estados_checkbuttons[i].get()==True:
            list_vi.append(columnas[i])
    regresion(lista_vo,list_vi,dataframe,"sacadon.png")

def cerrar_programa():
    sys.exit()
 
def cargar_archivo():
    global archivo,dataframe
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        entrada_texto.config(state='normal')  # Habilitar el cuadro de texto
        entrada_texto.delete(0, tk.END)  # Limpiar el contenido actual
        entrada_texto.insert(0, archivo)  # Insertar la ruta del archivo seleccionado
        entrada_texto.config(state='disabled')  # Volver a deshabilitar el cuadro de texto

        # Utilizar la ruta del archivo con la función leer_archivo
        dataframe = l.leer_archivo(archivo)

        if dataframe is not None:

            # Crear un Frame para la tabla
            frame_tabla = tk.Frame(ventana)
            frame_tabla.pack(pady=10, padx=10)

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
    global estados_checkbuttons, opcion_seleccionada,columnas 
    frame_but2 = tk.Frame(ventana)
    frame_but2.pack(padx=10,pady=3)
    frame_but = tk.Frame(ventana)
    frame_but.pack(pady=10, padx=3)
    datos=l.leer_archivo(archivo)
    columnas = list(datos.columns)

    # Crear una nueva ventana para los Checkbuttons

    # Variable para almacenar el estado de cada Checkbutton
    estados_checkbuttons = [tk.BooleanVar() for _ in range(len(columnas))]

    # Crear Checkbuttons dinámicamente en columnas
    for i, columna in enumerate(columnas):
        chk=tk.Label(frame_but,text='VARIABLES INDEPENDIENTES:')
        chk.grid(row=0,column=0,sticky='w')
        checkbutton = ttk.Checkbutton(frame_but, text=columna, variable=estados_checkbuttons[i])
        checkbutton.grid(row=0, column=i+1, sticky="w")



    columnos = list(datos.columns)

    # Crear una nueva ventana para los Radiobuttons


    # Variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()

    # Crear Radiobuttons dinámicamente en columnas
    for i, columna in enumerate(columnos):
        chk=tk.Label(frame_but,text='VARIABLE OBJETIVO:')
        chk.grid(row=1,column=0,sticky='w')
        radiobutton = ttk.Radiobutton(frame_but, text=columna, variable=opcion_seleccionada, value=columna)
        radiobutton.grid(row=1, column=i+1, sticky="w")
    boton_cargar = tk.Button(frame_but2, text="MOSTRAR MODELO", command=mostrar_modelo)
    boton_cargar.grid(row=2,column=5,pady=5)
    boton_guardar = tk.Button(frame_but2, text="GUARDAR MODELO", command=guardar_modelo)
    boton_guardar.grid(row=2,column=6,pady=5,padx=5)
    texto=tk.StringVar()
    etiqueta=tk.Label(frame_but2,text='Como:')
    etiqueta.grid(row=2,column=7)
    pantalla=tk.Entry(frame_but2, textvariable=texto)
    pantalla.grid(row=2,column=8,columnspan=3,rowspan=2)
    

# Crear ventana y otros elementos

ventana = tk.Tk()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

entrada_texto = tk.Entry(ventana, state='disabled', width=40)
entrada_texto.pack(pady=8)

# Botón para cargar un archivo
boton_cargar = tk.Button(ventana, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.place(x=400,y=2)
boton_cerrar = tk.Button(ventana, text="Cerrar Programa", command=cerrar_programa)
boton_cerrar.place(x=1172,y=2)

ventana.mainloop()

