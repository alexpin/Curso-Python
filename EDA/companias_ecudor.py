import pandas as pd

# Ruta del archivo csv
ruta_archivo_csv = "/mnt/c/Users/alexa/OneDrive/Escritorio/Bases_Data/Super_Compañias/bi_ranking.csv"


# Leer el archivo csv en un DataFrame de pandas
try:
    df = pd.read_csv(ruta_archivo_csv)
    print("Contenido del archivo de csv:")
    print(df)
except FileNotFoundError:
    print("¡El archivo no se encontró!")
except Exception as e:
    print("Ocurrió un error al leer el archivo:")
    print(e)
