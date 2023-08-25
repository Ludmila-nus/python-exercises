'''Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en 
ese caso imprima dos listas correspondientes a: 
1. La columna cuyos elementos suman el máximo 
2. La columna cuyos elementos suman el máximo 
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo: 
M1=[[2,5,3],[6,1,8],[7,5,4]]  devolverá: L1 = [7,5,4] y L2 = [2,6,9,7] 
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = [] 
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo 
numero de objetos)'''


from termcolor import colored

#--- creamos una lista numerica matriz
matriz_1=[[2,5,3],[6,1,8],[7,5,6]] 
print(colored(f'Matriz 1 formada por:{matriz_1}','red'))
#--- creamos una lista numerica comun
#matriz_2 = [[4,2,3],[4,5],[6,8,2]]
#print(colored(f'Matriz 2 formada por:{matriz_2}','blue'))

# --- comprobamos que sea una matriz
n_columnas = len(matriz_1[0])
matriz = True
for i in range(0,len(matriz_1)):       
        if len(matriz_1[i]) != n_columnas:
            matriz = False 


# --- si es una matriz realizara los calculos
if matriz == True:              
    # -- determinamos que fila suma el maximo 	
    filas = []
    suma_filas = []
    fila_max = [] 
    for i in range(0,len(matriz_1)):
        # --- sumamos los valores de cada fila y los agregamos a una nueva lista 
        suma_filas.append(sum(matriz_1[i]))
        # --- comparamos la suma de las filas y seleccionamos la que sume el valor mas alto
        if suma_filas[i] ==  max(suma_filas):  
            fila_max = matriz_1[i]
       
    # -- determinamos que columna suma el maximo 
    columnas = []
    cadena_columnas = []
    suma_columnas = []
    columna_max = []
    for i in range(0,len(matriz_1)):
        for columna in matriz_1:
        # --- obtenemos los valores de cada columna
             columnas.append(columna[i]) 
        # --- agregamos los valores de cada columna en una nueva lista   
        cadena_columnas.append(columnas)
        # --- sumamos los valores de cada columna y los agregamos a una nueva lista 
        suma_columnas.append(sum(columnas))
        # --- volvemos la columna a cero para poder separar los valores de cada columna
        columnas = [] 
        # --- comparamos las columnas y obtenemos la que tiene la suma de valores maxima  
        if suma_columnas[i] ==  max(suma_columnas):  
            columna_max = cadena_columnas[i]
else:
     print('No es una matriz.')        
# --- imprimimos por pantalla los resultados
if matriz == True:
   print('')
   print(colored(f'Fila cuyos elementos suman el maximo {fila_max}' , 'magenta'))
   print(colored(f'Columna cuyos elementos suman el maximo {columna_max}' , 'magenta'))
	
