import pandas as pd

import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)
print(df_books.head(2))

def two_times(value):
    return value * 2

df_books['Rating2'] = df_books['User Rating'].apply(two_times)
# Applay aplica una funcion al DataFrame
print(df_books)

df_books['Rating2'] = df_books['User Rating'].apply(lambda x : x * 3) # lambda o funciones anomias de python
print(df_books.head())

df_books['Rating2'] = df_books.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)
# Se lee asi: Applicar a todo el df_books la funcion lambda que es, multiplicar los valores de la 
# columna User Rating por dos solamente si Genre es igual a Fiction, si no dejar el miimo valor
# de la columa User Rating, estamos haciendo referencia al axis uno o columnas.

print(df_books)
