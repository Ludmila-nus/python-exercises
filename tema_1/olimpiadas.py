'''En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:
Hannah Neise: 8 minutos 3 segundos y 10 centésimas
Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas'''

# script que pida los tiempos por pantalla para cada uno de los finalistas
print('Ingrese el tiempo del atleta Hannah Neise')
minutos = input('minutos: ')
segundos = input('segundos: ')
centesimas = input('centesimas: ')
# Convierte los tiempos de minutos-segundos-centésimas a segundos
hannahTiempo = float(minutos) * 60 + float(segundos) + float(centesimas) * 0.01
print('El tiempo en segundos de la atleta es: ' + str(hannahTiempo))

print('Ingrese el tiempo del atleta Jackie Narracott')
minutos = input('minutos: ')
segundos = input('segundos: ')
centesimas = input('centesimas: ')
# Convierte los tiempos de minutos-segundos-centésimas a segundos
JackieTiempo = float(minutos) * 60 + float(segundos) + float(centesimas) * 0.01
print('El tiempo en segundos de la atleta es: ' + str(JackieTiempo))

print('Ingrese el tiempo del atleta Kimberley Bos')
minutos = input('minutos: ')
segundos = input('segundos: ')
centesimas = input('centesimas: ')
# Convierte los tiempos de minutos-segundos-centésimas a segundos
KimberleyTiempo = float(minutos) * 60 + float(segundos) + float(centesimas) * 0.01
print('El tiempo en segundos de la atleta es: ' + str(KimberleyTiempo))

# Sabiendo que la pista es de 100 metros calcula la velocidad media de c/u en m/seg
VelocMediaHannah = 1 * float(hannahTiempo) / 100 
VelocMediaJackie = 1 * float(JackieTiempo) / 100
VelocMediaKimberley = 1 * float(KimberleyTiempo) / 100

# Imprime los resultados por pantalla
print('La velocidad media  en m/seg de cada participante fue de: ')
print('Hannah Neise: ' + str(VelocMediaHannah))
print('Jackie Narracott: ' + str(VelocMediaJackie))
print('Kimberley Bos: ' + str(VelocMediaKimberley))