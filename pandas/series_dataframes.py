import pandas as pd

psg_players = pd.Series(['Nabas', 'Mbappe', 'Neymar', 'Messi'], index=[1,7,10,30]) #series

print(psg_players)

psg_players2 = pd.Series(['Nabas', 'Mbappe', 'Neymar', 'Messi']) # Series
print(psg_players2)

dictio = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'} #Diccionario de python
Dictio_panda = pd.Series(dictio)
print(Dictio_panda)

print(psg_players[7]) # Acceder a un pasicion del objeto
print(psg_players2[0:3]) #Slacing

dictio2 = {'Jugador':['Nabas', 'Mbappe', 'Neymar', 'Messi'], 
'Altura':[183.0, 170.0, 170.0, 165.0],
'Goles':[2,200,200,200]
} # Data frame

psg_players3 = pd.DataFrame(dictio2)
print(psg_players3)
print(psg_players3.columns)
print(psg_players3.index)











