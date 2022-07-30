import pandas as pd
import numpy as np

dict = {'Col1':[1,2,3,np.nan],
 'Col2':[4,np.nan,6,7],
 'Col3':['a','b','c',None]}
 
df = pd.DataFrame(dict)
print(df)

print(df.isnull()) # Muestra  como True los valores nulos del dataframe.
print(df.isnull()*1) # Para llevarlos a 1 null o cero valido
print(df.fillna('Missing')) # Llena los valores nulos como ....
print(df.fillna(df.mean())) # Llena los valores  nulos con la media
print(df.interpolate()) # Llena los valores nulos con la interpolacion de un serie
print(df.dropna()) # Elimina los valores nulos

