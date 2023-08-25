'''Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con 
los números primos de la lista original. Además, el script debe devolver el número total de 
números primos encontrados y la suma de los números primos encontrados'''

from termcolor import colored 

#--- creamos una lista de numeros enteros
lista_numeros = [list(range(2,101))]
print(colored(f'Lista de numeros {lista_numeros}','blue'))
#--- devolvemos los numeros primos de esa lista
lista_numeros_primos = [ ] 

for num in range(2,101):
    primo = True
    for i in range(2,num):
        if (num % i == 0):
            primo = False
    if primo:
        lista_numeros_primos.append(num) # los agrupamos en una lista de numeros primos
print(colored(f'Lista de numeros primos {lista_numeros_primos}', 'magenta'))       
#--- devolvemos la cantidad de numeros primos que hay
print(colored(f'La cantidad de numeros primos en la lista son: {len(lista_numeros_primos)}','magenta'))
#--- sumamos los numeros primos encontrados
print(colored(f'La suma de numeros primos en la lista da un total de: {sum(lista_numeros_primos)}','magenta'))