#--- contraseña correcta 
contaseña_guardada = 'holamanola'

#--- pedimos al usuario que ingrese la contraseña
contraseña_pedida = input('Usted debe ingresar su contraseña: ')

# no distingue entre mayusculas y minusculas
contraseña_pedida = contraseña_pedida.lower()
contraseña_pedida = ''
#--- si la contraseña es correcta le damos la bienvenida
if contaseña_guardada == contraseña_pedida:
    print('¡Bienvenida a tu sistema!')
#--- si la contraseña es incorrecta le damos otra oportunidad de ingresala
elif contaseña_guardada != contraseña_pedida:
    contraseña_pedida = input('Usted ingreso una contraseña equivocada; vuelva a intentarlo: ')
    contraseña_pedida = contraseña_pedida.lower() # vuelvo a darle la condicion de no distingir may y min
    if contaseña_guardada == contraseña_pedida:
        print('¡Bienvenida a tu sistema!')
    # segundo fallo le damos un mensaje de error 
    elif contaseña_guardada != contraseña_pedida:
        print('Contraseña incorrecta, no tiene mas intentos')