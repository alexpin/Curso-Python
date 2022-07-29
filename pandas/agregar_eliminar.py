import pandas as pd
import numpy as np

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)
# Para recordar sep se usa para indicar el tipo de separador del archivo y header para indicar cual fila
# es el encabexado

print(df_books.head(2)) # Muestra las dos primeras filas.

# Drop columns -> Eliminar las columnas de un dataframe

print(df_books.drop('Genre', axis=1).head(2)) # axis o eje cero para filas uno para columnas, esta instruccion
                                              # solo borra los datos de la salida


df_books.drop('Genre', axis=1, inplace=True) # Borra toda la columna del dataframe
print(df_books.head(2))

df_books = df_books.drop('Year', axis=1) # Otra manera de borrar del dataframe
print(df_books.head(4))

del df_books['Price'] # Esta funcion  no es andas, es de python, no es muy recomendada.
print(df_books.head(4))

# drop rows

print(df_books.drop(0, axis=0).head(2)) # Borra la fila cero
print(df_books.drop([0,1,2], axis=0).head(2))
print(df_books.drop(range(0,10), axis=0).head(2))

# Add columns

print(df_books.head(2))

df_books['Nueva Columna'] = np.nan # nan es un valor no numerico, es el valor que va a tomar la columna
print(df_books.head(2))
print(df_books.shape[0]) # Muestra el numero de filas

data = np.arange(0, df_books.shape[0]) # Genera una lista de cero a 549
print(data)
df_books['Rango'] = data # Optiene una nueva columna con un rango de datos ordenado como el data
print(df_books)

# add rows

print(df_books.append(df_books)) # anexa de si mismo a si mismo, dobla en numero de filas






