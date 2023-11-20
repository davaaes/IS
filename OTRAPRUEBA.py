from tkinter import *
from tkinter import filedialog

arvhivo_seleccionado=None


ventana_principal = Tk()
ventana_principal.geometry('900x600')
ventana_principal.title('PRÁCTICA IS')


def cargarArchivo():
    global archivo_seleccionado

    archivo_seleccionado = filedialog.askopenfilename()
#DOS FUNCIONES PARA LLAMAR A LA REGRESIÓN SIMPLE O MÚLTIPLE 
def salir():
    salta.destroy()
    
    
def regresion_simple():
    global salta,v_objetivo,intopcion,v_independiente,intchk,opcion1,opcion2,opcion3,opcion8,opcion4,opcion5,opcion6,opcion7,opcion9,botonmostrar

    v_independiente=[]
    v_objetivo=[]
    if intopcion.get()==1:
        v_independiente.append('longitud')
    elif intopcion.get()==2:
        v_independiente.append('latitude')
    elif intopcion.get()==3:
        v_independiente.append('housing_median_age')
    elif intopcion.get()==4:
        v_independiente.append('total_rooms')
    elif intopcion.get()==5:
        v_independiente.append('total_bedrooms')
    elif intopcion.get()==6:
        v_independiente.append('population')
    elif intopcion.get()==7:
        v_independiente.append('households')
    elif intopcion.get()==8:
        v_independiente.append('median_income')
    elif intopcion.get()==9:
        v_independiente.append('median_house_value')
    else:
        salta=Toplevel(miFrame)
        salta.title('ERROR')
        salta.geometry('200x200')
        etiqueta=Label(salta,text='NO HA \n SELECCIONADO NINGÚNA \n VARIABLE INDEPENDIENTE')
        etiqueta.pack(padx=20,pady=20)
        boton1=Button(salta,text='Aceptar',command=salir)
        boton1.pack(pady=20)
        
    if intchk.get()==1:
        v_objetivo.append('longitud')
    elif intchk.get()==2:
        v_objetivo.append('latitude')
    elif intchk.get()==3:
        v_objetivo.append('housing_median_age')
    elif intchk.get()==4:
        v_objetivo.append('total_rooms')
    elif intchk.get()==5:
        v_objetivo.append('total_bedrooms')
    elif intchk.get()==6:
        v_objetivo.append('population')
    elif intchk.get()==7:
        v_objetivo.append('households')
    elif intchk.get()==8:
        v_objetivo.append('median_income')
    elif intchk.get()==9:
        v_objetivo.append('median_house_value')
    else:
        salta=Toplevel(miFrame)
        salta.title('ERROR')
        salta.geometry('200x200')
        etiqueta=Label(salta,text='NO HA \n SELECCIONADO NINGÚNA \n VARIABLE OVJETIVO')
        etiqueta.pack(padx=20,pady=20)
        boton1=Button(salta,text='Aceptar',command=salir)
        boton1.pack(pady=20)
def regresion_multiple():
    global salta,v_objetivo,intopcion,v_independiente,intchk,opcion1,opcion2,opcion3,opcion8,opcion4,opcion5,opcion6,opcion7,opcion9,botonmostrar

    v_independiente=[]
    v_objetivo=[]
    if intopcion.get()==1:
        v_independiente.append('longitud')
    elif intopcion.get()==2:
        v_independiente.append('latitude')
    elif intopcion.get()==3:
        v_independiente.append('housing_median_age')
    elif intopcion.get()==4:
        v_independiente.append('total_rooms')
    elif intopcion.get()==5:
        v_independiente.append('total_bedrooms')
    elif intopcion.get()==6:
        v_independiente.append('population')
    elif intopcion.get()==7:
        v_independiente.append('households')
    elif intopcion.get()==8:
        v_independiente.append('median_income')
    elif intopcion.get()==9:
        v_independiente.append('median_house_value')
    else:
        salta=Toplevel(miFrame)
        salta.title('ERROR')
        salta.geometry('200x200')
        etiqueta=Label(salta,text='NO HA \n SELECCIONADO NINGÚNA \n VARIABLE INDEPENDIENTE')
        etiqueta.pack(padx=20,pady=20)
        boton1=Button(salta,text='Aceptar',command=salir)
        boton1.pack(pady=20)
        
    if intchk.get()==1:
        v_objetivo.append('longitud')
    elif intchk.get()==2:
        v_objetivo.append('latitude')
    elif intchk.get()==3:
        v_objetivo.append('housing_median_age')
    elif intchk.get()==4:
        v_objetivo.append('total_rooms')
    elif intchk.get()==5:
        v_objetivo.append('total_bedrooms')
    elif intchk.get()==6:
        v_objetivo.append('population')
    elif intchk.get()==7:
        v_objetivo.append('households')
    elif intchk.get()==8:
        v_objetivo.append('median_income')
    elif intchk.get()==9:
        v_objetivo.append('median_house_value')
    else:
        salta=Toplevel(miFrame)
        salta.title('ERROR')
        salta.geometry('200x200')
        etiqueta=Label(salta,text='NO HA \n SELECCIONADO NINGÚNA \n VARIABLE OVJETIVO')
        etiqueta.pack(padx=20,pady=20)
        boton1=Button(salta,text='Aceptar',command=salir)
        boton1.pack(pady=20)
#HACER LAS DOS NUEVAS VENTANAS
def simple():
    global miFrame,intopcion,intchk,chk1,chk2,chk3,chk4,chk5,chk6,chk7,chk8,chk9,opcion1,opcion2,opcion3,opcion8,opcion4,opcion5,opcion6,opcion7,opcion9,botonmostrar
    # Función que se ejecutará al hacer clic en el primer botón
    ventana_principal.destroy()  # Cierra la ventana actual
    nueva_ventana = Tk()  # Crea una nueva ventana
    nueva_ventana.title("Nueva Pantalla")  # Asigna un título a la n
    etiqueta = Label(nueva_ventana, text='ESCOGISTE REGRESIÓN SIMPLE')
    etiqueta.pack(padx=20, pady=20)
    nueva_ventana.geometry('900x600')
    

    miFrame = Frame(nueva_ventana)
    miFrame.pack(expand=True)


    botonArchivo=Button(miFrame,text='CARGAR ARCHIVO',command=cargarArchivo)
    botonArchivo.grid(row=3, column=1, padx=70,pady=10)



    intchk=IntVar()
    chk=Label(miFrame,text='VARIABLE INDEPENDIENTE')
    chk.grid(row=0,column=0,padx=70,pady=10)
    chk1=Radiobutton(miFrame,text='longitude',variable=intchk,value=1).grid(row=1, column=0, padx=70,pady=10)
    chk2=Radiobutton(miFrame,text='latitude',variable=intchk,value=2).grid(row=2, column=0, padx=70,pady=10)
    chk3=Radiobutton(miFrame,text='housing_median_age',variable=intchk,value=3).grid(row=3, column=0, padx=70,pady=10)
    chk4=Radiobutton(miFrame,text='total_rooms',variable=intchk,value=4).grid(row=4, column=0, padx=70,pady=10)
    chk5=Radiobutton(miFrame,text='total_bedrooms',variable=intchk,value=5).grid(row=5, column=0, padx=70,pady=10)
    chk6=Radiobutton(miFrame,text='population',variable=intchk,value=6).grid(row=6, column=0, padx=70,pady=10)
    chk7=Radiobutton(miFrame,text='households',variable=intchk,value=7).grid(row=7, column=0, padx=70,pady=10)
    chk8=Radiobutton(miFrame,text='median_income',variable=intchk,value=8).grid(row=8, column=0, padx=70,pady=10)
    chk9=Radiobutton(miFrame,text='median_house_value',variable=intchk,value=9).grid(row=9, column=0, padx=70,pady=10)

    intopcion=IntVar()
    opcion=Label(miFrame,text='VARIABLE OBJETIVO')
    opcion.grid(row=0,column=2,padx=70,pady=10)
    opcion1=Radiobutton(miFrame,text='longitude',variable=intopcion,value=1).grid(row=1, column=2, padx=70,pady=10)
    opcion2=Radiobutton(miFrame,text='latitude',variable=intopcion,value=2).grid(row=2, column=2, padx=70,pady=10)
    opcion3=Radiobutton(miFrame,text='housing_median_age',variable=intopcion,value=3).grid(row=3, column=2, padx=70,pady=10)
    opcion4=Radiobutton(miFrame,text='total_rooms',variable=intopcion,value=4).grid(row=4, column=2, padx=70,pady=10)
    opcion5=Radiobutton(miFrame,text='total_bedrooms',variable=intopcion,value=5).grid(row=5, column=2, padx=70,pady=10)
    opcion6=Radiobutton(miFrame,text='population',variable=intopcion,value=6).grid(row=6, column=2, padx=70,pady=10)
    opcion7=Radiobutton(miFrame,text='households',variable=intopcion,value=7).grid(row=7, column=2, padx=70,pady=10)
    opcion8=Radiobutton(miFrame,text='median_income',variable=intopcion,value=8).grid(row=8, column=2, padx=70,pady=10)
    opcion9=Radiobutton(miFrame,text='median_house_value',variable=intopcion,value=9).grid(row=9, column=2, padx=70,pady=10)
    


    botonmostrar = Button(miFrame, text='Mostrar',command=regresion_simple).grid(row=6, column=1, padx=70,pady=10)



    nueva_ventana.mainloop()
def multiple():
    global chk1,chk2,chk3,chk4,chk5,chk6,chk7,chk8,chk9,opcion1,opcion2,opcion3,opcion8,opcion4,opcion5,opcion6,opcion7,opcion9,botonmostrar
    # Función que se ejecutará al hacer clic en el primer botón
    ventana_principal.destroy()  # Cierra la ventana actual
    nueva_ventana = Tk()  # Crea una nueva ventana
    nueva_ventana.title("Nueva Pantalla")  # Asigna un título a la n
    etiqueta = Label(nueva_ventana, text='ESCOGISTE REGRESIÓN MÚLTIPLE')
    etiqueta.pack(padx=20, pady=20)
    nueva_ventana.geometry('900x600')
    
    miFrame = Frame(nueva_ventana)
    miFrame.pack(expand=True)

    botonArchivo=Button(miFrame,text='CARGAR ARCHIVO',command=cargarArchivo)
    botonArchivo.grid(row=3, column=1, padx=70,pady=10)

    intchk1=IntVar()
    intchk2=IntVar()
    intchk3=IntVar()
    intchk4=IntVar()
    intchk5=IntVar()
    intchk6=IntVar()
    intchk7=IntVar()
    intchk8=IntVar()
    intchk9=IntVar()
    chk=Label(miFrame,text='VARIABLES INDEPENDIENTES')
    chk.grid(row=0,column=0,padx=70,pady=10)
    chk1=Checkbutton(miFrame,text='longitude',variable=intchk1).grid(row=1, column=0, padx=70,pady=10)
    chk2=Checkbutton(miFrame,text='latitude',variable=intchk2).grid(row=2, column=0, padx=70,pady=10)
    chk3=Checkbutton(miFrame,text='housing_median_age',variable=intchk3).grid(row=3, column=0, padx=70,pady=10)
    chk4=Checkbutton(miFrame,text='total_rooms',variable=intchk4).grid(row=4, column=0, padx=70,pady=10)
    chk5=Checkbutton(miFrame,text='total_bedrooms',variable=intchk5).grid(row=5, column=0, padx=70,pady=10)
    chk6=Checkbutton(miFrame,text='population',variable=intchk6).grid(row=6, column=0, padx=70,pady=10)
    chk7=Checkbutton(miFrame,text='households',variable=intchk7).grid(row=7, column=0, padx=70,pady=10)
    chk8=Checkbutton(miFrame,text='median_income',variable=intchk8).grid(row=8, column=0, padx=70,pady=10)
    chk9=Checkbutton(miFrame,text='median_house_value',variable=intchk9).grid(row=9, column=0, padx=70,pady=10)

    intopcion=IntVar()
    '''''
    intopcion2=IntVar()
    intopcion3=IntVar()
    intopcion4=IntVar()
    intopcion5=IntVar()
    intopcion6=IntVar()
    intopcion7=IntVar()
    intopcion8=IntVar()
    intopcion9=IntVar()
    '''''
    opcion=Label(miFrame,text='VARIABLE OBJETIVO')
    opcion.grid(row=0,column=2,padx=70,pady=10)
    opcion1=Radiobutton(miFrame,text='longitude',variable=intopcion,value=1).grid(row=1, column=2, padx=70,pady=10)
    opcion2=Radiobutton(miFrame,text='latitude',variable=intopcion,value=2).grid(row=2, column=2, padx=70,pady=10)
    opcion3=Radiobutton(miFrame,text='housing_median_age',variable=intopcion,value=3).grid(row=3, column=2, padx=70,pady=10)
    opcion4=Radiobutton(miFrame,text='total_rooms',variable=intopcion,value=4).grid(row=4, column=2, padx=70,pady=10)
    opcion5=Radiobutton(miFrame,text='total_bedrooms',variable=intopcion,value=5).grid(row=5, column=2, padx=70,pady=10)
    opcion6=Radiobutton(miFrame,text='population',variable=intopcion,value=6).grid(row=6, column=2, padx=70,pady=10)
    opcion7=Radiobutton(miFrame,text='households',variable=intopcion,value=7).grid(row=7, column=2, padx=70,pady=10)
    opcion8=Radiobutton(miFrame,text='median_income',variable=intopcion,value=8).grid(row=8, column=2, padx=70,pady=10)
    opcion9=Radiobutton(miFrame,text='median_house_value',variable=intopcion,value=9).grid(row=9, column=2, padx=70,pady=10)
    




    botonmostrar = Button(miFrame, text='Mostrar').grid(row=6, column=1, padx=70,pady=10)

    nueva_ventana.mainloop()



def mostrar_pantalla(mensaje):
    # Función que muestra la segunda pantalla
    nueva_ventana = Tk()  # Crea una nueva ventana
    nueva_ventana.title("Nueva Pantalla")  # Asigna un título a la n
    etiqueta = Label(nueva_ventana, text=mensaje)
    etiqueta.pack(padx=20, pady=20)
    nueva_ventana.geometry('900x600')

    nueva_ventana.mainloop()



# Crear los botones en la ventana principal
marco_central = Frame(ventana_principal)
marco_central.pack(expand=True)

lineal = Button(marco_central, text="REGRESIÓN LINEAL", command=simple)
lineal.pack(pady=100)

multiples = Button(marco_central, text="REGRESIÓN MÚLTIPLE", command=multiple)
multiples.pack(pady=100)

ventana_principal.mainloop()