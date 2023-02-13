# Funciones
# valors por default
# def mi_funcion(nombre=None, apellido=None):
#     print(f'Hola {nombre} {apellido}')


# def miSegundaFuncion(nombre = None):
#     return f'Hola {nombre}'


# mi_funcion('Eduardo', 'Uh')
# mi_funcion('Iván', 'Gamiño')
# print(miSegundaFuncion('eduardo'))
# print(miSegundaFuncion('Iván'))

# Valores por default, tipo de parámetro esperado, y tipo de retorno esperado
# def suma_numeros(a: int = 0, b: int = 0) -> int:
#     return a + b


# print(f'Resultado de la suma: {suma_numeros(5, 15)}')

# Argumentos variables

# def listar_nombres(*nombres): # internamente lo convierte en una tupla
#     print(type(nombres))
#     counter = 1
#     for nombre in nombres:
#         print(f'Nombre {counter}: {nombre}')
#         counter += 1


# names = ['Eduardo', 'Iván', 'Jóse', 'Alvaro', 'Laura', 'Juan']
# listar_nombres(*names)
# listar_nombres('Eduardo', 'Iván', 'Jóse', 'Alvaro')

# Ejercicio "Sumar todos los números recibidos como argumentos

# def sumar_numeros(*numeros):
#     acumulador = 0
#     for numero in numeros:
#         acumulador += numero
#     return acumulador


# print(sumar_numeros(45, 55, 60, 40))
# arregloNumeros = [45, 55, 60, 40, 100]
# print(sumar_numeros(*arregloNumeros))

# Ejercicio "Multiplicar todos los números recibidos como argumentos

# def multiplicar_numeros(*args):
#     acumulador = 1
#     for arg in args:
#         acumulador *= arg
#     return acumulador


# print(multiplicar_numeros(1, 10, 10, 100))

# Argumentos variables llave-valor (diccionario)

# def listar_terminos(**kwargs):
#     for llave, valor in kwargs.items():
#         print(f'{llave} : {valor}')


# diccionario = {'1':'Eduardo', '2':'Iván', '3':'Laura','4':'Sasaki', '5':'Armando'}
# listar_terminos(**diccionario)
# listar_terminos(IDE='Integrated Developement Environment', OOP='Object Oriented Programming')

# Función con diferentes tipos de argumentos

# def imprimir_argumentos(nombre, *numeros, **nombres):
#     print(f'Primer argumento: {nombre}')
#     for numero in numeros:
#         print(numero)
#     for llave, valor in nombres.items():
#         print(f'{llave} : {valor}')


# name = 'Eduardo'
# numbers = [1, 2, 3]
# names = {'1':'Eduardo', '2':'Iván', '3':'Laura', '4':'Sasaki', '5':'Armando'}
# imprimir_argumentos(name, *numbers, **names)

# Funciones recursivas

# def calcular_factorial(numero = 0):
#     if 0 <= numero <= 1:
#         return numero
#     return numero * calcular_factorial((numero - 1))


# numero = int(input('Ingrese el número para calcular el factorial: '))
# resultado = calcular_factorial(numero)
# print(f'El factorial de {numero} es {resultado}')

# Ejercicio "Imprimir números de manera descendente usando recursividad (valores positivos únicamente)"

# def imprimir_numeros(numero = 0):
#     if numero > 0:
#         print(numero)
#         imprimir_numeros(numero - 1)


# numero = int(input('Ingrese el número: '))
# if numero >= 0:
#     imprimir_numeros(numero)
# else:
#     print('El número debe ser positivo')

# Ejercicio "Calculadora de impuestos

# def calcular_pago_total(pagosinimpuestos=0.0, montoimpuesto=0.0):
#     return pagosinimpuestos + (pagosinimpuestos * (montoimpuesto / 100))


# pagoSinImpuesto = float(input('Ingrese el pago sin impuestos: '))
# montoImpuesto = float(input('Ingrese el porcentaje de impuestos a pagar (16, 20, 36): '))
# pagoConImpuesto = calcular_pago_total(pagoSinImpuesto, montoImpuesto)
# print(f'El pago con impuestos es de {pagoConImpuesto}')

# Ejercicio "Convertidor de temperaturas"

def fahrenheit_a_celsius(temperatura_fahrenheit):
    return (temperatura_fahrenheit - 32) / 1.8


def celsius_a_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * 1.8) + 32


fahrenheit = float(input('Ingrese la temperatura en fahrenheit: '))
celsius = float(input('Ingrese la temperatura en celsius: '))

print(f'{fahrenheit:.2f} grados fahrenheit equivalen a {fahrenheit_a_celsius(fahrenheit):.2f} grados celsius')
print(f'{celsius:.2f} grados celsius equivalen a {celsius_a_fahrenheit(celsius):.2f} grados fahrenheit')