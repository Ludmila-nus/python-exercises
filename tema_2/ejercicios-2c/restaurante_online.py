'''En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente 
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana. 
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la 
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos. 
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus 
ingredientes.'''

#--- preguntamos al usuario que haburguesa quiere clasica o vegana
print('<<<<<bienvenido al sistema de pedidos online>>>>>>')
print('¿Que haburguesa desea elegir?    clasica: opcion 1 / vegana: opcion 2')
eleccion = int(input('ingrese el numero de su eleccion: '))
while 0 > eleccion > 2: # comprobamos que la opcion elegida sea 1 o 2 sino vuelve a preguntar
    print('Opcion invalida ingrese el numero de su eleccion\
       clasica: opcion 1 / vegana: opcion 2')
    eleccion = int(input())

#--- preguntamos si quiere ingredientes extra
print('¿Quiere ingrediente extra? opcion 1: si / opcion 2: no ')
ingrediente_extra =int(input('ingrese el numero de su eleccion: '))
ingr_extra_seleccionados = []
while 0 > ingrediente_extra > 2 : # comprobamos que la opcion elegida sea 1 o 2 sino vuelve a preguntar
    print('Opcion invalida ingrese el numero de su eleccion\
        clasica: opcion 1 / vegana: opcion 2')
    ingrediente_extra = int(input())

#--- si quiere ingredientes extra damos las opciones para hamburguesa clasica 
if eleccion == 1 and ingrediente_extra == 1:
    print('Ingredientes extra disponibles: queso ideazabal, bacon y huevo')
    cantidad = int(input('¿Cuantos ingredientes extra deseas? ingresa la cantidad en numeros: '))
    for i in range(cantidad):
       xtra = input('¿que ingrediente quieres? #{}: ' .format(i + 1))
       xtra = xtra.lower()
       while xtra != 'queso ideazabal' and xtra != 'bacon' and xtra != 'huevo': # comprobamos que ingrese bien el nombre del ingrediente
           print('respuesta no valida, vuelve a intentarlo')
           xtra = input('¿que ingrediente quieres? #{}: ' .format(i + 1))
           xtra = xtra.lower()
       ingr_extra_seleccionados.append(xtra)

#--- si quiere ingredientes extra damos las opciones para hamburguesa vegana
if eleccion == 2 and ingrediente_extra == 1:
     print('Ingredientes extra disponibles: tofu y cebolla caramelizada')
     cantidad = int(input('¿Cuantos ingredientes extra deseas? ingresa la cantidad en numeros: '))
     for i in range(cantidad):
        xtra = input('¿que ingrediente quieres? #{}: ' .format(i + 1))
        xtra = xtra.lower()
        while xtra != 'tofu' and xtra != 'cebolla caramelizada': # comprobamos que ingrese bien el nombre del ingrediente
           print('respuesta no valida, vuelve a intentarlo')
           xtra = input('¿que ingrediente quieres?: ')
           xtra = xtra.lower()
     ingr_extra_seleccionados.append(xtra)

#--- imprimimos por pantalla la eleccion del usuario
if eleccion == 1 and ingrediente_extra == 2: 
    print('su pedido es: HAMBURGUESA CLASICA')   
elif eleccion == 1 and ingrediente_extra == 1: 
    print('su pedido es: HAMBURGUESA CLASICA con los ingredientes extra ', ingr_extra_seleccionados)      
elif eleccion == 2 and ingrediente_extra == 2: 
    print('su pedido es: HAMBURGUESA VEGANA')     
elif eleccion == 2 and ingrediente_extra == 1: 
    print('su pedido es: HAMBURGUESA VEGANA con los ingredientes extra: ', ingr_extra_seleccionados)    