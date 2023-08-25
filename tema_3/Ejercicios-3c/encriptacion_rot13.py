'''El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se 
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma 
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y 
catalán la ”Ç”, en alemán la ”ß”, etc.).  
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos 
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario 
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta 
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el 
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual. 
'''

from termcolor import colored

'''1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto 
codificado según el cifrado ROT13 '''

#--- creamos una lista con el abecedario
#abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abc = 'abcdefghijklmnopqrstuvwxyz'
#--- creamos una lista con el cifrado ROT13
#rot13 = ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
rot13 = 'nopqrstuvwxyzabcdefghijklm'
#--- pedir por pantalla una cadena de caracteres (una frase)
texto_1 = input('Ingrese una frase: \n')
largo_texto_1 = len(texto_1)
#--- devolver el texo codificado según el cifrado ROT13 
texto_codificado = ''

for i in range(len(texto_1)):
    for j in range(len(abc)):
        if texto_1[i] == abc[j]:
            texto_codificado += rot13[j]
    if texto_1[i] != abc[j]:
        texto_codificado += texto_1[i]


# imprimimos por pantalla el texto resultante
print('El texto codificado a ROT13 es:',colored(texto_codificado,'magenta'))

'''2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas 
esta codificación ROT13 de la otra.'''

#--- comprobamos si el texto_codificado es la codificacion ROT13 del texto_1
nuevo_texto = ''
for i in range(0,len(texto_codificado)):
    for j in range(0,len(rot13)):
        if texto_codificado[i] == rot13[j]:
            nuevo_texto += abc[j]
    if texto_codificado[i] == ' ':
        nuevo_texto += ' '
# print(nuevo_texto)

if nuevo_texto == texto_1:
    print((f'El texto: \n'),(colored(f'{texto_codificado}','blue')),('\n es la codificacion ROT13 del texto \n'),(colored( f'{texto_1}','blue')))
else:
    print((f'El texto: \n'),(colored(f'{texto_codificado}','red')),('\n no es la codificacion ROT13 del texto \n'),(colored( f'{texto_1}','red')))



   
#--- tomamos dos textos nuevo y comparamos si uno es la codificacion ROT13 del orto
