''' Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es "sbc56", el output deberá ser "ssbbcc5566" '''

#ingresa por pantalla un string de 5 caracteres
palabra = input('Ingrese un string de 5 caracteres: ')

#devuelve otro string de caracteres duplicados
print(palabra[0] + palabra[0] + palabra[1] + palabra[1] + palabra[2] + palabra[2] + palabra[3] + palabra[3] + palabra[4] + palabra[4])