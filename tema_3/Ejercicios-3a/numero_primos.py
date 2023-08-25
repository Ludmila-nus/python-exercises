'''Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es 
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1 
o sí mismo'''

#--- creamos un bulce que recorra todos los numero del 2 al 100

lista_numeros = []
numeros = 2
for i in range(2, 101):
  if (numeros % i != 0):
    lista_numeros.append(numeros)
    numeros = numeros + 1
print(f'Los numeros primos del 2 al 100 son {lista_numeros}')
