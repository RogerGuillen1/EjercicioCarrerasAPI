class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def __str__(self):
        return f"Carrera(nombre='{self.nombre}')"