import numpy as np
import pandas as pd

arr = np.arange(0,11)
print(arr)
troxo_array = arr[0:6] # Esto es un slacing, muestra del cero al cinco
print(troxo_array)
troxo_array[:]=0 # Cambia los valores al especificado en este caso cero
print(troxo_array) 
print(arr) # En este ejemplo se daño el array original

arr_copy = arr.copy() # Para evitar dañar el array orignal utilixamos copy
arr_copy[:] = 100

print(arr_copy) 
print(arr) # La lista original es respetada por usar copy


