class Carrera:
    def __init__(self, pNombre):
        self.__nombre = pNombre
    def insert(self, mycursor):
        print("insertar")
    def see(self, mycursor):
        mycursor.execute("SELECT * FROM carreras")
        carreras = mycursor.fetchall()
        return carreras
    def update(self, mycursor):
        print("actualizar")
    def delete(self, mycursor):
        sql = "DELETE FROM carreras WHERE nombre = %s"
        val = (self.__nombre)
        mycursor.execute(sql, val)
        print(f"Carrera '{self.__nombre}' eliminada.")