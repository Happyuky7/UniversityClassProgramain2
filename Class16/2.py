import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('MrBeast_youtube_stats.csv')

print(df.head())

print(df.shape)

print(df.dtypes)

print(df.columns)

print(df.describe())

print(df.info())