# Crea una clase Persona con los atributos nombre, 
# edad y profesion. Agrega un método presentarse() que 
# devuelva un mensaje con su información.
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}."
p = Persona("Ana", 28, "Ingeniera")
print(p.presentarse())