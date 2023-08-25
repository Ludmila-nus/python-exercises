#--- usuario debe ingresar una contraseña (segura 1 vocal minuscula, 2 simbolos * y #)
contraseña = input('Ingrese una contraseña, asegurese de que contenga: \n 1 vocal minuscula\
     \n 2 simbolos especiales diferentes * y # \n:')

#--- comprobamos si la contraseña cuenta con lo requerido
if ('*' in contraseña) and ('#' in contraseña) and (('a' in contraseña) or ('e' in contraseña )\
 or ('i' in contraseña) or ('o' in contraseña) or ('u' in contraseña)):
    print('su contraseña es segura') #devolvemos si la contraseña es segura
else:
    print('contraseña insegura') #devolvemos si la contraseña no es segura
