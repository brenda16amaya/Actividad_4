import matplotlib.pyplot as plt # Se importa la libreria matplotlib y renombra como plt y sirve para hacer grafica los datos
import numpy as np # Se importa la libreria numpy y renombra como np y sirve para hacer operaciones matematicas 



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): # Se define una función gr_con_prediccion con parámetros
    
    
    plt.figure(figsize=(15, 6)) # Se crea una figura de tamaño 15x6 para la gráfica
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se dibuja una línea con "dataTeoricoEsfuerzo" en el eje x y "dataTeoricoDeformacion" en el eje y
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') # Se dibuja puntos dispersos con "dataRealEsfuerzo" en el eje x y "dataRealDeformacion" en el eje y, en color rojo
    plt.xlabel('Esfuerzo [kN]') # Se nombra el eje x con "Esfuerzo [kN]"
    plt.ylabel('Deformación [mm]') # Se nombra el eje y con "Deformación [mm]"
    plt.title('Gráfica 2: teórico versus real [ZOOM]') # Se nombra el grafico como "Gráfica 2: teórico versus real [ZOOM]"
    plt.xlim(0, x_lim) # Se establece los limites del eje x
    plt.ylim(0, y_lim) # Se establece los limites del eje y
    plt.grid()  # Se agrega una cuadricula a la grafica
    plt.gca().invert_yaxis()  # Se invierte los valores del eje y
    plt.show()  # Se muestra la grafica

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): # Se define una función gr_con_prediccion_3000 con parámetros
  plt.figure(figsize=(15, 6)) # Se crea una figura de tamaño 15x6 para la gráfica
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se dibuja una línea con "dataTeoricoEsfuerzo" en el eje x y "dataTeoricoDeformacion" en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') # Se dibuja puntos dispersos con "dataRealEsfuerzo" en el eje x y "dataRealDeformacion" en el eje y, en color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') # Se dibuja una línea de predicción utilizando el modelo "model"
  plt.scatter(	3000 , prediction, color='green') # Se dibuja un punto en (3000, prediction) en color verde
  plt.xlabel('Esfuerzo [kN]') # Se nombra el eje x con "Esfuerzo [kN]"
  plt.ylabel('Deformación [mm]') # Se nombra el eje y con "Deformación [mm]"
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') # Se nombra el grafico como "Gráfica 3: Predicción a una carga de 3000 kN"
  plt.xlim(0, 3000) # Se establece los limites del eje x (3000)
  plt.ylim(0, 45) # Se establece los limites del eje y (45)
  plt.grid() # Se agrega una cuadricula a la grafica
  plt.gca().invert_yaxis() # Se invierte los valores del eje y
  plt.show() # Se muestra la grafica

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): # Se define una función gr_sin_prediccion con parámetros
  plt.figure(figsize=(15, 6)) # Se crea una figura de tamaño 15x6 para la gráfica
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) # Se dibuja una línea con "dataTeoricoEsfuerzo" en el eje x y "dataTeoricoDeformacion" en el eje y
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') # Se dibuja puntos dispersos con "dataRealEsfuerzo" en el eje x y "dataRealDeformacion" en el eje y, en color rojo
  plt.xlabel('Esfuerzo [kN]') # Se nombra el eje x con "Esfuerzo [kN]"
  plt.ylabel('Deformación [mm]') # Se nombra el eje y con "Deformación [mm]"
  plt.title('Gráfica 1: teórico versus real') # Se nombra el grafico como "Gráfica 1: teórico versus real"
  plt.grid() # Se agrega una cuadricula a la grafica
  plt.gca().invert_yaxis() # Se invierte los valores del eje y
  plt.show() # Se muestra la grafica