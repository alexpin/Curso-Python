import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0, names=['Names', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
print(df_books)
print(df_books.columns)

archi_json = pd.read_json('/home/alexpino70/curso_python/archivos/HPCharactersDataRaw.json', typ='Series')
print(archi_json)
print(df_books[0:4])
print(df_books[['Names', 'Author', 'Year']])

#loc

print(df_books.loc[:]) # Muestra todo el dataframe
print(df_books.loc[0:4, ['Names', 'Author']]) # muestra del cero al cuatro y las labels name y author
print(df_books.loc[:, ['Reviews']] * -1)
print(df_books.loc[:, ['Author']] == 'JJ Smith')

# iloc busqueda por indices

print(df_books.iloc[:, 0:3]) # Todas las filas, y cuatro primeras columnas
print(df_books.iloc[1,3]*-1) 
print(df_books.iloc[:2, 2:])
