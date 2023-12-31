import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import lector as l
from modelos import *
import joblib
from decimal import Decimal, getcontext
from scroll_horizontal import *
from aviso_errores import *
from funciones_auxiliares import *

global estados_checkbuttons, opcion_seleccionada, list_vi



def mostrar_modelo():
    """
    Muestra el modelo de regresión lineal en la interfaz gráfica, incluyendo la tabla de predicciones y la fórmula.

    """
    global estados_checkbuttons, opcion_seleccionada,columnas,dataframe,interc,coef,list_vi
    n=1
    limpiar_interfaz(2,frame_predicciones,frame_grafica,frame_but,frame_but2,frame_tabla)
    lista_vo=[opcion_seleccionada.get()]
    list_vi= obtener_variables_seleccionadas(estados_checkbuttons, columnas)
    if not validar_variables_seleccionadas(list_vi) or not validar_variable_objetivo(opcion_seleccionada):
        return

    if not validar_variable_ocean_proximity(list_vi, lista_vo):
        return
    
    reg,fig,error,formula,interc,coef,columna_dep,columna_indep= regresion(lista_vo, list_vi, dataframe)
    predicciones(columna_dep,reg,columna_indep)
    mostrar_formula(error,formula,n)
    plot_grafico(fig,columna_dep)

def mostrar_formula(error, formula, n):
    """
    Muestra la fórmula y el error del modelo en la interfaz gráfica.

    Parameters:
    - error (float): El error del modelo.
    - formula (str): La fórmula del modelo.
    - n (int): Número que indica si es la primera vez que se muestra la fórmula (1) o no (otros valores).

    """
    global etiqueta_formula_error

    contenido = f"Formula={formula}\nError={error}"

    if n == 1:
        etiqueta_formula_error = tk.Label(frame_grafica, text=contenido)
    else:
        etiqueta_formula_error.config(text=contenido)

    etiqueta_formula_error.pack()

def plot_grafico(fig,columna_dep):
    """
    Plotea el gráfico de la regresión en la interfaz gráfica.

    Parameters:
    - fig (matplotlib.figure.Figure): La figura de Matplotlib a ser mostrada.
    - columna_dep (str): Nombre de la columna dependiente.

    """
    # Crear un marco secundario en el lienzo con el scroll configurado
    my_canvas,second_frame = configurar_scroll_horizontal(frame_grafica)

    # Configurar el lienzo para la figura de Matplotlib
    canvas_fig = FigureCanvasTkAgg(fig, master=second_frame)
    canvas_widget = canvas_fig.get_tk_widget()
    canvas_widget.pack(side="top",expand=True, fill="both")

    # Configurar la ventana en el lienzo y vincular la función de configuración
    configurar_marco_scroll(my_canvas,second_frame)
    
    #Si la gráfica tiene 1 o 2 columnas dependientes se ajustara al second_frame para centrarse
    if len(columna_dep)<=2:
        second_frame.pack(side="top", fill="both")

def mostrar_ventana_entrada():
    """
    Muestra una ventana para que el usuario ingrese una descripción del modelo de regresión.

    """
    global ventana_entrada,cuadro_texto
    # Crear una nueva ventana superior (Toplevel)
    ventana_entrada = tk.Toplevel(ventana)
    ventana_entrada.update_idletasks()
    width = 400
    height = 200
    x = (ventana_entrada.winfo_screenwidth() - width) // 2
    y = (ventana_entrada.winfo_screenheight() - height) // 2
    ventana_entrada.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    ventana_entrada.title("Descripción")

    # Etiqueta y cuadro de entrada en la nueva ventana
    etiqueta_entrada = tk.Label(ventana_entrada, text="Describa su regresión")
    etiqueta_entrada.pack(pady=10)

    cuadro_texto = tk.Text(ventana_entrada, wrap="word", height=5, width=40)  # Puedes ajustar height y width según tus necesidades
    cuadro_texto.pack(pady=10, expand=True)
    boton_desc = tk.Button(ventana_entrada,text='Guardar',command=guardar_modelo)
    boton_desc.pack(padx=5,pady=5)

def guardar_modelo():
    """
    Guarda el modelo entrenado en un archivo utilizando la clase Modelo.

    """
    global dataframe, opcion_seleccionada, estados_checkbuttons,columnas
    descripcion=cuadro_texto.get('1.0',tk.END)
    ventana_entrada.destroy()
    lista_vo = [opcion_seleccionada.get()]
    list_vi= obtener_variables_seleccionadas(estados_checkbuttons, columnas)

    if not validar_variables_seleccionadas(list_vi) or not validar_variable_objetivo(opcion_seleccionada):
        return

    if not validar_variable_ocean_proximity(list_vi, lista_vo):
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
    modelo.entrenar_modelo(lista_vo, list_vi,descripcion, dataframe)

    try:
        # Guardar el modelo utilizando la clase Modelo
        modelo.guardar_modelo(file_path)
        mostrar_info(f"Modelo guardado en: {file_path}")
    except Exception as e:
        mostrar_error(f"Error al guardar el modelo: {e}")

def cargarModelo():
    """
    Carga un modelo previamente guardado desde un archivo y muestra detalles sobre el modelo.

    """
    global opcion_seleccionada, estados_checkbuttons, dataframe, columnas,list_vi

    # Seleccionar un archivo de modelo previamente guardado
    
    filename = filedialog.askopenfilename(title="Seleccionar modelo", filetypes=[("Joblib files", "*.joblib"), ("All files", "*.*")])
    if filename is not None:
        # Crear una instancia de la clase Modelo
        modelo = Modelo()
        
        # Cargar el modelo desde el archivo especificado
        modelo_interno = modelo.cargar_modelo(filename)
        
        
        if modelo_interno is not None:
            limpiar_interfaz(1,frame_predicciones,frame_grafica,frame_but,frame_but2,frame_tabla)
            # Obtener los coeficientes y el término independiente desde el modelo interno
            reg,fig,error, formula, intercepto, coeficientes,columna_dep,descripcion,columna_indep = modelo_interno
              # Assuming the intercept is stored in the array
            coeficientes = coeficientes.flatten().tolist()
            predicciones(columna_dep,reg,columna_indep)
            mostrar_formula(error,formula,1)
            mostrar_descripcion(descripcion)
            # Ahora tendrás tus coeficientes como una lista con comas
            # Mostrar detalles del modelo cargado
            
            print(f"El modelo {filename} tiene de error1: {error}, intercepto: {intercepto}, y coeficientes: {coeficientes}")  
            

            
        else:
            print("El modelo interno es None. Revisa la carga del modelo.")

def cargar_archivo():
    """
    Abre un cuadro de diálogo para que el usuario seleccione un archivo y carga los datos en la interfaz.

    """
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
            limpiar_interfaz(1,frame_predicciones,frame_grafica,frame_but,frame_but2,frame_tabla)
            # Crear un Treeview para mostrar la tabla
            treeview = ttk.Treeview(frame_tabla)
            treeview["columns"] = tuple(dataframe.columns)
            
            # Configurar encabezados
            for column in dataframe.columns:
                treeview.heading(column, text=column)
            # Configurar el tamaño de los espacios entre elementos
            treeview.column("#0", minwidth=0, width=40, stretch=tk.NO)  # Espacio entre el ícono y el texto

            for column in dataframe.columns:
                treeview.column(column, minwidth=0, width=100, stretch=tk.NO)  # Espacio entre las columnas
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
    """
    Crea dinámicamente Checkbuttons para las variables independientes y Radiobuttons para la variable objetivo.

    """
    # Leer las columnas desde el archivo
    # Cambia 'ruta/del/archivo.csv' con la ruta correcta de tu archivo
    global estados_checkbuttons, opcion_seleccionada,columnas 
    canvas = tk.Canvas(frame_grafica,bg=fondo,highlightthickness=0)
    canvas.pack(expand=True, fill='both')

    # Crear un frame en el lienzo
    frame_canvas = tk.Frame(canvas,bg=fondo)
    canvas.create_window((0, 0), window=frame_canvas, anchor=tk.NW)
    
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
    boton_guardar = tk.Button(frame_but2, text="GUARDAR MODELO", command=mostrar_ventana_entrada)
    boton_guardar.grid(row=2,column=6,pady=3,padx=5)

def mostrar_descripcion(descripcion):
    """
    Muestra la descripción del modelo en la interfaz gráfica.

    Parameters:
    - descripcion (str): La descripción del modelo.

    """
    global ventana,frame_grafica

    frame_descripcion=tk.Frame(ventana,padx=5,pady=5)
    frame_descripcion.pack()
    feliznavidadalberto=tk.Label(frame_grafica,text='DESCRIPCIÓN DEL MODELO:')
    feliznavidadalberto.pack()
    felizanoalberto=tk.Label(frame_grafica,text=descripcion,padx=10)
    felizanoalberto.pack()

def mostrar_prediccion(reg_model,variable_obj):
    """
    Obtiene y muestra la predicción del modelo basándose en las entradas proporcionadas por el usuario.

    Parameters:
    - reg_model: El modelo de regresión.
    -variable_obj(str):nombre de la variable objeto

    """

    # Obtener la predicción
    prediccion = obtener_y_mostrar_contenido(reg_model,contenido_cajas)

    # Mostrar la predicción en tu interfaz gráfica
    etiqueta_prediccion.config(text=f"La predicción de {variable_obj} es: {prediccion}")
    
def predicciones(list_vi, reg_model,variable_obj):
    """
    Crea cajas de entrada dinámicamente para las variables independientes y muestra la predicción.

    Parameters:
    - list_vi (list): Lista de variables independientes.
    - reg_model: El modelo de regresión.
    -variable_obj(str):nombre de la variable objeto

    """
    # Declarar variables globales necesarias
    global my_canvas, contenido_cajas, etiqueta_prediccion

    contenido_cajas = []
    # Crear un marco secundario en el lienzo con el scroll configurado

    my_canvas,second_frame = configurar_scroll_horizontal(frame_predicciones)

    j = 0

    # Crear etiquetas y entradas para cada elemento en la lista de variables
    for i in list_vi:
        nombre = tk.Label(second_frame, text=str(i))
        nombre.grid(column=j, row=0, padx=4)
        j += 1
        entrada_texto = tk.Entry(second_frame, state='normal')
        entrada_texto.grid(column=j, row=0, padx=4)
        j += 1
        # Agregar la caja de entrada a la lista
        contenido_cajas.append(entrada_texto)

    # Configurar la ventana en el lienzo y vincular la función de configuración
    configurar_marco_scroll(my_canvas,second_frame)

    # Obtener la posición de la última caja para posicionar el botón y la etiqueta
    ultima_caja_coords = contenido_cajas[-1].winfo_geometry().split('+')
    x_pos_ultima_caja = int(ultima_caja_coords[1]) + contenido_cajas[-1].winfo_x()

    # Botón para obtener y mostrar el contenido actual
    boton_obtener_contenido = tk.Button(frame_predicciones, text="Obtener Predicción", command=lambda: mostrar_prediccion(reg_model,variable_obj))
    boton_obtener_contenido.place(x=x_pos_ultima_caja + 20, y=int(ultima_caja_coords[2]) + 60)

    # Etiqueta para mostrar la predicción
    etiqueta_prediccion = tk.Label(frame_predicciones, text="")
    etiqueta_prediccion.place(x=x_pos_ultima_caja + 40 + boton_obtener_contenido.winfo_reqwidth(), y=int(ultima_caja_coords[2]) + 60)

def cerrar_ventana():
    """
    Cierra la ventana principal de la aplicación.

    """
    ventana.destroy()
    sys.exit()

# Crear ventana y otros elementos
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
fondo=ventana.cget('bg')
frame_grafica = tk.Frame(ventana,width=600, height=300,bg=fondo)
frame_grafica.pack(padx=50)

#Crear Frame para predicciones
frame_predicciones=tk.Frame(ventana,padx=5,pady=5)
frame_predicciones.pack(fill="both", expand=True)

ventana.mainloop()
