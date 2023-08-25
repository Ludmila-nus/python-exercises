'''GESTIÓN DE EMPLEADOS: 
Imagina que eres el gerente de recursos humanos de una empresa y 
necesitas gestionar la información de los empleados. Cada empleado 
tiene un nombre, salario y departamento al que pertenece. Implementa 
un programa en Python que permita agregar nuevos empleados, 
actualizar el salario de un empleado existente, mostrar la lista completa 
de empleados y calcular el promedio salarial por departamento'''

# comenzamos con un diccionario vacio
info_empleados = {}

# cargamos los empleados (nombre, salario y departamento al que pertenecen)
continuar = True
while continuar:
    # damos las opciones del sistema 
    opcion = input('\nSeleccione una opcion: \n\t1- Agregar empleado nuevo \n\t2- actualiza salario de empleado existente \n\t3- Mostrar lista compelta de empleados \
          \n\t4- Calcular el promedio salarial por departamento \n\t5- Salir \n\t :')
    # opcion 1 agregar empleado nuevo
    if opcion == '1':
        # pedimos por pantalla nombre, departamento y salario del empleado nuevo
        nombre = input('Ingrese el nombre del empleado: ')
        departamento = input(f'Ingrese el departamento al que pertenece el empleado {nombre}: ')
        salario = int(input(f'Ingrese el salario del empleado {nombre}: '))
        # cargamos los datos proporcionados en el diccionario
        info_empleados[nombre] = {
            'salario':salario,
            'departamento':departamento
        }
        # mostramos por pantalla los datos cargado
        print(f'Los datos ingresados son: \n\tNombre del empleado: {nombre} \n\tDepartamento: {departamento} \n\tSalario: {salario}')
    # opcion 2 actualizar salario de empleado ya cargado
    elif opcion == '2':
        nombre = input('Ingrese el nombre del empleado para actualizar su salario: ')
        if nombre in info_empleados:
            salario = int(input(f'Ingrese el salario actualizado del empleado {nombre}: ')) 
            info_empleados[nombre] = {
            'salario':salario,
            }
            print(f'El salario del empleado {nombre} se ha actualizado a {salario}')
        else:
            print(f'El empleado {nombre} no se encuentra registrado en el sistema')   

    # opcion 3 se muestra una lista completa de los empleados cargados en el sistema
    elif opcion == '3':     
        print('Lista de empleados: ')   
        for empleado, datos in info_empleados.items():
            salario_empleado = datos['salario']
            dpto_empelado = datos['departamento']
            print(f'\nEmpleado: {empleado} \tSalario: {salario_empleado} \tDepartamento: {dpto_empelado}')

    # opcion calcular el promedio salarial por departamento
    elif opcion == '4':
        dpto_promedio = input('Ingrese el departamento del cual quiere el promedio salarial: ')
        contador = 0
        print(info_empleados)
        #if dpto_promedio in info_empleados:
        suma_salarios = sum(info_empleados['nombre']['salario'])
        contador += 1
       # else:
        #print(f'El departamento {dpto_promedio} no se encuentra en el sistema')
                


        