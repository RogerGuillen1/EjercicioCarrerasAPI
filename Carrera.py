class Carrera:
    def __init__(self, pNombre):
        self.__nombre = pNombre
    def insert(self, mycursor):
        print("insertar")
    def see(self, mycursor):
        print("consultar")
    def update(self, mycursor):
        print("actualizar")
    def delete(self, mycursor):
        print("pues essxo")