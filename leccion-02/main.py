# operandoA = 3
# operandoB = 2
# suma = operandoA + operandoB
# print(f'El resulrado de la suma es: {suma}')
# resta = operandoA - operandoB
# print(f'El resultado de la resta es: {resta}')
# multiplicacion = operandoA * operandoB
# print(f'El resultado de la multiplicación es: {multiplicacion}')
# division = operandoA / operandoB # división con residuo (literal float)
# print(f'El resultado de la división es: {division}')
# divisionEnteros = operandoA // operandoB # división sin residuo (literal integer)
# print(f'El resultado de la división es: {divisionEnteros}')
# modulo = operandoA % operandoB # retorna el residuo de la división (float o integer)
# print(f'El residuo de la operación es: {modulo}')
# exponente = operandoA ** operandoB
# print(f'El resultado del exponente es: {exponente}')

# Ejercicio, "Area y Perimetro de un rectangulo"

# altoRectangulo = int(input('Ingrese el alto del rectangulo: '))
# anchoRectangulo = int(input('Ingrese el ancho del rectangulo: '))
# print('Calculando...')
# areaRectangulo = altoRectangulo * anchoRectangulo
# perimetroRectangulo = (altoRectangulo + anchoRectangulo) * 2
# print(f'El área del rectangulo es {areaRectangulo} y el perimetro es {perimetroRectangulo}')

# Operadores de comparación

# a = 4
# b = 2
# resultado = (a == b)
# print(resultado)
# resultado = (a != b)
# print(resultado)
# resultado = (a < b)
# print(resultado)
# resultado = (a > b)
# print(resultado)
# resultado = (a >= b)
# print(resultado)
# resultado = (a <= b)
# print(resultado)

# Ejercicio "numero par o impar"

# numero = int(input('Ingrese el número: '))
# if((numero % 2) == 0):
#    print(f'{numero} es un número par')
# else:
#    print(f'{numero} es un número impar')

# Ejercicio "determinar si es adulto"

# edad = int(input('Ingrese la edad: '))
# if(edad >= 18):
#     print('Es un adulto')
# else:
#     print('No es un adulto')

# Operadores lógicos

# a = False
# b = True
# resultado = a and b
# print(resultado)
# resultado = b or a
# print(resultado)
# resultado = not a
# print(resultado)
# resultado = not b
# print(resultado)

# Ejercicio "Valor dentro de un rango"

# numero = int(input('Ingrese el número a evaluar: '))
# valorMinimo = 0
# valorMaximo = 5
# if numero >= valorMinimo and numero <= valorMaximo:
#     print(f'El número {numero} se encuentra dentro del rango')
# else:
#     print(f'El número {numero} se encuentra fuera del rango')
# resultado = (numero >= valorMinimo) and (numero <= valorMaximo)
# print(f'Dentro del rango: {resultado}')
# if resultado:
#     print(f'El número {numero} se encuentra dentro del rango')
# else:
#     print(f'El número {numero} se encuentra fuera del rango')

# Ejercicio "Asistir a un partido"

# vacaciones = False
# diaDescanso = False
# if vacaciones or diaDescanso:
#     print('El padre si puede asistir')
# else:
#     print('el padre no puede asistir')
# if not (vacaciones or diaDescanso):
#     print('el padre no puede asistir')
# else:
#     print('El padre si puede asistir')

# Ejercicio "dentro del rango de edades"

# edad = int(input('Ingrese su edad: '))
# veintes = 20 <= edad < 30 # (edad >= 20) and (edad < 30)
# treintas = 30 <= edad < 40 # (edad >= 30) and (edad <=40)
# dentroDelRango = veintes or treintas
# if not dentroDelRango:
#     print('No se encuentra entre los 20\'s o 30\'s')
# else:
#     print('Se encuentra entre los 20\'s o 30\'s')
#     if veintes:
#         print('Específicamente en los 20\'s')
#     elif treintas:
#         print('Específicamente en los 30\'s')

# Ejercicio "nayor de dos números"

# primerNumero = int(input('Ingrese el primer número: '))
# segundoNumero = int(input('Ingrese el segundo número: '))

# if primerNumero > segundoNumero:
#     print(f'El número {primerNumero} es mayor al número {segundoNumero}')
# elif primerNumero == segundoNumero:
#     print(f'Los números son iguales')
# else:
#     print(f'El número {segundoNumero} es mayor al número {primerNumero}')

# Ejercicio "tienda de libros"

print('Proporcione los siguientes datos del libro:')
bookName = input('Proporcione el nombre: ')
bookId = int(input('Proporcione el ID: '))
bookPrice = float(input('Proporcione el precio: '))
delivery = input('Indique si el envio es gratuito (True/False): ')

if delivery == 'True':
    delivery = True
elif delivery == 'False':
    delivery = False
else:
    delivery = 'valor incorrecto, debe escribir "True" o "false"'

print(f'''
    Nombre: {bookName}
    Id: {bookId}
    Precio: {bookPrice}
    Envío gratuito: {delivery}
''')
