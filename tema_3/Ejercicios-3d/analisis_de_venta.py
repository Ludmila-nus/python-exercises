'''Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los 
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor 
venta.'''

from termcolor import colored

# --- creamos dos listas
# 1-ventas del mes
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250] 
# 2- dias de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# --- convertimos la lista de dias en una lista anidada
dias = []
for dia in dias_semana:
    dias.append([dia])
# print(dias)    

# --- creamos una lista con los promedios por dia
# creamos una lista vacia para ubicar los promedios por dia de la semana(7 dias)
ventas_por_dia = [0,0,0,0,0,0,0] 
# creamos un contador de dias que usaremos para reiniciar el bucle a los 7 dias
dia_numero = 0
# obtenemos la suma de ventas por dia
for venta in ventas:
    ventas_por_dia[dia_numero] +=venta
    dia_numero += 1
    # condicional para que vuelva a lunes
    if dia_numero == 7:
        dia_numero = 0

dia_total_ventas = []
for i in range(7):
    dia_total_ventas.append([[ventas_por_dia[i],dias[i]]])
print(dia_total_ventas)

print(('Las ventas promedio por dia son:'))
for i in range(7):     
    print(colored(f'dia {dias_semana[i]}: {ventas_por_dia[i]} EU.','blue'))
print(colored(f'El dia con mayores ventas {max(dia_total_ventas)}','magenta'))    
