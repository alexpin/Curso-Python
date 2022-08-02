import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)

print(df_books.head(2))
print(df_books.info())
print(df_books.describe())
print(df_books.tail(2)) # Devualeve las x ultimas filas.
print(df_books.memory_usage(deep=True)) # Devuelve el uso de la memoria de cada columna
print(df_books['Author'].value_counts()) # Devuelve los registros por autor.

df_books.iloc[0] # Muestra todas las columas de la posicion cero.
df_books = df_books.append(df_books.iloc[0]) # Duplica la fila cero
print(df_books) # La duplicacion se ve al final.False
df_books = df_books.drop_duplicates(keep='last') # Elimina todas las filas duplicadas del data frame, con
print(df_books)                                  # keep last borra el primero y deja el ultimo

print(df_books.sort_values('Year', ascending=False)) # Ordena todo el dataframe por la coumna Year en orden ascendente




