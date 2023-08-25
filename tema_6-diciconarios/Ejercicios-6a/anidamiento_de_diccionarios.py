# 22.  Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada representa un producto y tiene a su vez las 
#claves "nombre" y "precio" con sus respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada producto. 
productos= {
    'producto1': {
        'nombre':'galletitas',
        'precio':'300',
    },
    'producto2':{
        'nombre':'alfajores',
        'precio':'200',
    }
}
for producto, producto_info in productos.items():
    print('\nproducto: ' + producto)
    nombre_producto = producto_info['nombre']
    precio_producto = producto_info['precio']
    print('\tnombre del producto: '+ nombre_producto)
    print('\tprecio del producto: '+ precio_producto)



# 23.  Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor. Imprime el diccionario actualizado.
productos['producto3']={'nombre':'chocolates','precio':'250'}
print(productos)

# 24. Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada representa un equipo deportivo y tiene las 
#claves "nombre" y "jugadores" con sus respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de 
#los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores.  
athletics=['ludmila','romina','sofia','valeria','noeli','marina','monica']
las_rojas=['sofia','victoria','silvina','lucrecia','florencia','laura','yamila']
matienzo=['sofia','veronica','romina','marina','soldedad','guadalupe','betiana']
corral_de_bustos=['lucrecia','fernanda','ludmila','marina','noeli','silvina','valeria']
equipos={
    'equipo1':{
        'nombre':'atlethics',
        'jugadoras':athletics
               },
    'equipo2':{
        'nombre':'las_rojas',
        'jugadoras':las_rojas
    },
    'equipo3':{
        'nombre':'matienzo',
        'jugadoras':matienzo
    }}

for equipo, info_equipo in equipos.items():
    print('\nEquipo numero: ' + equipo)
    nombre_equipo= info_equipo['nombre']
    jugadoras_equipo= info_equipo['jugadoras']
    print('\tNombre del equipo: ' + nombre_equipo )
    print('\tNombre de las jugadoras: ', jugadoras_equipo)

# 25. Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor. La lista de jugadores debe contener 
#al menos tres nombres. Imprime el diccionario actualizado. 
equipos['equipo4']={'nombre':'corral_de_bustos','jugadoras':corral_de_bustos}

# 26. Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario 
#"equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado. 
athletics.append('samanta')

for equipo, info_equipo in equipos.items():
    print('\nEquipo numero: ' + equipo)
    nombre_equipo= info_equipo['nombre']
    jugadoras_equipo= info_equipo['jugadoras']
    print('\tNombre del equipo: ' + nombre_equipo )
    print('\tNombre de las jugadoras: ', jugadoras_equipo)