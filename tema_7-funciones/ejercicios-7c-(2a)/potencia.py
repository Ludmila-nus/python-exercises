'''POTENCIA 
Implementa una función recursiva llamada potencia que calcule el resultado 
de elevar un número a una potencia dada. Puedes asumir que tanto el 
número como la potencia son enteros no negativos. '''

# importamos modulos
from functools import lru_cache

# damos el tamaño al cache
@lru_cache(maxsize=100)

def potencia(base, exponente):
    """La funcion dara el resultado de un numero elevado a una potencia dada"""
    
    if exponente == 0:
        return 1
    else:
        return base * (potencia(base, exponente-1))
    

resultado = potencia(2,5)   
print(resultado) 