'''Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma 
de los otros dos.'''

#--- pedir al usuario 3 numeros
print('Ingrese 3 numeros')
num_1 = int(input('#1: '))
num_2 = int(input('#2: '))    
num_3 = int(input('#3: '))    

#--- comprobar si alguno es la suma de los otros dos
if num_1 == num_2 + num_3:
    print('El numero', num_1, 'es la suma de los numeros', num_2, 'y', num_3)
elif num_2 == num_1 + num_3:
    print('El numero', num_2, 'es la suma de los numeros', num_1, 'y', num_3)
elif num_3 == num_1 + num_2:
    print('El numero', num_3, 'es la suma de los numeros', num_1, 'y', num_2)
else:
    ('Ningun numero es la suma de los otros dos')
