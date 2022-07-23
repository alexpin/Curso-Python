import numpy as np


lista = [1,2,3,4,5,6,7,8,9]    
print(lista)

arr = np.array(lista)     
print(type(arr))

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

print(arr[0])
print(arr[0] + arr[5])

print(matriz[0, 2])

print(arr[0:3])
print(arr[2:]) # Puedo recorrer sin el strar y sin el end
print(arr[::3]) # Imprime todo pero de tres en tres
print(arr[-1]) # Toma el primer valor pero del final al inicio
print(arr[-3:]) # Toma los tres ultimos

print(matriz[1:]) # Desde la primera fila hacia adelante
print(matriz[1:,0:2]) # Desde la primera fila, pero con las columnas de la cero a la uno(no toma en cuenta el end)

# matrix de tres dimensiones
matrix3d = [[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]
matrix3d = np.array(matrix3d)
print(matrix3d)
print(matrix3d[0,0,0]) # Imprime el primer valor de las filas y las columnas y profundidad
print(matrix3d[-1, -1, -1]) # Ultimo valor
print(matrix3d[:, 0, 0])

