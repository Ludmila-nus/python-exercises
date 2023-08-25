mi_tupla = (1,2,3,455,55,6)

mi_tupla_ordenada = tuple(sorted(mi_tupla))
print(mi_tupla_ordenada)
# (1, 2, 3, 6, 55, 455)

mi_tupla_invertida = tuple(reversed(mi_tupla))
print(mi_tupla_invertida)
#>> (6, 55, 455, 3, 2, 1)

mi_tupla_invertida = tuple(sorted(mi_tupla,reverse=True))
print(mi_tupla_invertida)
#>> (455, 55, 6, 3, 2, 1)