'''CUENTA BANCARIA 
Crea una clase "CuentaBancaria" con atributos como número de cuenta y 
saldo. Implementa métodos para depositar y retirar dinero, y muestra el 
saldo actual.'''


class CuentaBancaria:
    def __init__(self, nro_cta, saldo):
        self.nro_cta = nro_cta
        self.saldo = saldo

    def details(self):    
        accion = input('Que accion necesita realizar? /n 1: depositar dinero /n 2: rerirar dinero /n 3: mostrar el saldo actual /n 4: salir \
                       Ingrese el numero de la accion seleccionada: ')
        if accion == '1':
            deposito = float(input('¿Cuanto dinero va a depositar?: '))
            ok = input('ingrese ok si desea seguir con el deposito: ')
            if ok.lower() == 'ok':
                print('Su deposito se ha realizado correctamente')
                saldo = self.saldo + deposito
                print(f'Su saldo actual es: {saldo}')
            else:
                print('La accion ha sido cancelada')    
        if accion == '2':
            reriro = float(input('¿Cuanto dinero va a rerirar?: '))
            ok = input('ingrese ok si desea seguir con el reriro: ')
            if ok.lower() == 'ok':
                print('Su reriro se ha realizado correctamente')
                saldo = self.saldo - reriro
                print(f'Su saldo actual es: {saldo}')
            else:
                print('La accion ha sido cancelada')     
        if accion == '3':
            print(f'su saldo actual es: {self.saldo}')      
        if accion == '4':
            print('Gracias por usar nuestros servicios bancarios. Hasta luego.')

cuenta = CuentaBancaria('123456789',100000)
cuenta.details()