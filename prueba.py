import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import lector as l

# Función de regresión
def regresion(columna_indep, columnas_dep, df, name=None):
    df = df.dropna()
    indep_v = df[columna_indep].values
    x = len(columnas_dep)
    dep_v = [df[col].values for col in columnas_dep]
    X1 = np.array(dep_v).T
    Y1 = np.array(indep_v)
    reg = LinearRegression()
    reg = reg.fit(X1, Y1)
    y_pred = reg.predict(X1)
    error = np.sqrt(mean_squared_error(Y1, y_pred))
    r2 = reg.score(X1, Y1)
    print("-" * 36)
    print("Error sin raíz: %.3f" % mean_squared_error(Y1, y_pred))
    print("-" * 36)
    print("Error : ", error)
    print("-" * 36)
    print("r2 es : ", r2)
    print("-" * 36)
    coef = reg.coef_
    interc = "{:.4f}".format(reg.intercept_[0])
    for i in range(len(coef[0])):
        print("Beta ", str(i + 1), " =", "{:.8f}".format(coef[0][i]))
        coef[0][i] = "{:.8f}".format(coef[0][i])
    print("-" * 36)
    print('Término independiente: ', interc)
    print("-" * 36)

    if len(columnas_dep) == 1:
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.scatter(X1, Y1, label='Datos', s=10)
        ax.plot(X1, y_pred, color='red', label='Línea de regresión')
        ax.set_xlabel(str(columna_indep[0]).upper())
        ax.set_ylabel(str(columnas_dep[0]).upper())
        leyend = "Y = " + "(" + str(coef[0][0]) + ")" + "*x1 + " + "(" + str(interc) + ")"
        ax.legend(title=leyend, title_fontsize=8)
        ax.set_title('Regresión Lineal Simple')

        if name is not None:
            fig.savefig(name)
        else:
            return fig

    elif len(columnas_dep) == 2:
        fig = Figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(dep_v[0], dep_v[1], Y1, c='r', marker='o')
        ax.set_xlabel((str(columnas_dep[0])).upper())
        ax.set_ylabel((str(columnas_dep[1])).upper())
        ax.set_zlabel((str(columna_indep[0])).upper())

        x10_range = np.linspace(min(dep_v[0]), max(dep_v[0]), 10)
        x11_range = np.linspace(min(dep_v[1]), max(dep_v[1]), 10)
        x1_mesh, x2_mesh = np.meshgrid(x10_range, x11_range)
        y_pred = reg.predict(np.vstack((x1_mesh.ravel(), x2_mesh.ravel())).T)
        y_pred = y_pred.reshape(x1_mesh.shape)
        ax.plot_surface(x1_mesh, x2_mesh, y_pred, alpha=0.5)
        leyend = "Y = " + "(" + str(coef[0][0]) + ")" + "*x1 + " + "(" + str(coef[0][0]) + ")" + "*x2 +" + "(" + str(
            interc) + ")"
        ax.legend(loc=9, title_fontsize=8, title=leyend)

        if name is not None:
            fig.savefig(name)
        else:
            return fig

# Función para plotear gráfico en Tkinter
def plot_grafico(columna_indep, columnas_dep, df, name=None):
    # Obtiene los datos para graficar desde la función de regresión
    fig = regresion(columna_indep, columnas_dep, df, name)

    # Crea el lienzo de Tkinter para la figura de Matplotlib
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

# Crea la ventana principal
ventana = tk.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
ventana.title("Interfaz con Gráfico")

# Función que se llama cuando se presiona el botón
def generar_grafico():
    # Selecciona las columnas para la regresión y el nombre del archivo (si es necesario)
    columna_indep = ["latitude"]
    columnas_dep = ["latitude",'longitude']
    df = l.leer_archivo("housing.xlsx")
    name = None

    # Llama a la función para graficar
    plot_grafico(columna_indep, columnas_dep, df, name)

# Agrega un botón para generar la gráfica
boton_grafico = tk.Button(ventana, text="Generar Gráfico", command=generar_grafico)
boton_grafico.pack(side=tk.TOP)  # Ubicado en la parte superior

# Ejecuta el bucle principal de la interfaz
ventana.mainloop()

