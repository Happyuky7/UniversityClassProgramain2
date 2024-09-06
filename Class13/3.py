"""
Graficar una funcion cuadratica
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 50)
y = x**2

plt.plot(x, y, color='red')
plt.grid()
plt.show()

