'''Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un 
programa para realizar un seguimiento de los productos que has vendido y el valor total de las 
ventas. Supongamos que hay un total de 10 productos.  
Tú has vendido 5 de estos productos en las siguientes cantidades: 
Producto 1: 3 unidades 
Producto 2: 1 unidad 
Producto 5: 7 unidades 
Producto 6: 2 unidades 
Producto 9 : 4 unidades 
Los precios de cada uno de estos productos son como siguen: 
Producto 1: 30.0 EU  Producto 6: 44.0 EU  
Producto 2: 9.8 EU  Producto 7: 21.2 EU 
Producto 3: 42.5 EU  Producto 8: 53.2 EU 
Producto 4: 32.6 EU  Producto 9: 25.3 EU 
Producto 5: 71.5 EU  Producto 10: 57.8 EU 
Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima 
la cantidad total de ventas, el dinero facturado por producto y el dinero total.'''

from termcolor import colored

#--- creamos una lista de los productos y sus precios
productos = [['p1', 30],['p2', 9.8],['p3', 42.5],['p4', 32.6],['p5', 71.5],['p6', 44],['p7', 21.2],['p8', 53.2],['p9', 25.3],['p10', 57.8],]

#--- preguntamos cuantas unidades de cada producto se han vendido y almacenamos el valor
total_ventas = [] # lista para almacenar la cantidad de unidades venidas por producto
for i in range(0,len(productos)):
    print('Ingrese la cantidad que se vendio del producto:')
    print(productos [i][0])
    vendidos = int(input('cantidad vendida: '))
    total_ventas.append(vendidos)

#--- damos el resultado por pantalla de 
# 1- total de ventas
print(colored(f'El total de unidades venidas es de:  {sum(total_ventas)} Unidades','blue'))

# 2- dinero facturado por producto
dinero = [] # creamos una lista que almacene el valor facturado por producto
print(colored('El total de dinero facturado por unidad es de: ','blue')) 
for i in range(0,len(productos)):
    dinero_por_producto= productos[i][1] * total_ventas[i]
    print(colored(f'{productos[i][0]} {dinero_por_producto} Euros','magenta'))   
    dinero.append(dinero_por_producto)

# 3- dinero total facturado
print(colored(f'El total de dinero facturado es de:  {sum(dinero)} Euros','blue'))


