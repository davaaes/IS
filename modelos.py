import sklearn as sk 
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.figure import Figure
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D 
from lector import *
import joblib
from sklearn.impute import SimpleImputer


class Modelo:
        def __init__(self):
            self.modelo = None

        def entrenar_modelo(self, columna_indep, columnas_dep, df):
            fig,error,formula,interc,coef = regresion(columna_indep, columnas_dep, df)
            self.modelo = (error,interc,coef)
            return self.modelo
        def predecir(self, X):
            if self.modelo is not None:
                return self.modelo.predict(X)
            else:
                raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")

        def guardar_modelo(self, path):
            if self.modelo is not None:
                joblib.dump(self.modelo,path)
            else:
                raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")

        def cargar_modelo(self, path):
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
            if self.modelo is not None:
                error, formula = self.modelo
                return formula.coef_, formula.intercept_
            else:
                raise ValueError("El modelo no ha sido entrenado. Debes llamar a entrenar_modelo primero.")

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
        ax.set_title('Regresión Lineal Simple')

        if name is not None:
            fig.savefig(name)
        else:
            return fig,error,leyend,interc,coef

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

        if name is not None:
            fig.savefig(name)
        else:
            return fig,error,leyend,interc,coef
    elif len(columnas_dep) > 2:
        
        fig, axs = plt.subplots(len(columnas_dep), 1, figsize=(10, 15))
        
        formul = "Y = " 
        for i in range(len(coef[0])):
            formul += ("(" + str(coef[0][i])+")" + "*x" + str(i+1) + " + ") 
        formul += "("  + str(   interc  ) + ")"

        def f(n,coef,intercept):
            x = 0
            for i in range(len(n)):
                x += n[i] * coef[0][i]
            x += intercept
            return x

        
        l = []
        for i in range(len(coef[0])):
            l.append(0)
        
        y1 = np.linspace(min(Y1),max(Y1),len(Y1))
        print(Y1)
        print(y1)
        for i in range(len(l)):
            l[i] = y1
            z_values = f(l,coef,reg.intercept_[0])
            axs[i].plot(y1,z_values)
            title = "GRÁFICO " + str(i) + ": " + (str(columnas_dep[i]).upper()) + " y " + (str(columna_indep[0]).upper())
            axs[i].set_title(title,fontsize = 6)
            l[i] = 0
            

        plt.subplots_adjust(hspace = 0.5)
        
        if name is not None:
            fig.savefig(name)
        else:
            return fig,error,formul