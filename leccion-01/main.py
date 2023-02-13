# Enviar un saludo a la consola utilizando Python
# print('Este es mi saludo desde Python')
# los valores de las variables se almacenan en una posición de memoria, y
# las variables apuntan a estas direcciones.
# Cada uno de estos valores es una literal, es decir, un valor que podemos asignar a las variables
# x = 10
# y = 15
# z = x + y

# print(x)
# print(y)
# print(z)
# recuperar la dirección de memoria en la que se encuentra una literal
# print(id(x))
# print(id(y))
# print(id(z))

# Ejercicio de declaración de variables

# name = 'Eduardo Iván Uh Gamiño'
# numTelefono = 9992753852
# email = 'eduardoivanuhgamino@gmail.com'

# print(name)
# print(numTelefono)
# print(email)

# Tipos de datos en python
# numeric(integer, complex number, float), dictionary, boolean, set, sequence type(string, list, tuple)
# x = 10
# nombre: str = 'Eduardo' # :str indica que apunta hacia una literal tipo string, esa sintaxis se llama "hint"
# flotante = 1.4
# boleano = True
# arr = [5, 8, 9]
# print(type(x))
# print(type(nombre))
# print(type(flotante))
# print(type(boleano))
# print(type(arr))

# Manejo de cadenas en python

# miGrupoFavorito = 'System of a down'' eduardo'  # si las cadenas son adyacentes se puede omitir el operador "+"
# miSegundoGrupoFavorito = 'linking park'
# Formato de string con los operadores {} y la función str.format()
# print('Mi grupo favorito es {}'.format(miGrupoFavorito))
# Usando las cadenas F para concatenar strings en Python (hay otras maneras, busca en la documentación)
# print(f'Mi segundo grupo favorito es {miSegundoGrupoFavorito}')

# Tipos bool (boolean)

# mayorQue = False
# print(mayorQue)
# primerNumero = 10
# segundoNumero = 2
# mayorQue = primerNumero > segundoNumero
# if mayorQue:
  #  print(f'{primerNumero} es mayor que {segundoNumero}')
# else:
  #  print(f'{primerNumero} no es mayor que {segundoNumero}')

# Función "input" para procesar la entrada del usuario

# primerNumero = int(input('Ingrese el primer número: '))
# segundoNumero = int(input('Ingrese el segundo número: '))
# resultado = primerNumero + segundoNumero
# print(f'El resultado es: {resultado} y su tipo es: {type(resultado)}')
# print('Fin del programa...')

# Ejercicio "califica tu día"

# calificacion = input('Califica tu día del 1 al 10: ')
# print(f'Mi día estuvo de: {calificacion}')

# Ejercicio "detalles de un libro"

title = input('Ingrese el titulo del libro: ')
author = input('Ingrese el nombre del autor del libro: ')
print(f'{title} was written by {author}')
