# Ciclo for
# condicion = True
#
# while condicion:
#     print('While')
# else:
#     print('Else')

# contador = 0
#
# while contador < 4:
#     print(contador)
#     contador += 1
# else:
#     print('Else')

# Ejercicio "Imprimir del 0 al 5 usando while"

# contador = 0
# maximo = 6
#
# while contador < maximo:
#     print(contador)
#     contador += 1

# Ejercicio "Imprimir del 5 al 1 de manera descendente"

# contador = 5
# limite = 0
#
# while contador > limite:
#     print(contador)
#     contador -= 1

# Ciclo for

# cadena = 'Hola'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin ciclo for')

# Palabra break

# for letra in 'Holanda':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         break

# Palabra continue "Imprimir números pares"

for numero in range(6):
    if numero % 2 != 0:
        continue
    print(f'Número {numero} es par.')
