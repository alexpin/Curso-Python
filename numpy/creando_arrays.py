import numpy as np

list(range(0,10))
print(list(range(0,10))) # Codigo de python para generar una lista

np.arange(0,10)
print(np.arange(0,20,2)) # Codigo de numpy, para generar un array, de dos en dos

print(np.zeros(3)) #Crea un array compuesto por ceros 
print(np.zeros((10,10))) # Se utlizan para definir estructuras predefinidas

print(np.ones((10,10)))

print(np.linspace(0,10,100)) # Crea un distribucion que inicia en cero, termina en 10 y genera 100 datos

print(np.eye(4)) # Crea un matriz con la diagonal principal en 1 y el resto en ceros

print(np.random.rand()) # Crea un valor aleatorio entre cero y uno
print(np.random.rand(4)) # Genera un array con cuatro valores totalmente aleatorios
print(np.random.rand(4,4)) # Gerena un estructura matricial de cuatro por cuatro
print(np.random.randint(1,15)) # Genera un enteros aleatorio entre uno y quince
print(np.random.randint(1,100,(10,10))) # Genera un estructura de 10 por 10 de aleatorios
