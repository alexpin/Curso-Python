import pandas as pd

players_granada = {'Jugador':['Luis Suárez','Jorge Molina', 'Antonio Puertas', 'Germán Sánchez', 'Luis Milla', 'Luís Manuel Arantes Maximiano'],

'Posición':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],

'Número':[9, 23, 10, 6, 5, 1],

'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],

'Goles':[7, 7, 5, 2, 2, 0]}

dataf_granada = pd.DataFrame(players_granada)

print(dataf_granada)
print(dataf_granada.columns)
print(dataf_granada.index)








