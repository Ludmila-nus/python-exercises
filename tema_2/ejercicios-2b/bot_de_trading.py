'''Un bot de trading está programado para realizar ciertas acciones con respecto a un producto 
financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del 
producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está 
entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está 
estrictamente por encima de 150 el bot deberá imprimir la orden de vender.'''

#--- el usuario introduce el precio que necesita
precio_usuario = float(input('Ingrese el precio en dolares que necesita: '))

#--- el script le devuelve que se orden se ejecutara
if precio_usuario < 100: # precio < 100 usd, orden de compra
    print('orden de compra al precio', precio_usuario, 'dolares')
elif 100 <= precio_usuario <= 150:  # precio >= 100 usd <= 150, orden hold
    print('orden hold al precio', precio_usuario, 'dolares')
elif precio_usuario > 150: # precio > 150 usd, orden de venta
    print('orden de venta al precio', precio_usuario, 'dolares')
