import pandas as pd

# Ruta del archivo Excel
ruta_archivo_excel = "C:\Users\alexa\OneDrive\Escritorio\Bases_Data\Super_Compañias.xlsx"

# Leer el archivo Excel en un DataFrame de pandas
try:
    df = pd.read_excel(ruta_archivo_excel)
    print("Contenido del archivo de Excel:")
    print(df)
except FileNotFoundError:
    print("¡El archivo no se encontró!")
except Exception as e:
    print("Ocurrió un error al leer el archivo:")
    print(e)
