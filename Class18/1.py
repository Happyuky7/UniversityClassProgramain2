# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %%
os.listdir('./NBA/')

# %%
games = pd.read_csv('./NBA/games.csv')
details = pd.read_csv('./NBA/games_details.csv', low_memory=False)
teams = pd.read_csv('./NBA/teams.csv')
players = pd.read_csv('./NBA/players.csv')
ranking = pd.read_csv('./NBA/ranking.csv')

# %%
print(f'La BBDD de detalles de juegoss tiene {details.shape[0]} filas y {details.shape[1]} columnas')
print('')
print(f'La BBDD de juegos tiene {games.shape[0]} filas y {games.shape[1]} columnas')
print('')
print(f'La BBDD de rendimiento de jugadores tiene {players.shape[0]} filas y {players.shape[1]} columnas')
print('')
print(f'La BBDD de ranking tiene {ranking.shape[0]} filas y {ranking.shape[1]} columnas')
print('')
print(f'La BBDD de equipos tiene {teams.shape[0]} filas y {teams.shape[1]} columnas')

# %%
print(details.shape[0])
print(details.shape[1])
print(games.shape[0])
print(games.shape[1])
print(players.shape[0])
print(players.shape[1])
print(ranking.shape[0])
print(ranking.shape[1])
print(teams.shape[0])
print(teams.shape[1])

# %%
games.info()

# %%
games

# %%
games.columns

# %%
games = games[
    ['GAME_DATE_EST', 'GAME_ID', 'GAME_STATUS_TEXT', 'TEAM_ID_home', 'PTS_home', 'TEAM_ID_away','PTS_away', 'HOME_TEAM_WINS']
]

# %%
games.head()

# %%
games['GAME_DATE_EST'] = pd.to_datetime(games['GAME_DATE_EST'])

# %%
games.info()

# %%
games['year'] = games['GAME_DATE_EST'].dt.year
games.head()

# %%
teams.info()

# %%
teams.head()

# %%
teams.columns

# %%
teams = teams[['TEAM_ID', 'NICKNAME', 'CITY']]
teams.head()

# %%
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': [5, 6, 7, 8]})

# %%
df1

# %%
df2

# %%
merged_df = pd.merge(df1, df2, on='key', how='inner')
merged_df

# %%
home_games = pd.merge(games, teams, left_on='TEAM_ID_home', right_on='TEAM_ID', how='inner')
home_games.head()

# %%
home_games = home_games.rename(columns={'CITY': 'city_home', 'NICKNAME': 'nickname_home'})
home_games.head()

# %%



