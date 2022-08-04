import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11) # Crea una serie aleatoria de cero a cinco con once valores
y = x**2

plt.plot(x,y)
print(plt.show())
