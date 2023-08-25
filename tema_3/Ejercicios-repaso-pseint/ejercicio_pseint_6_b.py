'''Pedir  un  número  (entero)  y  calcular  qué  números  desde  el  1  hasta  el  propio  número 
son múlEplos de 2 y 3. 
  Recordatorio: un número es múlEplo de 2 si al dividir por 2, el resto es 0; y es múlEplo   
  de 3 si al dividir por 3, el resto es 0 
  Ejemplo: dado el número 15, los números múlEplos de 2 y 3 hasta 15 son 6 y 12 (resto   
  0 en ambas divisiones) 
'''

#--- pedimos un numero por pantalla
numero = int(input('ingrese un numero: '))
multiplos_comunes = []

#--- calculamos que numero hay del 1 hasta el "numero del usuario" que sean multiplos de 2 
for i in range(1,(numero+1)):    
    multiplo_2 = i % 2
    multiplo_3 = i % 3
    if multiplo_2 == 0 and multiplo_3 == 0:
       multiplos_comunes.append(i)
print('los multiplos de 2 y 3 hasta', numero, 'son', multiplos_comunes)       