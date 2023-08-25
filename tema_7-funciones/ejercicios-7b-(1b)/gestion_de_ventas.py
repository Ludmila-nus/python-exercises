'''Crea un programa que permita gestionar las ventas de una tienda. Utiliza una 
estructura de datos adecuada para almacenar la información de las ventas 
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para 
agregar el producto vendido con su precio y otro para mostrar las ventas de 
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: 
precio1}, {“Producto”: producto2, “Precio”: precio2}...])'''

# estructura para almacenar la informacion
base_datos = []

# funcion 1: agrega producto vendido con su precio
def agregar_producto(producto,precio):
   """agrega ventas a nuestra base de datos"""
   venta = {
      'producto':producto,
      'precio':precio
      }
   base_datos.append(venta)

# funcion 2: muestra las ventas de productos con sus respectivos precios
#def mostrar_ventas(ventas_producto):
def  mostrar_ventas():
   """muestra las ventas realizadas de cada producto"""
   for dato in base_datos:
      print('Producto', dato['producto'])
      print('Precio', dato['precio'])
      print('------------')

agregar_producto('camisa',5500)
agregar_producto('jeans',10000)
agregar_producto('botas',7500)

mostrar_ventas()

 