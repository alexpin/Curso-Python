import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)
print(df_books.head(2))

print(df_books.groupby('Author').count()) # Agrupar por columna Author y quiero ver un count.
print(df_books.groupby('Author').mean()) # Media, min, max, sum, 
 # Nota: Author se convierte en indice.

print(df_books.groupby('Author').sum().loc['William Davis']) # Agrupa por Author, suma registros y filtra por el registro William Davis

print(df_books.groupby('Author').sum().reset_index()) # Resetea el indice y muestra la suma plana
print(df_books.groupby('Author').agg(['min','max'])) # Agrupa por determinadas fuciones de agrupamiento
                                                    # en este caso min y max

print(df_books.groupby('Author').agg({'Reviews':['min','max'],'User Rating':'sum'}))
# Agrupa por autor, con agrupamiento pot reviews del min y el max, ademas el user Rating sumado.

print(df_books.groupby(['Author','Year']).count())


