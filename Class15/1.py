import pandas as pd

Data = pd.read_csv('data_real_t.csv')

print(Data)

pd.set_option('display.max_rows', None)

print(Data)