# Crea una nueva subclase Trabajador 
# que sobrescriba presentarse() para 
# que incluya su empresa.

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}."
class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.profesion} y trabajo en {self.empresa}."
t = Trabajador("Elena", 35, "Arquitecta", "Construcciones XYZ")
print(t.presentarse())
