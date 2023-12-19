import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import lector as l
from modelos import *
import joblib
from decimal import Decimal, getcontext


global estados_checkbuttons, opcion_seleccionada, list_vi


def mostrar_modelo():
    global estados_checkbuttons, opcion_seleccionada,columnas,dataframe,interc,coef,list_vi
    n=1
    limpiar_interfaz(2)
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
    fig,error,formula,interc,coef,columna_dep= regresion(lista_vo, list_vi, dataframe)
    predicciones(list_vi)
    mostrar_formula(error,formula,n)
    plot_grafico(fig)

def mostrar_formula(error,formula,n):
    contenido = f"Formula={formula}\nError={error}"

    if n==1:
        formula_error = tk.Label(frame_grafica, text=f"Formula={formula}\nError={error}")
    else:
        formula_error = tk.Label(text=f"Formula={formula}\nError={error}")

    formula_error.pack()

def plot_grafico(fig):
    fig.set_size_inches(3, 2)
    # Crea el lienzo de Tkinter para la figura de Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

def guardar_modelo():
    global dataframe, opcion_seleccionada, estados_checkbuttons

    lista_vo = [opcion_seleccionada.get()]
    list_vi = []
    for i in range(len(estados_checkbuttons)):
        if estados_checkbuttons[i].get() == True:
            list_vi.append(columnas[i])

    if len(list_vi) == 0:
        tk.messagebox.showerror("Error", "Seleccione al menos una variable independiente.")
        return

    if not opcion_seleccionada.get():
        tk.messagebox.showerror("Error", "Seleccione una variable objetivo.")
        return

    if "ocean_proximity" in list_vi or "ocean_proximity" in lista_vo:
        tk.messagebox.showerror(
            "Error", "La variable ocean_proximity no puede usarse como variable ya que es una cadena de texto."
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".joblib",
        filetypes=[("Joblib files", "*.joblib"), ("All files", "*.*")],
        title="Guardar Modelo",
    )

    if not file_path:
        return  

    modelo = Modelo()

    # Entrenar el modelo y asignarlo a la instancia
    modelo.entrenar_modelo(lista_vo, list_vi, dataframe)

    try:
        # Guardar el modelo utilizando la clase Modelo
        modelo.guardar_modelo(file_path)
        tk.messagebox.showinfo("Éxito", f"Modelo guardado en: {file_path}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al guardar el modelo: {e}")

def cargarModelo():
    global opcion_seleccionada, estados_checkbuttons, dataframe, columnas,list_vi

    # Seleccionar un archivo de modelo previamente guardado
    
    filename = filedialog.askopenfilename(title="Seleccionar modelo", filetypes=[("Joblib files", "*.joblib"), ("All files", "*.*")])
    if filename is not None:
        limpiar_interfaz(1)
        # Crear una instancia de la clase Modelo
        modelo = Modelo()
        
        # Cargar el modelo desde el archivo especificado
        modelo_interno = modelo.cargar_modelo(filename)
        
        
        
        if modelo_interno is not None:
            # Obtener los coeficientes y el término independiente desde el modelo interno
            fig,error, formula, intercepto, coeficientes,columna_indep = modelo_interno
              # Assuming the intercept is stored in the array
            coeficientes = coeficientes.flatten().tolist()
            predicciones(columna_indep)
            mostrar_formula(error,formula,1)

            # Ahora tendrás tus coeficientes como una lista con comas
            # Mostrar detalles del modelo cargado
            
            print(f"El modelo {filename} tiene de error1: {error}, intercepto: {intercepto}, y coeficientes: {coeficientes}")  
            

            
        else:
            print("El modelo interno es None. Revisa la carga del modelo.")

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
            limpiar_interfaz(1)
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
    boton_cargar.grid(row=2,column=5,pady=3)
    boton_guardar = tk.Button(frame_but2, text="GUARDAR MODELO", command=guardar_modelo)
    boton_guardar.grid(row=2,column=6,pady=3,padx=5)
     
def limpiar_interfaz(n):
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
# Crear ventana y otros elementos
def on_horizontal_scroll(*args):
    my_canvas.xview(*args)
def predicciones(list_vi):
    global my_canvas


    
    my_scrollbar=ttk.Scrollbar(frame_predicciones, orient="horizontal", command=on_horizontal_scroll)
    my_scrollbar.pack(side='top',fill='x')
    my_canvas= tk.Canvas(frame_predicciones,xscrollcommand=my_scrollbar.set)
    my_canvas.pack(side='bottom',fill="both", expand=True)
    second_frame= tk.Frame(my_canvas)
    j=0
    for i in list_vi:
        
        nombre=tk.Label(second_frame,text=str(i))
        nombre.grid(column=j,row=0,padx=4)
        j+=1
        entrada_texto=tk.Entry(second_frame,state='normal')
        entrada_texto.grid(column=j,row=0,padx=4)
        j+=1
    my_canvas.create_window((0,0), window=second_frame, anchor='nw')
    second_frame.bind("<Configure>", lambda event, canvas=my_canvas: canvas.configure(scrollregion=my_canvas.bbox("all")))
def cerrar_ventana():
    ventana.destroy()
    sys.exit()

ventana = tk.Tk()
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Contenedor para la fila 0 (entrada de texto y botones)
frame_top = tk.Frame(ventana)
frame_top.pack(side="top", fill="x")

entrada_texto = tk.Entry(frame_top, state='disabled', width=80)
entrada_texto.grid(row=0,column=0,pady=3,padx=10)

# Crear un Frame para la tabla
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=5, padx=10)

# Crear un Frame para los botones de variables
frame_but2 = tk.Frame(ventana)
frame_but2.pack(padx=10,pady=3)
frame_but = tk.Frame(ventana)
frame_but.pack(pady=5, padx=3)

# Botón para cargar un archivo
boton_elegir = tk.Button(frame_top, text="Elegir archivo", command=cargar_archivo)
boton_elegir.grid(row=0, column=1, pady=3, padx=(10, 5), sticky='n', ipadx=10)

boton_cargar = tk.Button(frame_top, text="Cargar modelo", command=cargarModelo)
boton_cargar.grid(row=0, column=2, pady=3, padx=(5, 10), sticky='n', ipadx=10)

# Crear un Frame para la grafica
frame_grafica = tk.Frame(ventana,width=400, height=200)
frame_grafica.pack()
frame_predicciones=tk.Frame(ventana,padx=5,pady=5)
frame_predicciones.pack(fill="both", expand=True)

ventana.mainloop()

