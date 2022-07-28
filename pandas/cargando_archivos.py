import pandas as pd

bestsellers = pd.read_csv('/home/alexpino70/curso_python/archivos/bestsellers with categories.csv', sep=',',
header=0, names=['Namessss', 'Authorrrrrr', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
print(bestsellers)
print(bestsellers.columns)

archi_json = pd.read_json('/home/alexpino70/curso_python/archivos/HPCharactersDataRaw.json', typ='Series')
print(archi_json)