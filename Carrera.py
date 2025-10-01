class Carrera:
    def __init__(self, pNombre):
        self.__nombre = pNombre
    
    def insert(self, mycursor, mydb):
        sql = "INSERT INTO carrera (nombre) VALUES (%s)"
        val = (self.__nombre)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Carrera '{self.__nombre}' insertada correctamente.")

    def see(self, mycursor):
        mycursor.execute("SELECT * FROM carreras")
        carreras = mycursor.fetchall()
        return carreras
    
    def update(self, mycursor, mydb):
        nuevo_nombre = input("Introduce el nuevo nombre de la carrera")
        sql = "UPDATE carrera SET nombre = %s WHERE nombre = %s"
        val = (nuevo_nombre, self.__nombre)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Carrera '{self.__nombre}' actualizada a '{nuevo_nombre}'.")
        self.__nombre = nuevo_nombre

    def delete(self, mycursor):
        sql = "DELETE FROM carreras WHERE nombre = %s"
        val = (self.__nombre)
        mycursor.execute(sql, val)
        print(f"Carrera '{self.__nombre}' eliminada.")