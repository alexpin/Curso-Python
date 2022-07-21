import numpy as np

arr = np.random.randint(1,20,10)
matrix = arr.reshape(2,5)
print(arr)
print(matrix)

#Funcion max -> retorna el numero mas grande
print(arr.max())
print(matrix.max(0)) # Por el eje 1 fila 0 columna

# argmax -> Retorna el indice del valor mas alto
print(arr.argmax())
print(matrix.argmax(0))

# min
print(arr.min())
print(matrix.min(0))

#argmin
print(arr.argmin())
print(matrix.argmin(0))

# ptp -> Devuelve la diferencia entre el pico mas alto y el mas bajo
print(arr.ptp())
print(matrix.ptp(0))

# Devuelve el precentil(valor de la mitad)
print(np.percentile(arr,50))

# sort -> Ordena de menor a mayor el arreglo
print(np.sort(arr))

# median -> Calcula la media
print(np.median(arr))
print(np.median(matrix,0))

# std -> Calcula la desviacion standar
print(np.std(arr))

# var -> Calcula la varian.a
print(np.var(arr))

# mean -> calcula la media
print(np.mean(arr))

# concatenate -> Concatena dos arreglos por el eje que le indiquemos
a = np.array([[1,2],[3,4]])
b = np.array([5,6])
print(a.ndim)
print(b.ndim)
b = np.expand_dims(b, axis=0)
print(np.concatenate((a,b), axis=0))

# T -> Transpuesta en este caso de b, es cambiarle la forma.
print(np.concatenate((a,b.T), axis=1))



