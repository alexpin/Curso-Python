import pandas as pd
import numpy as np  

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3'],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
 'B':['B4','B5','B6','B7'],
 'C':['C4','C5','C6','C7'],
 'D':['D4','D5','D6','D7']})

df3 = pd.concat([df1,df2], ignore_index=True) # Concatena por el axis 0, los indices se heredan
#(para este caso se repiten), por eso usamos ignore_index True, para corregirlo.
print(df3) 

df4 = pd.concat([df1,df2],axis=1) # Usando el axis 1
print(df4)

#MERGE

ixq = pd.DataFrame({'key':['k0','k1','k2','k3'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key':['k0','k1','k2','k3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})

print(ixq.merge(der, on='key')) # merge de ixqierda a derecha sobre la columna key.

ixq = pd.DataFrame({'key':['k0','k1','k2','k3'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key_2':['k0','k1','k2','k3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})

print(ixq.merge(der, left_on='key', right_on='key_2')) # Para utilixar las dos columnas key and key_2

ixq = pd.DataFrame({'key':['k0','k1','k2','k3'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key_2':['k0','k1','k2',np.nan],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})

print(der)
print(ixq.merge(der, left_on='key', right_on='key_2', how='left')) # En how puedo utilixar inner, left
#  o right, la opcion por defecto es inner.

#JOIN - es un index match, busca el match por indices, no por columas como el merge

ixq = pd.DataFrame({'A':['A0','A1','A2'],
'B':['B0','B1','B2']},
index=['K0','K1','K2'])

der = pd.DataFrame({'C':['C0','C1','C2'],
'D':['D0','D1','D2']},
index=['K0','K2','K3'])

print(ixq.join(der, how='outer')) # Valores de how= left, right, inner, outer(Trae todo)



