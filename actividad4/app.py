from data.data import *  # Se importa todos los elementos de la carpeta "data" desde el paquete "data"
from BD.baseDatos import *   # Se importa todos los elementos de la carpeta "BD" desde el paquete "baseDatos"
from sklearn.linear_model import LinearRegression # Se importa la clase "LinearRegression" desde el módulo "sklearn.linear_model"
from grafica.grafica import *   # Se importa todos los elementos de la carpeta "grafica" desde el paquete "grafica"
import pandas as pd   # Se importa la libreria pandas para analizar los datos como pd

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() # Llama a la función "dataTeorico" desde la carpeta "data.data" y almacena sus resultados en las variables "dataTeoricoEsfuerzo" y "dataTeoricoDeformacion"

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() # Llama a la función "lecturaDatos" desde la carpeta "BD.baseDatos" y almacena los datos en "data_list"
data_real = pd.DataFrame(data_list) # Se crea un DataFrame de pandas data_real a partir de la lista de datos obtenida
data_real_fit = data_real  # Se copia el DataFrame data_real en data_real_fit
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) # Prepara los datos para el modelo de regresión lineal, define las caracteristicas de x
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1) # Prepara los datos para el modelo de regresión lineal, define las caracteristicas de y
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] # Obtiene los valores máximos de 'Esfuerzo[kN]' en el "data_real"
y_lim = data_real['Deformacion[mm]'].iloc[-1] # Obtiene los valores máximos de 'Deformacion[mm]' en el "data_real"
model = LinearRegression() # Se crea un modelo de regresión lineal
model.fit(X, y) # Se ajusta el modelo con los datos de entrenamiento (X e y)
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) # Se realiza una predicción para un valor de entrada de 3000 kN y la almacena en "prediction"
print('la predicción a 1000 kN es de: ', prediction ,'mm') # Se mprime la predicción


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] # Se extrae las columnas 'Esfuerzo[kN]' del "data_real"
dataRealDeformacion = data_real['Deformacion[mm]'] # Se extrae las columnas 'Deformacion[mm]' del "data_real"

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se grafica la data_real
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) # Se grafica la data_real con prediccion de los valores ya especificados
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model) # Se grafica una prediccion a la data_real para 3000KN

