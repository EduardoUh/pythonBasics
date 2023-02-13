# Colecciones en python
# Listas, mantienen un orden y son mutables

# nombres = ['Juan', 'Karla', 0, 'Ricardo', True, 'María']

# Acceder a los elementos de una lista

# print(nombres[0])
# print(nombres[1])

# Acceder a los elementos de manera inversa

# print(nombres[-1])
# print(nombres[-2])

# Imprimor un rango

# print(nombres[0:3]) # El segundo número es un límite, por lo que no está incluido en el rango

# Ir del inicio de la lista al índice (sin incluirlo)

# print(nombres[:4])

# Desde el índice indicado hasta el final

# print(nombres[2:])

# Cambiar el valor de  un índice

# nombres[5] = 'Eduardo'
# print(nombres)

# Iterar una lista

# for nombre in nombres:
#     print(nombre)

# Largo de una lista

# print(len(nombres))

# Insertar un elemento

# nombres.append('Iván')
# print(nombres)

# Insertar elemento en un índice en específico

# nombres.insert(0, 'Pancracio')
# print(nombres)

# Remover último elemento

# nombres.pop()
# print(nombres)

# Remover un elemento por valor

# nombres.remove('Eduardo')
# print(nombres)

# Remover elemento por indice

# del nombres[0]
# print(nombres)

# Eliminar todos lo elementos de la lista

# nombres.clear()
# print(nombres)

# Borrar la lista de memoria

# del nombres
# print(nombres) # no imprime nada ya que no existe más en memoria

# Sintaxis de range(inicio<opcional default 0>, fin<requerido>, incremento<opcional default 1>)
# Ejercicio "Iterar un rango de 0 a 10 e imprimir números divisibles entre 3"

# print('Ejercicio 1')
# for numero in range(11):
#     if numero % 3 != 0 or numero == 0:
#         continue
#     print(numero)

# Ejercicio "Crear un rango de 2 a 6 e imprimirlo"

# print('Ejercicio 2')
# rango = range(2, 7)
# for numero in rango:
#     print(numero)

# Ejercicio "Crear un rango de 3 a 10 con incremento de 2

# print('Ejercicio 3')
# for numero in range(3, 11, 2):
#     print(numero)

# Tuplas, mantienen un orden y son inmutables

# frutas = ('Naranja', 'Platano', 'Guayaba')

# Largo de una tupla

# print(len(frutas))

# Acceder por indice

# print(frutas[1])

# Navegación inversa

# print(frutas[-2])

# Rango de valores

# print(frutas[1:])
# print(frutas[:2])
# print(frutas[0:2])

# Recorrer los elementos de una túpla

# for fruta in frutas:
#     print(fruta, end = ', ')

# Las tuplas son inmutables

# frutas[1] = 'Melocotón'
# print(frutas)

# Para "modificar" una tupla entonces se puede convertir en una lista, las cuales si son mutables
# print(frutas)
# listaFrutas = list(frutas)
# listaFrutas[1] = 'Melocotón'
# frutas = tuple(listaFrutas)
# print(listaFrutas)
# print('\n', frutas)

# añadir elementos a una tupla

# tupla  = (1, 2, 3, 4)
# tupla = tupla.__add__((18,)) # solo se pueden añadir tuplas a la tupla, de ahí que haya dos paréntesis y una coma junto al número
# print(tupla)

# Eliminar una tupla

# del frutas
# print(frutas)

# Las listas y diccionarios se pasan por referencia

# lista = ['eduardo', 'iván', 'uh', 'gamiño']
# print(lista)
# listaCopia = [*lista] # para que se elimine la referencia (similar al spread operator)
# listaCopia[1] = 'Pancracio'
# print(lista)
# print(listaCopia)

# Ejercicio "Crear una lista que sólo incluya los valores menores a 5"

# numeros = (13, 1, 8, 3, 2, 5, 8)
# lista = []

# for numero in numeros:
#     if numero >= 5:
#         continue
#     lista.append(numero)
# print(lista)

# Set, no mantienen un orden, no almacena elementos duplicados, no se pueden modificar elementos, pero si agregarlos o eliminarlos

# planetas = {'Marte', 'Júpiter', 'Venus'}

# Crear una copia del set (eliminando la referencia)

# planetas2 = planetas.copy()

# Eliminar un elemento del Set, arrojando error en caso de no encontrar el elemento señalado

# planetas2.remove('Júpiter')
# print(planetas)
# print(planetas2)

# Eliminar elemento si arrojar error en caso de no existir

# planetas2.discard('Júpiter')

# Largo del Set

# print(len(planetas))

# Revisar si un elemento existe

# print('Marte' in planetas)
# print(planetas.__contains__('Marte'))

# Agregar más elementos

# planetas2.add(5)
# print(planetas2)

# No acepta elementos duplicados, es decir que no lo va a agregar

# planetas2.add(5)
# print(planetas2)

# Limpiar Set

# planetas2.clear()
# print(planetas2)

# ELiminar Set de memoria

# del planetas2
# print(planetas2)#

# Diccionarios, similares a los objetos literales en JS
# dict {key:value}, cualquier tipo inmutable se puede usar como llave (int, float, bool, str, etc)

diccionario = {'IDE':'Integrated Development Environment',
               'OOP':'Object Oriented Programming',
               'DBMS':'Database Management System',
               }
# Obetener valores de elementos en específico

# print(diccionario['DBMS'])
# print(diccionario.__getitem__('OOP'))
# print(diccionario.get('IDE'))

# Longitud

# print(len(diccionario))

# Modificar elementos

# diccionario['IDE'] = 'integrated development environment'
# print(diccionario['IDE'])

# Añadir un elemento

# diccionario['Programador'] = True
# print(diccionario)

# Recorrer los elementos

# for llave in diccionario:
#     print(f'{llave} : {diccionario[llave]}')
# print('\n')
# for llave, valor in diccionario.items():
#     print(f'{llave} : {valor}')
# print('\n')
# for key in diccionario.keys():
#     print(key)
# print('\n')
# for value in diccionario.values():
#     print(value)

# Comprobar existencia de elementos
# print('\n')
# print('OOP' in diccionario)
# print(diccionario.__contains__('DBMS'))

# remover un elemento

print(diccionario)
diccionario.pop('DBMS')
print(diccionario)

# Limpiar el diccionario

diccionario.clear()
print(diccionario)

# Eliminar el diccionario de memoria

del diccionario
print(diccionario)
