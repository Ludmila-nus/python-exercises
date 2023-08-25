'''En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta ———————— 12 EU
Sopa de pescado ——————— 10 EU
Dorada al horno ———————— 18 EU
Arroz al curry ————————— 14 EU
Lasaña de carne ——————— 15 EU
Brownie de chocolate ————— 8 EU
Helado ——————————— 6 EU
Refrescos —————————— 5,5 EU
Café ———————————— 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta.'''

#menu elegido por el cliente, ingresa cantidades (se piden por pantalla) y se multiplica automaticamente por su precio
print('cantidad consumida por el cliente: ')
ensaladaMixta = float(input('Ensalada mixta: ')) * 12
sopaPescado = float(input('Sopa de pescado: ')) * 10
doradaHorno = float(input('Dorada al horno: ')) * 18
arrozCurry = float(input('Arroz al curry: ')) * 14
lasagnaCarne = float(input('Lasagna de carne: ')) * 15 
browniChoco = float(input('Browni de chocolate: ')) * 8
helado = float(input('Helado: ')) * 6
refrescos = float(input('Refrescos: ')) * 5.5
cafe = float(input('Cafe: ')) * 3.5

#total de la cuenta
suma_total = ensaladaMixta + sopaPescado + doradaHorno + arrozCurry + lasagnaCarne + browniChoco + helado + refrescos + cafe
print('El total de la cuenta es de: ' + str(suma_total))
