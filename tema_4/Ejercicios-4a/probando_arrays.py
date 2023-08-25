import constantes as cte
import numpy as np    

print(cte.tau)
'''
my_array = np.array([1,2,3,4,5,6,7,8,9])
print(my_array)
nuevo_array = my_array * 2
print(nuevo_array)

my_list = [1,2,3]
lista_a_array = np.array(my_list)
print(lista_a_array)
lista_b_array = np.array([1,2,3], dtype = np.int8)
print(type(lista_a_array[0]))
print(type(lista_b_array[0]))

lista_c_array = np.array([[1,2,3],[4,5,6]], dtype = np.int8)
print(lista_c_array)

print(lista_c_array.shape)
print(lista_c_array.ndim)
lista_d_array = lista_c_array.reshape([3,2])
print(lista_d_array)



my_array2 = np.arange(1,8,2)
print(my_array2)

array_vacio = np.zeros((2,4))
print(array_vacio)


eye_array = np.eye(3, k = 1)
eye_array[eye_array == 0] = 2
eye_array[eye_array < 2] = 9
eye_array[1: , :2] = 4

print(eye_array)
print('')

sorted_array = np.sort(eye_array)

print(sorted_array)
print('')
sorted_array = np.sort(eye_array, axis=0)

print(sorted_array)
print('')

array_view = sorted_array.view()
array_view [:] = 5
print(array_view)
print(sorted_array)

array_copy = sorted_array.copy()
array_copy [:] = 6
print(array_copy)
print(sorted_array)
'''
'''
a = np.zeros((3,3))
a[:] = 2

a.fill(8)
print(a)
print('')

a += 3
print(a)
print('')

a -=6
print(a)
print('')

a *=2
print(a)
print('')

a /=2
print(a)
print('')

'''

b = np.arange(1,10).reshape((3,3))
print(b)
print('')
suma_array = b.prod()
print(suma_array)
print('')
suma_array0 = b.prod(0)
print(suma_array0)
print('')
suma_array1 = b.prod(1)
print(suma_array1)
print('')

mean_array = b.mean()
print(mean_array)
max_array = b.max()
print(max_array)
min_array = b.min()
print(min_array)

indice_min = b.argmin()
indice_max = b.argmax()
print(indice_max, indice_min)
