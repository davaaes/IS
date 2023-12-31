import tkinter as tk
from tkinter import ttk
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import joblib


class Modelo:
    def __init__(self):
        # Inicializa el modelo como None
        self.modelo = None

    def entrenar_modelo(self, columna_indep, columnas_dep,descripcion, df):
        """
        Entrena un modelo de regresión lineal con los datos proporcionados.

        Parameters:
        - columna_indep (str): Nombre de la columna independiente.
        - columnas_dep (list): Lista de nombres de las columnas dependientes.
        - descripcion (str): Descripción del modelo.
        - df (pandas.DataFrame): DataFrame que contiene los datos.

        Returns:
        tuple: Tupla con el modelo entrenado, la figura, el error, la fórmula, el intercepto, los coeficientes , las columnas dependientes y la independiente.
        """
        reg, fig, error, formula, interc, coef, columna_dep,columna_indep = regresion(columna_indep, columnas_dep, df)
        # Almacena el modelo y otros resultados relevantes
        self.modelo = (reg, fig, error, formula, interc, coef, columna_dep, descripcion,columna_indep)
        return self.modelo

    def predecir(self, X):
        """
        Realiza predicciones utilizando el modelo entrenado.

        Parameters:
        - X (numpy.ndarray): Datos para hacer predicciones.

        Returns:
        numpy.ndarray: Predicciones del modelo.
        """
        if self.modelo is not None:
            return self.modelo[0].predict(X)
        else:
            raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")

    def guardar_modelo(self, path):
        """
        Guarda el modelo en un archivo utilizando joblib.

        Parameters:
        - path (str): Ruta donde se guardará el modelo.
        """
        if self.modelo is not None:
            joblib.dump(self.modelo, path)
        else:
            raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")

    def cargar_modelo(self, path):
        """
        Carga el modelo desde un archivo utilizando joblib.

        Parameters:
        - path (str): Ruta desde la cual se carga el modelo.

        Returns:
        object: Modelo cargado.
        """
        try:
            # Carga el modelo desde el archivo
            modelo_cargado = joblib.load(path)
            self.modelo = modelo_cargado
            print("Modelo cargado correctamente. Tipo de objeto:", type(self.modelo))
            return self.modelo
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            return None  # Asegúrate de retornar None si hay un error

    def obtener_coeficientes(self):
        """
        Obtiene los coeficientes de la regresión.

        Returns:
        tuple: Tupla con los coeficientes y el intercepto.
        """
        if self.modelo is not None:
            error, formula = self.modelo[2], self.modelo[3]
            return formula.coef_, formula.intercept_
        else:
            raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")


def regresion(columna_indep, columnas_dep, df, name=None):
    """
    Realiza la regresión lineal y genera gráficos.

    Parameters:
    - columna_indep (str): Nombre de la columna independiente.
    - columnas_dep (list): Lista de nombres de las columnas dependientes.
    - df (pandas.DataFrame): DataFrame que contiene los datos.
    - name (str, optional): Nombre del archivo para guardar el gráfico.

    Returns:
    tuple: Tupla con el modelo, la figura, el error, la fórmula, el intercepto, los coeficientes y las columnas dependientes.
    """
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
    
    # Imprimir métricas de regresión
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
        # Gráfico para la regresión lineal simple
        fig = Figure(figsize=(3, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.scatter(X1, Y1, label='Datos', s=10)
        ax.plot(X1, y_pred, color='red', label='Línea de regresión')
        ax.set_xlabel(str(columna_indep[0]).upper())
        ax.set_ylabel(str(columnas_dep[0]).upper())
        leyend = f"{str(columna_indep)} = " + f"({str(coef[0][0])}) * {str(columnas_dep[0])} + ({str(interc)})"
        ax.set_title('Regresión Lineal Simple')

        # Guardar el gráfico si se especifica un nombre
        if name is not None:
            fig.savefig(name)
        else:
            return reg, fig, error, leyend, interc, coef, columnas_dep,columna_indep

    elif len(columnas_dep) == 2:
        # Gráfico para la regresión lineal múltiple (2D)
        fig = Figure(figsize=(3, 2), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(dep_v[0], dep_v[1], Y1, c='r', marker='o')
        ax.set_xlabel((str(columnas_dep[0])).upper())
        ax.set_ylabel((str(columnas_dep[1])).upper())
        ax.set_zlabel((str(columna_indep[0])).upper())

        # Superficie de la regresión
        x10_range = np.linspace(min(dep_v[0]), max(dep_v[0]), 10)
        x11_range = np.linspace(min(dep_v[1]), max(dep_v[1]), 10)
        x1_mesh, x2_mesh = np.meshgrid(x10_range, x11_range)
        y_pred = reg.predict(np.vstack((x1_mesh.ravel(), x2_mesh.ravel())).T)
        y_pred = y_pred.reshape(x1_mesh.shape)
        ax.plot_surface(x1_mesh, x2_mesh, y_pred, alpha=0.5)
        leyend = f"{str(columna_indep)} = " + f"({str(coef[0][0])}) * {str(columnas_dep[0])} + ({str(coef[0][1])}) * {str(columnas_dep[1])} + ({str(interc)})"

        
        # Guardar el gráfico si se especifica un nombre
        if name is not None:
            fig.savefig(name)
        else:
            return reg, fig, error, leyend, interc, coef, columnas_dep,columna_indep
    elif len(columnas_dep) > 2:
        # Gráficos para la regresión lineal múltiple (más de 2D)
        fig, axs = plt.subplots(1, len(columnas_dep), figsize=(3 * len(columnas_dep), 2))
        
        # Crear la fórmula de la regresión
        formul = f"{str(columna_indep)} = " + " + ".join([f"({str(coef[0][i])}) * {str(columnas_dep[i])}" for i in range(len(coef[0]))]) + f" + ({str(interc)})"


        def f(n,coef,intercept):
            x = 0
            for i in range(len(n)):
                x += n[i] * coef[0][i]
            x += intercept
            return x

        # Configurar datos para la visualización
        l = [0] * len(coef[0])
        
        y1 = np.linspace(min(Y1),max(Y1),len(Y1))
        
        for i in range(len(l)):
            l[i] = y1
            z_values = f(l,coef,reg.intercept_[0])
            axs[i].plot(y1,z_values)
            title = "GRÁFICO " + str(i) + ": " + (str(columnas_dep[i]).upper()) + " y " + (str(columna_indep[0]).upper())
            axs[i].set_title(title,fontsize = 6)
            l[i] = 0
            
        plt.tight_layout()
        plt.subplots_adjust(hspace = 0.5)
        
        # Guardar el gráfico si se especifica un nombre
        if name is not None:
            fig.savefig(name)
        return reg, fig, error, formul, interc, coef, columnas_dep,columna_indep