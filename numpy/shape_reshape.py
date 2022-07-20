import numpy as np

arr = np.random.randint(1,10,(3,2))
print(arr)
print(arr.shape) # Muestra la forma del array, ej numero de filas y columnas
print(arr.reshape(1,6)) # Cambia la forma del areglo.
print(arr.reshape(2,3))

print(np.reshape(arr,(1,6))) # otra forma de llamar la funcion
print(np.reshape(arr,(2,3),'C')) # Como lo haria C
print(np.reshape(arr,(2,3),'F')) # En frotland
print(np.reshape(arr,(2,3),'A')) # Como mejor esta optimi.do en mi sistema

# Desafio

desafio = np.random.randint(1,100,(10,10))
print(desafio)
print(desafio.shape)
print(desafio.reshape(5,20))

