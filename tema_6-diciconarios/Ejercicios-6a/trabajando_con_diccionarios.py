'''TEMA: DICCIONARIOS
OBJETIVO: FAMILIARIZACIÓN CON EL USO DE DICCIONARIOS, SUS CARACTERÍSTICAS Y METODOS ASOCIADOS
EJERCICIOS 6A: TRABAJANDO CON DICCIONARIOS:'''

# 1. Crea un diccionario vacío llamado “mi_diccionario”. 
mi_diccionario = {}

# 2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor  sea tu nombre.
mi_diccionario['nombre'] = 'ludmila'

# 3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario".   
print(mi_diccionario.values())

# 4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" en caso contrario.  
print('edad' in mi_diccionario)
        
# 5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor: "nombre" con el nombre del alumno, "edad" 
#con su edad y "materia" con su materia favorita.  
estudiante = {'nombre': 'ludmila', 'edad': '37', 'materia':'programacion'}
print(estudiante)

# 6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad actual de tu amigo.  
estudiante['edad'] = '38'
print(estudiante)

# 7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante". 
estudiante.pop('materia')

# 8. Imprime todas las claves en el diccionario “estudiante".  
print(estudiante.keys())

# 9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor 
#"1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor “5555555555”.  
agenda={'juan':'123456789', 'joana':'9876543210', 'jimena':'5555555555' }

# 10. Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor “9998887777". 
agenda['julio'] = '9998887777'

# 11. Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".  
print(agenda.items())

# 12. Crea una lista llamada "claves" que contenga todas las claves del diccionario “agenda".  
claves= [agenda.keys()]

# 13. Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario.     
print('juan' in agenda)

# 14. Elimina la entrada con la clave “Jimena”.  
agenda.pop('jimena')

# 15. Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e 
# imprime cada par clave-valor en el formato "Nombre: Número”.  
for clave, valor in agenda.items():
    print('Nombre', clave)
    print('numero', valor)

# 16. Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el 
#diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”. 
print(agenda.get('juan', 'clave no encontrada'))

# 17. Borra todas las entradas del diccionario “agenda”.
agenda.clear()
print(agenda)