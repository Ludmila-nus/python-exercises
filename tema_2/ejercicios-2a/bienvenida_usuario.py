#--- pedir el nombre al usuario
nombre = input('Introduzca su nombre: ')

#---controlamos minus/may - . - # introducidos erroneamente
nombre = (nombre.replace('.','').replace('#','').title()) 
print(nombre)

#--- damos una bienvenida personalizada
# si es alejandro - saludamos a Alejandro
if nombre == 'Alejandro':
    print('¡Bienvenido ', nombre, '!')
# si es Naomi - saludamos a Nahomi
elif nombre == 'Naomi':
    print('¡Bienvenido ', nombre, '!')
# si es Sergio - saludamos a Sergio
elif nombre == 'Sergio':
    print('¡Bienvenido ', nombre, '!')
# si es un invitado - saludamos genericamente
else: 
    print('¡Bienvenido invitado!')
