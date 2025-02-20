# Crea una clase Figura con un método calcular_area() 
# vacío (pass). Luego, crea las clases Circulo y 
# Rectangulo que implementen este método.
import math
class Figura:
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto
c = Circulo(5)
r = Rectangulo(4, 6)
print(c.calcular_area())  
print(r.calcular_area())  