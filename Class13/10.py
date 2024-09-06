
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = x**2



fig = plt.figure(figsize=(2,2), dpi=100)
plt.plot(x,y)
plt.savefig('grafico.png')  
plt.show()

