import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('flights.csv')
print(df.head())

mn_pas = df['passengers'].mean()
std_pas = df['passengers'].std()

print(f'El promedio es: {mn_pas}')
print(f'La desviación estándar es: {std_pas}')

df['outlier'] = 0
print(df.head(1))

for index, serie_row in df.iterrows():
    if (serie_row['passengers'] > mn_pas + std_pas) or (serie_row['passengers'] < mn_pas - std_pas):
        df.at[index, 'outlier'] = 1

print(df['outlier'].value_counts())
print(df['outlier'].value_counts('%'))

df3 = pd.DataFrame({
    'name': ['John', 'Mike', 'Sara'],
    'age': [25, 30, 35],
    'gender': ['M', 'M', 'F']
})

print(df3)

df3.set_index('name', inplace=True)
print(df3)

print(df3.loc[['John', 'Sara'], ['age', 'gender']])

#print(df3.loc[0])

print(df[df['outlier'] == 1])

print(df.loc[df['outlier'] == 1])

AA = df.loc[df['outlier'] == 1, 'month'].value_counts()

print('Los tipos clasificados son los siguientes meses: ')
print(AA)