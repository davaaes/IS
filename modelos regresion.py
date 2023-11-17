

import sklearn as sk 
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D 


def regresion(columna_indep,columnas_dep,archivo):

    if archivo.endswith('.csv'):
        df = pd.read_csv(archivo)
    elif archivo.endswith('.xlsx'):
        df = pd.read_excel(archivo)

    indep_v = df[columna_indep].values

    x = len(columnas_dep)
    dep_v = []
    for i in range(x):
        valores = df[columnas_dep[i]].values
        dep_v.append(valores)
    
    X1 = np.array(dep_v).T
    Y1 = np.array(indep_v)


    reg = LinearRegression()

    reg = reg.fit(X1,Y1)

    y_pred = reg.predict(X1)
    

    error = np.sqrt(mean_squared_error(Y1,y_pred))
    r2 = reg.score(X1,Y1)

    print("Error sin raíz: %.3f" % mean_squared_error(Y1, y_pred))
    print("El error es: ", error)
    print("r2 es : ", r2)
    print('Coefficients: \n', reg.coef_)
    print('Independent term: \n', reg.intercept_)
    print("Mean squared error: %.3f" % mean_squared_error(Y1, y_pred))
    
   
    if len(columnas_dep) == 1 :
        plt.scatter(X1, Y1, label='Datos reales' , s = 10)
        plt.plot(X1, y_pred, color='red', label='Línea de regresión')
        plt.xlabel(str(columna_indep[0]).upper())
        plt.ylabel(str(columnas_dep[0]).upper())
        plt.legend()
        plt.title('Regresión Lineal Simple')
        plt.show()

    elif len(columnas_dep) == 2:

        fig = plt.figure()
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
        plt.show()



    
archivo = "housingcsv.csv"
columna_indep =['latitude']
columnas_dep = ['longitude','total_rooms','population']

regresion(columna_indep,columnas_dep,archivo)
