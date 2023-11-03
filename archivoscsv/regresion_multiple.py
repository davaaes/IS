import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def regresion_lineal():
    data = pd.read_csv("housingcsv.csv")

    # Definir la variable independiente (característica) y la variable dependiente (target)
    X = data[['median_income']]
    y = data['total_rooms']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un modelo de regresión lineal simple
    model = LinearRegression()

    # Ajustar el modelo a los datos de entrenamiento
    model.fit(X_train, y_train)

    # Hacer predicciones en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Calcular el error cuadrático medio (MSE) en el conjunto de prueba
    mse = mean_squared_error(y_test, y_pred)
    print(f"Error cuadrático medio: {mse}")

    # Graficar los puntos de datos y la línea de regresión
    plt.scatter(X_test, y_test, label='Datos reales')
    plt.plot(X_test, y_pred, color='red', label='Línea de regresión')
    plt.xlabel('Median Income')
    plt.ylabel('total_rooms')
    plt.legend()
    plt.title('Regresión Lineal Simple')
    plt.show()



def regresion_multiple():
    # Carga de datos desde un archivo CSV
    datos = pd.read_csv("housingcsv.csv")

    # Variables independientes y variable target
    X = datos[['latitude', 'housing_median_age']]
    y = datos['median_income']  # Variable target

    # División de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creación y entrenamiento del modelo de regresión lineal
    modelo = linear_model.LinearRegression()
    modelo.fit(X_train, y_train)

    # Predicciones con el modelo entrenado
    print(X_test)
    y_pred = modelo.predict(X_test)

    # Coeficientes e intercepto del modelo
    print('Coeficientes:', modelo.coef_)
    print('Intercepto:', modelo.intercept_)

    # Métricas de evaluación del modelo
    print('Error cuadrático medio (MSE): %.2f' % mean_squared_error(y_test, y_pred))
    print('Coeficiente de determinación (R^2): %.2f' % r2_score(y_test, y_pred))
    plt.figure(figsize=(8, 6))

    # Graficar los datos reales de test
    plt.scatter(X_test['latitude'], y_test, label='Datos reales')

    # Graficar la predicción del modelo
    plt.scatter(X_test['latitude'], y_pred, color='red', label='Predicciones')

    plt.xlabel('Latitud')
    plt.ylabel('Income')
    plt.legend()
    plt.title('Modelo de Regresión Múltiple')

    plt.show()

regresion_lineal()
regresion_multiple()




