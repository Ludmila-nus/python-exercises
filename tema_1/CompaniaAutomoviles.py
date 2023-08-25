'''Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes.'''

ComisionrRmbS1 = 20000 * 0.03
ComisionRmbPlus = 35000 * 0.05
ComisionRmbTT = 60000 * 0.07

print('Introduzca la cantidad de unidades vendidas en el mes concluido')
RmbS1 = input('RMB Serie 1: ')
RmbPlus = input('RMB Serie Plus: ')
RmbTT = input('RMB Todoterreno: ')

comision = float(RmbS1) * ComisionrRmbS1 + float(RmbPlus) * ComisionRmbPlus + float(RmbTT) * ComisionRmbTT

print('Su comision este mes es de: ' + str(comision))