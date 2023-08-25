'''ANALISIS DE DATOS CLIMÁTICOS 
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la 
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres 
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál 
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para 
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde 
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los 
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica 
correspondientes. 
(Pista 1) Tu array de entrada podría ser algo como esto, con daros de temperatura, 
humedad, presión y mes del año: '''


# importar modulos
import numpy as np

# Datos de clima ordenados como: temperatura, humedad, presión y mes del año
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

# extraemos los meses en un array distinto
meses =np.array([mes[3] for mes in clima])

# creamos un array para cada dato climatico
temperaturas_medias = np.zeros(12)
humedad_media = np.zeros(12)
presion_media = np.zeros(12)

# sacamos el promedio de cada dato climatico
for mes in range(1,13):
    # temperatura relacionada con el mes
    datos_clima =clima[meses == mes]
    # determinamos la media mensual de cada dato climatico
    temperaturas_medias[mes-1] = np.mean(datos_clima[:,0].astype(int))
    humedad_media[mes-1] = np.mean(datos_clima[:,1].astype(int))
    presion_media[mes-1] = np.mean(datos_clima[:,2].astype(int))
   
print(f'Las temperaturas medias mensuales son: \n {np.round(temperaturas_medias)}')    
print(f'La humedad media mensuales es: \n {np.round(humedad_media)}')   
print(f'La presion medias mensual es: \n {np.round(presion_media)}')   