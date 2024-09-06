
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 50)
y = x**2

plt.plot(x, y, color='red')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfica de Ecuación Cuadrática')
plt.grid()
plt.show()

