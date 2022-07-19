import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype) # Para saber el tipo de dato que maneja el array
print(arr)
arr = arr.astype(np.float64) # Puedo definir el dato directamente desde numpy
print(arr)

arr = np.array([1,2,3,4], dtype = 'float64') # Cambiar el tipo de dato del array
print(arr.dtype)
print(arr)

arr = np.array([0,1,2,3,4])
arr = arr.astype(np.bool_) # Convierte el tipo de datos del array en un bool
print(arr)

arr = np.array([0,1,2,3,4])
arr = arr.astype(np.string_) # Convierte el tipo de datos del array en string
print(arr)

arr = np.array(['0','1','2','3','4'])
arr = arr.astype(np.int8) # Convierte el tipo de datos del array en int
print(arr)

