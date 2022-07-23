from __future__ import division
import numpy as np

lista = [1,2]
print(lista)

arr =np.arange(0,10)
arr2 = arr.copy()
#Operaciones
multiplicacion = arr * 2
suma = arr + 2
division = 1 / arr
cuadrado = arr ** 2
suma_entre_arrays = arr + arr2

matrix = arr.reshape(2,5)
matrix2 = matrix.copy()
suma_matrix = matrix + matrix2

matrix2.T # transpuesta de valores
operacion_de_producto = np.matmul(matrix,matrix2.T) # Operacion de prodicto punto(algebra)
matrix @ matrix2.T # es lo mismo que hacer las dos lineas de arriba



print(arr2)
print(multiplicacion)
print(suma)
print(division)
print(cuadrado)
print(suma_entre_arrays)
print(matrix)
print(suma_matrix)
print(operacion_de_producto)

