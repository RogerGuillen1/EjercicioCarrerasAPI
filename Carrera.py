import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="universidad"
)


class Carrera:
    def __init__(self, pNombre):
        self.__nombre = pNombre
    def insert(self):
        print("insertar")
    def see(self):
        print("consultar")
    def update(self):
        print("actualizar")
    def delete(self):
        print("pues essxo")