from re import I
import pandas as pd

df_books = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0)
print(df_books.head())

#PIVOT Transforma los valores de una columnas o filas a indices

df_pivot = df_books.pivot_table(index='Author',columns='Genre',values='User Rating')
print(df_pivot)


df_pivot2 = df_books.pivot_table(index='Genre',columns='Year', values='User Rating', aggfunc='sum')
print(df_pivot2) #aggfunc es funcion de agrupamiento

# MELT Toma las columnas y las pasa a filas

print(df_books[['Name','Genre']].head())
print(df_books[['Name','Genre']].head().melt())
print(df_books.melt(id_vars='Year',value_vars='Genre'))

#Simplemente, podemos seleccionar las columnas que no quiero hacer melt usando el parámetro id_vars. 
# Para este caso Year y también la única columna que quiero aplicar el melt, 
# para este caso Genre con la propiedad value_vars.

