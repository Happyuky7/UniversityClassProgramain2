import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data = pd.read_csv('data_real_t.csv')
pd.set_option('display.max_rows', None)

Tiempo = Data['Tiempo [s]']
Temperatura = Data['Temperatura [°C]']
Turbidez = Data['Turbidez [NTU]']

plt.plot(Tiempo, Turbidez, color='blue')

plt.legend(['Turbidez'], loc='upper left')

plt.xlabel('Tiempo [s]')
plt.ylabel('Turbidez [NTU]')
plt.title('Mi primer gráfico con data en Pandas')
plt.grid(True)
plt.xlim(2800, 3000)

plt.show()