'''En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos 
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la 
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y 
R hasta la Z se les ha asignado al grupo A también, el resto están en el B. 
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por 
pantalla el grupo que le corresponde a ese alumno'''

#--- se le pregunta al usuario el sexo y el nombre
print('<<<<<<¡Bienvenido!>>>>>>>')
print('Usted debe responder unas preguntas para saber al grupo que pertenece')
sexo = input('¿De que sexo es? responda "F" para femenino o "M" para masculino:  ')
nombre = input('¿Cual es su nombre?:  ')
sexo = sexo.lower()
nombre = nombre.lower()

#--- se devuelve por pantalla el grupo al que corresponden
import string
list[string.ascii_lowercase]


if sexo == 'f' and nombre > 'e' and nombre < 'm': # chicas grupo A -- E / M -- resto grupo B
    print('Su grupo es el "A"')
else:
    print('Su grupo es el "B"')
if sexo == 'm' and nombre < 'h' and nombre > 'r': # chicos grupo A -- A / H y R / Z -- resto grupo B
   print('Su grupo es el "A"')
else:
    print('Su grupo es el "B"')
