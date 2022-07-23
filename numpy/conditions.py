import numpy as np

arr = np.linspace(1,10,10, dtype='int8')


indices_cond = arr > 5
condiciones = arr[indices_cond]
condiciones2 = arr[(arr > 5) & (arr < 9)] # Funciona igual que lo anterior, pero agregando mas codiciones
arr[arr > 5] = 99 
condiciones4 = arr[arr==99]


print(condiciones)
print(condiciones2)
print(arr)
print(condiciones4)