import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv("housing.csv")

# Definir la variable independiente (característica) y la variable dependiente (target)
X = data[['median_income']]
y = data['median_house_value']

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
plt.ylabel('Median House Value')
plt.legend()
plt.title('Regresión Lineal Simple')
plt.show()