# class Persona:
#     # self es una referencia al objeto que vamos a crear y despues
#     # se usa para asignar atributos a esa referencia del objeto
#     # método de tipo dunder (double underscore "__init__")
#     def __init__(self, nombre: str=None, apellido: str=None, edad: int=None):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#
# persona1 = Persona('Iván', 'Gamiño', 22)
# persona2 = Persona('Eduardo', 'Uh', 22)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# print(persona2.nombre)
# print(persona2.apellido)
# print(persona2.edad)

class Car:
    def __init__(self, brand: str = None, model: str = None, type: str = None):
        self.brand = brand
        self.model = model
        self.type = type


tsuru = Car('Nissan', 'Tsuru', 'Gas')
chevy = Car('Chevrolet', 'Chevy', 'Gas')
tsuru.brand = 'Toyota'
chevy.brand = 'Mitsubishi'

print(f'''
First car:
    Brand: {tsuru.brand}
    Model: {tsuru.model}
    Type: {tsuru.type}
Second car:
    Brand: {chevy.brand}
    Model: {chevy.model}
    Type: {chevy.type}
''')
