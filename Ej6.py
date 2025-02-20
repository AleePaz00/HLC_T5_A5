# Crea una clase Libro con atributos titulo y autor. 
# Luego, crea una clase Biblioteca que contenga una lista 
# de libros y métodos para agregar libros y mostrarlos.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a la biblioteca."

    def mostrar_libros(self):
        if not self.libros:
            return "La biblioteca está vacía."
        return "\n".join(f"{i+1}. {libro}" for i, libro in enumerate(self.libros))
biblio = Biblioteca()
biblio.agregar_libro(Libro("1984", "George Orwell"))
biblio.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
print(biblio.mostrar_libros())

