'''Tienes una tienda y deseas realizar un seguimiento de las ventas diarias 
de tus productos. Cada producto tiene un nombre y una cantidad 
vendida. Implementa un programa en Python que utilice un diccionario 
para almacenar la información de las ventas. El programa debe permitir 
registrar las ventas de productos, actualizar la cantidad vendida de un 
producto existente y calcular el total de ventas diarias. 
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada 
producto)'''
#-- importamos datetime para ponerle fecha al ingreso de los datos
from datetime import datetime
dia = datetime.today()

#--- listado de productos que vende la tienda
productos_tienda = ['buzo','remera','pantalon','campera','chaleco']

#--- diccionario vacio donde cargaremos los datos de las ventas de la tienda
ventas_tienda = {}

#--- cargamos el producto y la cantidad vendida de cada uno
print('---Bienvenido al sistema de ventas---')
print('Hoy es: ', dia)
ventas_diarias = 0
finalizar = ''
while finalizar != 'no':
    print('ingrese el nombre del producto vendido: ', '\n', productos_tienda)
    producto = input('producto: ')
    ventas_producto = int(input('Ingrese la cantidad vendida: '))
    # producto que ya se encuentra registrado
    if producto in ventas_tienda:
        ventas_tienda[producto] += ventas_producto
        ventas_diarias += 1
    # producto nuevo    
    else:
        ventas_tienda[producto] = ventas_producto
        ventas_diarias += 1
    print('La venta quedo registrada correctamente')
    finalizar = input('¿Quiere añadir una nueva venta? si / no: ')    

print('Resumen de ventas: ')
print(f'\ttotal de ventas del dia: {ventas_diarias}')
print(f'\tcantidad total de ventas de cada producto: {ventas_tienda}')
   