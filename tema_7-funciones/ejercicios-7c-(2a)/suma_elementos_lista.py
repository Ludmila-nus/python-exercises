'''SUMA ELEMENTOS DE UNA LISTA 
Crea una función recursiva llamada suma_lista que calcule la suma de todos 
los lista de una lista de enteros. Puedes asumir que la lista no está 
vacía. '''


def suma_lista(lista):

    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

lista_a = [1,2,3,4,5]
suma = suma_lista(lista_a)
print(suma)