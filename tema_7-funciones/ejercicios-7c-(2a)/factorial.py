# importamos modulos
from functools import lru_cache

# damos el tamaño al cache
@lru_cache(maxsize=100)

def factorial(numero):
    """funcion que calcula el factorial de un numero positivo entero"""
    
    # si el resultado es el numero multiplicado por si mismo
    resultado = 1
    if resultado == numero * numero:
        return resultado
    # sino llamamos nuevamente a la funcion dandole como parametro la multiplicacion del numero por el 
    # numero menos 1
    else:
        return(numero * factorial(numero-1))
    

resultado = factorial(10)    
print(resultado)