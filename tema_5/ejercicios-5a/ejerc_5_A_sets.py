from termcolor import colored


# 14. Crea un set y elimina uno de sus elementos. 
mi_set_14 = {'manzana','banana','sandia','pera'}
print(mi_set_14)
mi_set_14.remove('banana')
print(mi_set_14)

# 15. Crea un set vacío. 
mi_set_15 = ()
print(mi_set_15)

# 16. Crea dos sets y encuentra su union, su intersección y su diferencia. 
mi_set_16_a ={5,8,10,12,12,15,15}
mi_set_16_b ={2,4,6,10,10,12,8,8}
#union
print(mi_set_16_a | mi_set_16_b)
print(mi_set_16_a.union(mi_set_16_b))
#interseccion
print(mi_set_16_a & mi_set_16_b)
print(mi_set_16_a.intersection(mi_set_16_b))
#diferencia
print(mi_set_16_a - mi_set_16_b)
print(mi_set_16_a.difference(mi_set_16_b))
# 17. Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos. 
# es lo mismo que interseccion
nuevo_set_17 = mi_set_16_a & mi_set_16_b
print(colored(f'{nuevo_set_17}','red'))

# 18. Crea un script que dado un set con números devuelva el numero máximo y mínimo. 
set_18 = {10,52,48,70,99}
maximo = max(set_18)
minimo = min(set_18)
print(maximo,minimo)

# 19. Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets. 
# es lo miso que union
nuevo_set_19 = mi_set_16_a | mi_set_16_b
print(colored(f'nuevo set {nuevo_set_19}','blue'))
# 20. Crea un set con colores y comprueba si cierto color se encuentra en el set. 
set_20 = {'rojo','amarillo','verde'}
print('azul' in set_20)
print('rojo' in set_20)

# 21. Crea un script que dados dos sets cree un nuevo set con los elementos que están en el primer set pero no en el segundo. 
# es lo mismo que resta
nuevo_set_21 = mi_set_16_a - mi_set_16_b
print(colored(f'mi nuevo set es {nuevo_set_21}','yellow'))
# 22. Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set. 
producto = 1 
for num in mi_set_16_a:
    producto *= num 
    print(producto)
print(colored(f'el resultado de la multiplicacion es: {producto}', 'magenta'))