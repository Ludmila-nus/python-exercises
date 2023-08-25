# 18. Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario 
#representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos 
#valores. Recorre la lista e imprime el nombre y edad de cada estudiante.  
estudiante1= {
              'nombre':'juan',
              'edad':'23',
              }
estudiante2 = {
              'nombre':'pedro',
              'edad':'22',
              }
estudiantes=[estudiante1,estudiante2]
print(estudiantes)

# 19. Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las 
#mismas claves "nombre" y "edad". Imprime la lista actualizada.  
estudiante3 = {'nombre':'lola',
              'edad':'22',
              }
estudiantes.append(estudiante3)
print(estudiantes)

#20. Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada. 
estudiantes.remove(estudiante2)
print(estudiantes)

#21. Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. 
#Imprime la lista actualizada
estudiante1['edad'] = '25'
print(estudiantes)
