'''Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información: 
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 ... Por ejemplo: 
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos, 
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e 
imprimir la nota media de los alumnos junto con el DNI.  

Supón ahora que tu input es un string como este:  
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n 
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’ 

Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI 
de todos los alumnos en ese string. '''

# --- lista con los datos de los alumnos
#lista = [['David Fernandez','12311267A'],['Maria Garcia','12316487A'],['Juan Perez','647829236A']]

# --- creamos una lista pidiendo datos del alumno (nombre y dni)
lista_alumnos = []
otro_alumno = 'si'
while otro_alumno == 'si':
    nombre = input('Nombre del alumno:  ')
    dni = input('DNI del alumno:  ')
    lista_alumnos.append([nombre,dni])
    otro_alumno = input('Hay mas alumnos para cargar en la base de datos. Responda si /no:  ')
print('')
# --- agregamos a la lista de alumnos: código_asignatura, convocatoria, nota1, nota2, nota3
# --- pedimos el dato de la materia por pantalla
print('ingrese los datos de la materia')
codigo_asignatura = input('Codigo de la asignatura:  ')
convocatoria = input('convocatoria numero:  ')

# --- agregamos a la lista los datos de la materia y preguntamos las notas de cada alumno
promedio = []
lista_otro_alumnoal = []
for i in range(0,len(lista_alumnos)):
    print(f'Ingrese la nota del alumno {lista_alumnos[i]}')
    lista_alumnos[i].append(codigo_asignatura)
    lista_alumnos[i].append(convocatoria)
    nota = float(input('Ingrese la nota 1:  '))
    lista_alumnos[i].append(nota)
    nota = float(input('Ingrese la nota 2:  '))
    lista_alumnos[i].append(nota)
    nota = float(input('Ingrese la nota 3:  '))
    lista_alumnos[i].append(nota)
    # --- sacamos el promedio de cada alumno (sumamos las materias y las dividimos por 3 )
    promedio_individual = ((sum(lista_alumnos[i][4:])/3))
    # --- agregamos el DNI del alumno y el promedio a una nueva lista
    lista_otro_alumnoal.extend([[lista_alumnos[i][1],promedio_individual]])
    
# -- imprimimos por pantalla el DNI del alumno y el promedio
print('')
print(f'Para la materia codigo: {codigo_asignatura}, en la convocatoria: {convocatoria}')
print('Lista de alumnos (DNI) y sus promedios')
for i in range(0,len(lista_otro_alumnoal)):
    print(f'Alumno DNI: {lista_otro_alumnoal[i][0]} , nota promedio: {lista_otro_alumnoal[i][1]:.2f}')    



