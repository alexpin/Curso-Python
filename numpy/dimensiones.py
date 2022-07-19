from array import array
import numpy as np

scalar = np.array(42)
print(scalar)
print(scalar.ndim) # numero de dimensiones

vector = np.array([1,2,3])
print(vector)
print(vector.ndim)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[0,2,45]])
print(matrix)
print(matrix.ndim)

tensor = np.array([[[1,2,3],[4,5,6],[7,8,9],[0,2,45]],[[1,2,3],[4,5,6],[7,8,9],[0,2,45]]])
print(tensor)
print(tensor.ndim)

# Agregar o eliminar dimensiones

vector = np.array([1,2,3],ndmin=10) # Agrega 10 dimensiones al vector
print(vector)
print(vector.ndim) 

expand = np.expand_dims(np.array([1,2,3]),axis=0) # Expande una dimension a nivel de filas
print(expand)   # 0 son filas y 1 columnas
print(expand.ndim)

print(vector, vector.ndim)
vector_2 = np.squeeze(vector) #squeeze comprime el numero de versiones que no se esten usando
print(vector_2, vector_2.ndim)

tensorx = np.array([[[[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]],[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]],[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]]]])
print('Tensor de 5 dimensiones')
print(tensorx)
print(tensorx.ndim)
expandx = np.expand_dims(tensorx,axis=0)
print(expandx, expandx.ndim)
expandx = np.squeeze(expandx)
print(expandx, expandx.ndim)
