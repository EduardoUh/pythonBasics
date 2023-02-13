# numero = int(input('Ingrese un número entre 1 y 3: '))
# if numero == 1:
#     numeroTexto = 'Número uno'
# elif numero == 2:
#     numeroTexto = 'Número dos'
# elif numero == 3:
#     numeroTexto = 'Número tres'
# else:
#     numeroTexto = 'Valor fuera de rango'
# print(f'{numero}: {numeroTexto}')

# Operador ternario

# condicion = False
# print('Condición verdadera') if condicion else print('Condición falsa')

# Ejercicio "Estación del año"

# mes = int(input('Ingrese el mes del año (1-12): '))
# estacion = None
# if mes == 12 or 1 <= mes <= 2:
#     estacion = 'Invierno'
# elif 3 <= mes <= 5:
#     estacion = 'Primavera'
# elif 6 <= mes <= 8:
#     estacion = 'Verano'
# elif 9 <= mes <= 11:
#     estacion = 'Otoño'
# else:
#     mes = 'está fuera de rango'
# print(f'El més {mes} pertenece a la estación "{estacion}"')

# Ejercicio "Etapas de vida"

# edad = int(input('Ingrese su edad: '))
# etapaDeVida = None
#
# if 0 <= edad <= 9:
#     etapaDeVida = 'La infancia es increible...'
# elif 10 <= edad <= 19:
#     etapaDeVida = 'Muchos cambios y mucho estudio...'
# elif 20 <= edad <= 30:
#     etapaDeVida = 'Amor y comienza el trabajo...'
# else:
#     etapaDeVida = 'Etapa de vida no reconocida.'
# print(f'Tu edad es {edad}, {etapaDeVida}')

# Ejercicio "Sistema de calificaciones"

calificacion = int(input('Ingrese la calificación (0-10): '))
nota = None
if 9 <= calificacion <= 10:
    nota = 'A'
elif calificacion == 8:
    nota = 'B'
elif calificacion == 7:
    nota = 'C'
elif calificacion == 6:
    nota = 'D'
elif 0 <= calificacion <= 5:
    nota = 'F'
else:
    nota = 'Valor incorrecto.'
print(f'La calificación es {calificacion} y la nota correspondiente es: {nota}')
