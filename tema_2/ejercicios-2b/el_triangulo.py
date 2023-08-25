'''En una obra es necesario construir para el tejado de una casa una estructura triangular con tres 
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir 
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo 
con esas piezas'''

#--- se ingresan las 3 longitudes de las piezas
print('Ingrese el largo de las piezas')
lado_1, lado_2, lado_3 = float(input('pieza #1: ')), float(input('pieza #2: ')), float(input('pieza #3: '))

#--- se comprubeba si se puede realizar el tejado (triangulo)
# la suma de 2 lados debe ser mayor que el lado restante
if lado_1 < lado_2 + lado_3:
    print('Usted puede construri el tejado. ¡great!')
elif lado_2 < lado_1 + lado_3:
    print('Usted puede construri el tejado. ¡great!')
elif lado_3 < lado_1 + lado_2:    
    print('Usted puede construri el tejado. ¡great!')
else: 
    print('Usted no puede construir el tejado. sorry')    