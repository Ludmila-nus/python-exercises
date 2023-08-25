'''ANALISIS DE DATOS - VENTAS POR MES 
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año. 
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la 
venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos, 
etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en 
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3 
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de 
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.'''


import numpy as np
import datetime


#  creamos el array con los datos de ventas
ventas = np.array([
    ['2022-01-01',100,'ropa'],
    ['2022-02-01',200,'alimento'],
    ['2022-03-01',150,'ropa'],
    ['2022-01-02',120,'alimento'],
    ['2022-02-02',180,'electronicos'],
    ['2022-03-02',200,'alimento'],
    ['2022-01-02',90,'ropa'],
    ['2022-02-03',110,'electronicos'],
    ['2022-03-03',100,'alimento'],
    ])

#  extraemos las fechas en un array distinto
fecha_ventas = np.array([registro[0] for registro in ventas])
print(fecha_ventas)

#  convertimos las fechas en formto datatime y las extraemos a otro array
meses = np.array([mes[5:7] for mes in fecha_ventas]).astype(int)
print(meses)

#  analizamos cual fue el monto de ventas por mes
# creamos un array para almacenar las ventas por mes
ventas_por_mes = np.zeros(12)

#recorremos el array de ventas para sacar los totales de ventas por mes
for i in range(1,13):
    promedio = ventas[meses==i]
    ventas_por_mes[i-1] = np.sum(promedio[:,1].astype(int))
    print(ventas_por_mes)
    

print(ventas_por_mes)