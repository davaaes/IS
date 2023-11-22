import sklearn as sk 
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D 
from lector import *


def regresion(columna_indep,columnas_dep,df):

    df= leer_archivo(df)

    df = df.replace(np.nan,0)

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
    print("-"*36)
    print("Error sin raíz: %.3f" % mean_squared_error(Y1, y_pred))
    print("-"*36)
    print("Error : ", error)
    print("-"*36)
    print("r2 es : ", r2)
    print("-"*36)


    coef = reg.coef_
    interc ="{:.4f}".format(reg.intercept_[0])
    
    for i  in range(len(coef[0])):
        print("Beta " , str(i+1) ," =","{:.8f}".format(coef[0][i]))
        coef[0][i] = "{:.8f}".format(coef[0][i])
    print("-"*36)
    print('Término independiente: ', interc)
    print("-"*36)
    


    if len(columnas_dep) == 1 :
        fig =plt.figure()
        plt.scatter(X1, Y1, label='Datos' , s = 10)
        plt.plot(X1, y_pred, color='red', label='Línea de regresión')
        plt.xlabel(str(columna_indep[0]).upper())
        plt.ylabel(str(columnas_dep[0]).upper())
        leyend = "Y = "+ "(" + str(coef[0][0]) + ")" + "*x1 + " + "(" + str(interc) + ")"
        plt.legend(title = leyend,title_fontsize =8    )
        plt.title('Regresión Lineal Simple')
        return fig
        

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
        leyend = "Y = "+ "(" +str(  coef[0][0] ) + ")"+"*x1 + " + "(" + str(  coef[0][0]  ) +")" +"*x2 +"+"("  + str(   interc  ) + ")"
        ax.legend(loc = 9,title_fontsize = 8 , title = leyend  )
        return fig

    elif len(columnas_dep) > 2:
        
        formul = "Y = "
        for i in range(len(coef[0])):
            formul += ("(" + str(coef[0][i])+")" + "*x" + str(i+1) + " + ") 
        formul += "("  + str(   interc  ) + ")"
        print("Fórmula: \n",formul)
        print("-"*36)
            
    

archivo = "housing.db"
c_i = ["total_bedrooms"]

c_ds = ["total_bedrooms","longitude"]

regresion(c_i,c_ds,archivo)
plt.show()