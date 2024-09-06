
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 50)
y = x**2

plt.plot(x, y, color='red', label='Ecuación Cuadrática')
plt.plot(x, np.sin(y), color='green', label='Oscilación Seno')
plt.xlabel(r'$\alpha$', fontsize=15)
plt.ylabel(r'$\beta$($\alpha$)', fontsize=15)
plt.title('Gráfica de Ecuación Cuadrática')
plt.grid()
plt.legend(loc=9)
plt.show()

