# Iniciamos la matriz
m_1 = [[2,5,3],[6,1,8],[7,5,4]]

# obtenemos el numero de filas y columnas de la matriz para recorrerlas con el for
num_filas = len(m_1)
num_columnas = len(m_1[0])

# Iniciamos nuevas listas sum_filas y sum_columnas a cero y las multiplicamos por el valor de su longitud
# para asi poder tener los valores filas columnas por separado a la hora de las comprovaciones
sum_filas = [0] * num_filas
sum_columnas = [0] * num_columnas

# Verificamos si m_1 es una matriz ( Todas las filas deveran tener el mismo numero de columnas)
for i in range (num_filas):

    # Si alguna fila no tiene el mismo numero de columnas no sera una matriz y asignaremos  l_1 y l_2
    # listas vacias, saldremos del bucle con break ya que no hay nada mas que comprovar si falla alguna
    if len(m_1[i]) != num_columnas:
        l_1 = []
        l_2 = []
        break

    # Si es una matriz sumaremos los elementos de cada fila y cada columna
    for j in range(num_columnas):
        sum_filas[i] += m_1[i][j]
        sum_columnas[j] += m_1[i][j]
        
else:
    # Si es una matriz, obtenemos el índice de la fila y de la columna con la suma máxima
    fila_max = sum_filas.index(max(sum_filas))
    columna_max = sum_columnas.index(max(sum_columnas))
    # Asignamos L1 y L2 con la fila y columna correspondiente
    l_1 = m_1[fila_max]
    l_2 = [m_1[i][columna_max] for i in range(num_filas)]

# Imprimimos los resultados
print(l_1)
print(l_2)

# Hacemos lo mismo para la segunda matriz M2
m_2 = [[4, 2, 3], [4, 5], [6, 8, 2]]

numero_filas = len(m_2)
numero_columnas = len(m_2[0])
suma_filas = [0] * num_filas
suma_columnas = [0] * num_columnas

for i in range(numero_filas):
    if len(m_2[i]) != numero_columnas:
        L1 = []
        L2 = []
        break
    for j in range(numero_columnas):
        suma_filas[i] += m_2[i][j]
        suma_columnas[j] += m_2[i][j]
else:
    fila_max = suma_filas.index(max(suma_filas))
    columna_max = suma_columnas.index(max(suma_columnas))
    L1 = m_2[fila_max]
    L2 = [m_2[i][columna_max] for i in range(numero_filas)]

print(L1)
print(L2)