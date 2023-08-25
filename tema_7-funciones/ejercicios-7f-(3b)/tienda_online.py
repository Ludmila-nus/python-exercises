'''TIENDA ONLINE 
Crea una clase "Producto" con atributos como nombre, precio y cantidad en 
stock. Luego, crea una clase "Tienda" que contenga una lista de productos 
disponibles y métodos para agregar productos, mostrar el inventario y 
realizar una compra.'''


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Tienda:
    def __init__(self):
        self.listado_productos = []

    def agregar_producto(self, producto):
        self.listado_productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.listado_productos:
            print(f'Producto: {producto.nombre} \n Precio: {producto.precio} \n Cantidad en stock: {producto.stock}')

    def realizar_compra(self, nombre, cantidad):
        for producto in self.listado_productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f'La compra del producto {nombre} se ha realizado con exito \n Usted debe pagar {cantidad * producto.precio} Usd')
                else:
                    print('Lo lamento, no hay cantidad de ese producto en stock.')    

tienda = Tienda()
producto1 = Producto('Remera', 2500, 10)
producto2 = Producto('Jean', 7500, 15)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_inventario()

tienda.realizar_compra('Jean', 2)

tienda.mostrar_inventario()

        
        







