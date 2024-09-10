import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
print(df.head())
print(df.tail())

plt.bar(df.year, df.passengers)
plt.show()

df['passengers'][df['passengers'] > 500]

plt.hist(df['passengers'], bins=20)
plt.show()