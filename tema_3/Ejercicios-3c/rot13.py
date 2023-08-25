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


abc = 'abcdefghijklmnopqrstuvwxyz'
acb_mayuscula = abc.upper()
mensaje = 'hOlA'
mensaje_codificado = ''

# --- si el mensaje esta en minuscula
for letra in mensaje:
    for i in range(len(abc)):
        if letra == abc[i]:
            caracter_codificado = i + 13
            if caracter_codificado > 26:
                caracter_codificado = -26 + i + 13
            mensaje_codificado += abc[caracter_codificado]
print(mensaje_codificado)    

# -- si el mensaje esta en mayuscula
for letra in mensaje:
    for i in range(len(acb_mayuscula)):
        if letra == acb_mayuscula[i]:
            caracter_codificado = i + 13
            if caracter_codificado > 26:
                caracter_codificado = -26 + i + 13
            mensaje_codificado += acb_mayuscula[caracter_codificado]
print(mensaje_codificado)  
