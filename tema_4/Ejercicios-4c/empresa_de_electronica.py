'''EMPRESA DE ELECTRONICA 
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres 
analizar los datos de calidad de los componente utilizados en la producción de dichos 
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de 
producción, el tipo de componente, el lote al que pertenece el componente y la 
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos 
datos para determinar cuál es el tipo de componente con la puntuación de calidad más 
alta, cuántos componente se produjeron en cada mes y cuál es la puntuación de calidad 
promedio de cada tipo de componente
(Pista 2: puede ser util investigar np.unique y np.argmax)'''

#-- importamos numpy
import numpy as np

#-- creamos el array con los datos de la empresa electronica
# fecha de produccion, tipo de componente, lote, puntuacion de calidad(0-100)
datos = np.array([["2022-01-01", "componente 1", "lote A", 80],
                 ["2022-01-15", "componente 1", "lote B", 90],
                 ["2022-02-01", "componente 2", "lote C", 85],
                 ["2022-02-15", "componente 2", "lote D", 95],
                 ["2022-03-01", "componente 1", "lote F", 75],
                 ["2022-03-15", "componente 2", "lote G", 90]])

#--- determinar cual es el tipo de componente con la puntuación de calidad más alta
# determinamos la puntuacion maxima 
puntuacion_max = np.amax(datos[:,3].astype(int))

# determinamos el indice de la puntuacion maxima
indice_puntuacion_max = np.argmax(datos[:,3].astype(int))

# imprimimos por pantalla el resultado
print(f'El componente con la puntuacion maxima es el {datos[indice_puntuacion_max,1]} con una puntuacion de {puntuacion_max}')

#--- determinar cuántos componente se produjeron en cada mes
# extraemos las fechas de produccion
fechas_produccion = np.array([registro[0] for registro in datos])

# extraemos los meses de produccion
meses_produccion = np.array([meses[5:7] for meses in fechas_produccion]).astype(int)
meses = np.unique(meses_produccion)

# contamos cuantos componente se produjeron en cada mes
for mes in range(1,len(meses)+1):
    componente_mes = datos[meses_produccion==mes]
    componente, counts = np.unique(componente_mes[:,1], return_counts=True)
    print(f'En el mes {mes} se produjeron {counts} unidades del componente {componente}')


#--- determinamos cuál es la puntuación de calidad promedio de cada tipo de componente
# extraemos en un array los componentes
lista_componente = np.array([comp[1] for comp in datos])

# extraemos los componente como dato unico
componente = np.unique(datos[:,1])

# creamos un array para guardar los datos de puntuacion de cada componente
puntuacion_comp1 = np.zeros(len(datos))
puntuacion_media_comp2 = np.zeros(len(datos))

# recorremos con un for el array datos para extraer las puntuaciones segun los componentes
puntuaciones_comp1 = []
puntuaciones_comp2 = []
for i in range(len(datos)):
    if lista_componente[i] == componente[0]:
        puntuacion_comp1 = np.sum(datos[i,3].astype(int))
        puntuaciones_comp1.append(puntuacion_comp1)
    elif lista_componente[i] == componente[1]:
        puntuacion_comp2 = np.sum(datos[i,3].astype(int))
        puntuaciones_comp2.append(puntuacion_comp2)  

# sacamos la media de cada componente
puntuacion_comp1 = np.mean(puntuaciones_comp1)
puntuacion_comp2 = np.mean(puntuaciones_comp2)
# imprimimos por pantalla cada valor
print(f'El {componente[0]} tiene una puntuacion media de {puntuacion_comp1:.2f}')
print(f'El {componente[1]} tiene una puntuacion media de {puntuacion_comp2:.2f}')

# ---- probamos si me sale el codigo de elena-----
# extraemos lista aparte con los componentes
lista_comp = datos[:,1]

# extraemos las puntuaciones de los componentes
puntuaciones = datos[:,3].astype(float)

# creamos un array para almacenar los datos de los promedios 
promedio_por_tipo = np.zeros(len(componente))

# recorremos con un for la lista de componentes unicos
for i in range(len(componente)):
   promedio_por_tipo[i] = np.mean(puntuaciones[lista_comp==componente[i]])
   print(f'El {componente[i]} tiene una puntuacion media de {promedio_por_tipo[i]:.2f}')

# saliooooooooooooooooo vamoooooooooooooooooooooooooo!!!!!!!!!!!!!!!!!!   