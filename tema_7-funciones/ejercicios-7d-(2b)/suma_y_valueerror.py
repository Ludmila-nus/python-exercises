'''Un problema común al solicitar una entrada numérica ocurre cuando las 
personas ingresan texto en lugar de números. Cuando intentas convertir la 
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que 
solicite dos números. Suma los números y muestra el resultado. Captura el 
ValueError si alguno de los valores de entrada no es un número e imprime un 
mensaje de error amigable. Prueba tu programa ingresando dos números y 
luego ingresando texto en lugar de un número. Envuelve tu código del en un 
bucle while para que el usuario pueda continuar ingresando números incluso 
si comete un error ingresando texto en lugar de un número. '''

#--script solicita dos numeros los suma y devuelve el resultado
   
# el bucle continua si ingresa algun valor de entrada no es un numero
while True:
     
    try: 
        # pedimos al usuario que ingrese dos numeros por pantalla
        num1 = input('Ingrese el primer numero: ')
        num2 = input('Ingrese el segundo numero: ')

        # sumamos los numeros
        resultado = int(num1) +  int(num2)

        # si ingreso dos valores numericos se imprime el resultado   
        print(f'El resultado de la suma de los numeros ingresados es {resultado}')
        break

    # si no ingreso numeros le damos el mensje de error y pedimos que ingrese los numeros nuevamente    
    except ValueError:
        print('Ingreso invalido. Usted debe ingresar un numero.')    

    
        
        
