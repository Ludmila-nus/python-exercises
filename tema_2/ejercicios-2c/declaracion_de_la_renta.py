'''Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros 
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA TIPO IMPOSITIVO
Menos de 15.000 eu 5%
Entre 15.000 y 25.000 eu 15%
Entre 25.000 y 35.000 eu 20%
Entre 35.000 y 60.000 eu 30%
Más de 60.000 eu 45%
 
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo 
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.'''

#--- se le pregunta al usuario cuantos alos tiene
edad_usuario = int(input('¿Cuantos años tiene?: '))
#--- se le pregunta cual es su renta anual
renta_usuario = float(input('¿Cual es su renta anual?: '))
#--- se comprueba si debe tributar o no y lo imprimimos por pantalla
if edad_usuario > 18:#comprobamos si es mayor de edad 
    if 1000 < renta_usuario <= 15000: #Menos de 15.000 eu 5%
        impuesto = renta_usuario * 0.05
        print('usted debe pagar', impuesto, 'euros')
    elif 15000 < renta_usuario <= 25000: #Entre 15.000 y 25.000 eu 15%
        impuesto = renta_usuario * 0.15
        print('usted debe pagar', impuesto, 'euros')   
    elif 2500 < renta_usuario <= 35000: #Entre 25.000 y 35.000 eu 20%
        impuesto = renta_usuario * 0.20
        print('usted debe pagar', impuesto, 'euros')  
    elif 30000 < renta_usuario <= 60000: #Entre 35.000 y 60.000 eu 30%
        impuesto = renta_usuario * 0.30
        print('usted debe pagar', impuesto, 'euros')
    elif renta_usuario > 60000: #Más de 60.000 eu 45%
        impuesto = renta_usuario * 0.45
        print('usted debe pagar', impuesto, 'euros')
else:
    print('Usted no debe tributar')   