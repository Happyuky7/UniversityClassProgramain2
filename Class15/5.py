# 2.6 ¿Que haremos?
"""
- Utilizando la misma base flights.csv, hacer un loop y clasisficar los meses con una cantidad de pasajeros menor a la media
- Para ello, generen un nuevo objeto que represente la media de passengers y asígnele 0.
- Ejecuten un loop que recorra cada observación de passengers, donde si la observación es menor a la media de
passengers se le
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv('flights.csv')
