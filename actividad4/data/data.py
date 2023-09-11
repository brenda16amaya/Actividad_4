import pandas as pd   # Se importa la libreria pandas para analizar los datos como pd

# Importar datos del csv
data_teorico = r"C:\Users\user\Desktop\actividad5\data\Data ingeniero.csv"  # Se importa la base de datos de excel y se guarda como data_teorico

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): # Se define la función dataTeorico
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] # Se accede a las columnas "Esfuerzo[kN]" del data_teorico
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] # Se accede a las columnas "Deformacion[mm]" del data_teorico
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion # Se regresa de la funcion dos valores


