'''NUMERO TRIANGULAR 
Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
número triangular. Un número triangular se obtiene al sumar todos los 
números naturales desde 1 hasta n.'''


def numero_triangular(numero):

    if numero == 1:
        return numero
    
    else:
        return( numero + numero_triangular(numero-1))
    

valor = numero_triangular(10)    
 
print(valor) 