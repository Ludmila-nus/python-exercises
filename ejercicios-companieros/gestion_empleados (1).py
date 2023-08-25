'''Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento.'''
info_empleados = {}
info = True
while info:
    opcion = input("1. Registrar empleado\n2. Actualizar salario\n3. Calcular el promedio salarial por departamento\n4. Salir\nElige una opción: ")
    if opcion == "1":

        nombres = input("Ingresa tu nombre: ")
        salario = float(input("Ingresa tu salario: "))
        departamento = input("Ingresa tu departamento: ")
        info_empleados[nombres] = {
            "salario": salario,
            "departamento": departamento
        }
        for nombres, datos_empleado in info_empleados.items():
            salario = datos_empleado["salario"] # extraemos valor del salario
            departamento = datos_empleado["departamento"] # extraemos departamento
        print(f"Nombre: {nombres}, Salario: {salario}, Departamento: {departamento}")         
    elif opcion == "2":
        nombres = input("Ingrese el nombre del empleado a actualizar el salario: ")
        if nombres in info_empleados:
            nuevo_salario = float(input("Ingrese el nuevo salario: "))
            info_empleados[nombres] = nuevo_salario
            print(info_empleados)
        else:
            print("El empleado no existe en la base de datos.")
    elif opcion == "3":
        total_salario = 0
        promedio = 0
        departamento = input("Ingrese el departamento: ")
        contador = 0
               
        for datos_empleado in info_empleados.values():
            if datos_empleado["departamento"] == departamento:
                total_salario = total_salario + datos_empleado["salario"]
                contador = contador + 1
        if contador > 0:
            promedio = total_salario / contador
            print("El promedio salarial por departamento es: ", promedio)
        else:
                print("No hay empleados en ese departamento.")            

    elif opcion == "4":
        info = False
        print("Saliendo del programa...")
        

    # Si el numero introducido no es 1,2,3,4 pedimos que se elija
    # una opcion valida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
        
