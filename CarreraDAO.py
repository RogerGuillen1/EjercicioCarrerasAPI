class CarreraDAO:
    def __init__(self, cursor, db):
        self.cursor = cursor
        self.db = db

    def insert(self, carrera):
        sql = "INSERT INTO carrera (nombre) VALUES (%s)"
        val = (carrera.nombre,)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(f"Carrera '{carrera.nombre}' insertada correctamente.")

    def see_all(self):
        self.cursor.execute("SELECT * FROM carrera")
        return self.cursor.fetchall()

    def update(self, carrera, nuevo_nombre):
        sql = "UPDATE carrera SET nombre = %s WHERE nombre = %s"
        val = (nuevo_nombre, carrera.nombre)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(f"Carrera '{carrera.nombre}' actualizada a '{nuevo_nombre}'.")
        carrera.nombre = nuevo_nombre

    def delete(self, carrera):
        sql = "DELETE FROM carrera WHERE nombre = %s"
        val = (carrera.nombre,)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(f"Carrera '{carrera.nombre}' eliminada.")
