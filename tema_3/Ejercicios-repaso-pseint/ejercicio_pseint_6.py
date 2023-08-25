'''Pedir  un  número  (entero)  y  calcular  qué  números  desde  el  1  hasta  el  propio  número 
son múlEplos de 2 y 3. 
  Recordatorio: un número es múlEplo de 2 si al dividir por 2, el resto es 0; y es múlEplo   
  de 3 si al dividir por 3, el resto es 0 
  Ejemplo: dado el número 15, los números múlEplos de 2 y 3 hasta 15 son 6 y 12 (resto   
  0 en ambas divisiones) 
'''

#--- pedimos un numero por pantalla
numero = int(input('ingrese un numero: '))

multiplos_2 = []
multiplos_3 = []
multiplos_comunes = []

#--- calculamos que numero hay del 1 hasta el "numero del usuario" que sean multiplos de 2 
for i in range(1,(numero+1)):    
    multiplo = i % 2
    if (multiplo == 0):
       multiplos_2.append(i)
print('Los numeros multiplos de 2 son: ', multiplos_2)       
#--- calculamos que numero hay del 1 hasta el "numero del usuario" que sean multiplos de 3       
for j in range(1,(numero+1)): 
    multiplo = j % 3
    if (multiplo == 0):
       multiplos_3.append(j)
print('Los numeros multiplos de 3 son: ', multiplos_3)         
#--- comparamos las dos listas con multiplos y sacamos los numero iguales
for a in multiplos_2:
  for b in multiplos_3:
    if a == b:
      multiplos_comunes.append(a)

      
print('Los numeros multiplos de 2 y 3 hasta', numero, 'son:', multiplos_comunes)