"""
Cargar base de datos flights.csv


- Cargar las librerias necesarias para realizar su analisis
- Mostrar las primeras 5 entradas
- Mostras las ultimas 5 entradas
- Utilizar discribe para la columna year
- Almacenar en variables independientes los primeros 15 y los ultimos 15 en datos, usar concat para agurpar las variables en una sola
- Solicite la media, mediana y desviación estandar de la cantidad de pasajeros utilixando los metodos de numpy, replique el procedimiento 
  para las ultimas y primeras 15 observaciones, comente brevemente los resultados
- Comente sus resultados



Importante, subir un jupyter en formato ipynb
"""



import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pf = pd.read_csv('flights.csv')

print(pf)

passengers = pf['passengers']
years = pf['year']

plt.title('Cantidad de pasajeros por año')
plt.bar(years, passengers, label='Pasajeros', color='lightgreen')
plt.xlabel('Año')
plt.ylabel('Cantidad de pasajeros')
plt.grid(True)
plt.legend(title='Simbologia:')
plt.show()


print(pf.head(5))

print(pf.tail(5))

# La función describe() en pandas se utiliza para generar estadísticas descriptivas que resumen la tendencia central,
# la dispersión y la forma de la distribución de un conjunto de datos, excluyendo los valores NaN.

# Parámetros:
# - percentiles: Lista de números (opcional). Los percentiles a incluir en la salida. Todos deben estar entre 0 y 1.
#   El valor predeterminado es [.25, .5, .75], que devuelve los percentiles 25, 50 y 75.
# - include: 'all', lista de tipos de datos o None (opcional). Especifica los tipos de datos a incluir en el resultado.
#   Las opciones son:
#   - 'all': Incluye todas las columnas del DataFrame.
#   - Lista de tipos de datos: Limita los resultados a los tipos de datos proporcionados.
#   - None (predeterminado): Incluye todas las columnas numéricas.
# - exclude: Lista de tipos de datos o None (opcional). Especifica los tipos de datos a excluir del resultado.

# Retorno:
# - Series o DataFrame: Devuelve estadísticas resumidas del objeto Series o DataFrame proporcionado.

# Ejemplos:
# 1. Describir una Serie numérica:
#    s = pd.Series([1, 2, 3])
#    s.describe()
#    Salida:
#    count    3.0
#    mean     2.0
#    std      1.0
#    min      1.0
#    25%      1.5
#    50%      2.0
#    75%      2.5
#    max      3.0
#    dtype: float64

# 2. Describir un DataFrame:
#    df = pd.DataFrame({
#        'categorical': pd.Categorical(['d', 'e', 'f']),
#        'numeric': [1, 2, 3],
#        'object': ['a', 'b', 'c']
#    })
#    df.describe()
#    Salida:
#           numeric
#    count      3.0
#    mean       2.0
#    std        1.0
#    min        1.0
#    25%        1.5
#    50%        2.0
#    75%        2.5
#    max        3.0

# En este código, se está llamando a describe() en la columna 'year' del DataFrame pf,
# lo que generará estadísticas descriptivas para esa columna específica.
print(pf['year'].describe())

datos = pd.concat([pf.head(15), pf.tail(15)])
print(datos)

media_pasajeros = np.mean(datos['passengers'])
mediana_pasajeros = np.median(datos['passengers'])
desviacion_pasajeros = np.std(datos['passengers'])

print(f'La media de pasajeros es: {media_pasajeros}')
print(f'La mediana de pasajeros es: {mediana_pasajeros}')
print(f'La desviación estandar de pasajeros es: {desviacion_pasajeros}')



media_pasajeros_primeros_15 = np.mean(pf.head(15)['passengers'])
mediana_pasajeros_primeros_15 = np.median(pf.head(15)['passengers'])
desviacion_pasajeros_primeros_15 = np.std(pf.head(15)['passengers'])

print(f'La media de pasajeros de los primeros 15 es: {media_pasajeros_primeros_15}')
print(f'La mediana de pasajeros de los primeros 15 es: {mediana_pasajeros_primeros_15}')
print(f'La desviación estandar de pasajeros de los primeros 15 es: {desviacion_pasajeros_primeros_15}')

media_pasajeros_ultimos_15 = np.mean(pf.tail(15)['passengers'])
mediana_pasajeros_ultimos_15 = np.median(pf.tail(15)['passengers'])
desviacion_pasajeros_ultimos_15 = np.std(pf.tail(15)['passengers'])

print(f'La media de pasajeros de los ultimos 15 es: {media_pasajeros_ultimos_15}')
print(f'La mediana de pasajeros de los ultimos 15 es: {mediana_pasajeros_ultimos_15}')
print(f'La desviación estandar de pasajeros de los ultimos 15 es: {desviacion_pasajeros_ultimos_15}')

# Datos en graficos
plt.plot(datos['passengers'])
plt.show()



# Results:
# La media de pasajeros es: 228.4
# La mediana de pasajeros es: 229.0
# La desviación estandar de pasajeros es: 71.307262569542
# La media de pasajeros de los primeros 15 es: 126.8
# La mediana de pasajeros de los primeros 15 es: 126.0
# La desviación estandar de pasajeros de los primeros 15 es: 13.663820841916802
# La media de pasajeros de los ultimos 15 es: 336.4
# La mediana de pasajeros de los ultimos 15 es: 337.0
# La desviación estandar de pasajeros de los ultimos 15 es: 49.36708157329535

# La media de pasajeros es mayor en los ultimos 15 observaciones, la mediana es mayor 
# en los primeros 15 observaciones y la desviación estandar es mayor en los primeros 15 observaciones
