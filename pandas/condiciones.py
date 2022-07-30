import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)
print(df_books.head(2))

mayor_2016 = df_books['Year'] > 2016 # Flitrando
print(df_books[mayor_2016])

print(df_books[df_books['Year'] > 2016]) # Otra forma de hacer el flitrado

genre_fiction = df_books['Genre'] == 'Fiction'
print(genre_fiction)

print(df_books[genre_fiction & mayor_2016]) # cumple dos codiciones
print(df_books[~mayor_2016]) # Para negar la condicion



