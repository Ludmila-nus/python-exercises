'''SISTEMA DE RESERVAS DE VUELOS 
Imagina que estás desarrollando un sistema de reservas de vuelos para una 
aerolínea. Crea un sistema de clases que permita a los usuarios realizar 
reservas de vuelos. Aquí tienes una posible estructura: 
- Clase base: `Vuelo` 
  - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de 
pasajeros 
  - Métodos: agregar pasajero, verificar disponibilidad de asientos 
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`) 
  - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, 
trabajo) 
Resuelve el problema creando instancias de estas clases y realizando 
reservas para diferentes vuelos y tipos de vuelos especiales. '''


class Vuelo:
    """Esta clase representa un vuelo con su información asociada, capacidad de pasajeros y asientos disponibles."""

    def __init__(self, numero_vuelo, origen, destino, capacidad_max):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_max = capacidad_max
        self.lista_pasajeros = []  # Inicializamos la lista de pasajeros
        self.lista_asientos = []  # Inicializamos la lista de asientos disponibles
        self.asientos = {}  # Inicializamos el diccionario de asientos

        for numero in range(1, self.capacidad_max + 1):
            self.lista_asientos.append(numero)  # Llenamos la lista de asientos
            self.asientos[numero] = {'disponible': True}  # Llenamos el diccionario de asientos

    def agregar_pasajero(self, pasajero, dni):
        self.lista_pasajeros.append({'Nombre pasajero': pasajero, 'DNI': dni})
        print(f'El pasajero {pasajero} DNI n° {dni}, se ha agregado con exito al vuelo {self.numero_vuelo}')

    def asiento_disponible(self):
        asientos_disponibles = [numero for numero, asiento in self.asientos.items() if asiento['disponible']]
        print(f'Listado de asientos disponibles: {asientos_disponibles}')

    def seleccionar_asiento(self, asiento):
        if asiento in self.asientos and self.asientos[asiento]['disponible']:
            self.asientos[asiento]['disponible'] = False
            print(f'Usted ha seleccionado el asiento n° {asiento}')
        else:
            print(f'El asiento n° {asiento} no está disponible o no existe')

class VueloEspecial(Vuelo):
    """Esta clase representa los motivos del vuelo"""
    def __init__(self, numero_vuelo, origen, destino, capacidad_max):
        super().__init__(numero_vuelo, origen, destino, capacidad_max)
        
    def motivo_vuelo(self, motivo):
        self.lista_motivos = ['vacaciones', 'trabajo', 'negocios', 'turismo', 'estudios', 'salud', 'otros']

        motivo_viaje = [motivos for motivos in self.lista_motivos if motivos == motivo]

        if motivo_viaje:
            print(f'El motivo de su viaje es {motivo_viaje[0]}')
        else:
            print('Motivo no válido')


# Ejemplo de uso
vuelo = Vuelo(1510, 'Cordoba', 'Brazil', 400)
vuelo.asiento_disponible()
vuelo.seleccionar_asiento(150)
vuelo.agregar_pasajero('Ludmila Nussio', 31668464)

vuelo_especial = VueloEspecial(1520, 'Cordoba', 'Buenos Aires', 200)  # Crea una instancia de la clase Vuelo
vuelo_especial.motivo_vuelo('trabajo')  # Llama al método con un motivo
