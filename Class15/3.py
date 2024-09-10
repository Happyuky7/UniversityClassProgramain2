import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data = pd.read_csv('alumnos.csv')
print(Data.head())
print(Data.tail())
print(Data[2:5])
print(Data.shape)
print(Data[:3])
print(Data[16:])
print(Data[3:8])
print(Data[3:5])
print(Data.columns)
print(Data.peso)
print(Data['peso'])
print(Data.peso[1])