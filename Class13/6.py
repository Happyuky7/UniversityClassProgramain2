
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 50)
y = x**2

plt.plot(x, y, color='red')
plt.plot(x, np.sin(y), color='green')
plt.xlabel(r'$\alpha$', fontsize=15)
plt.ylabel(r'$\beta$($\alpha$)', fontsize=15)
plt.title('Gráfica de Ecuación Cuadrática')
plt.grid()
plt.show()

