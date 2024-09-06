
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = x**2



plt.subplot(1,2,1)
plt.plot(x,y)
plt.grid()
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.plot(x,y**2, color='green')
plt.subplot(2,2,4)
plt.plot(y,x**4, color='red')
plt.show()

