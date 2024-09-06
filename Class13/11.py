
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 50)
y = x**2



fig = plt.figure(figsize=(8,4), dpi=100)
plt.plot(x,x**2, 'b.-')
plt.plot(x,x**3, 'g--')
plt.show()

