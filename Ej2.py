# Extiende la clase Persona creando una subclase 
# Estudiante, agregando un nuevo atributo grado y 
# sobrescribiendo el método presentarse().

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}."

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, grado):
        super().__init__(nombre, edad, profesion)
        self.grado = grado

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.grado}."
e = Estudiante("Carlos", 22, "Estudiante", "Matemáticas")
print(e.presentarse())

