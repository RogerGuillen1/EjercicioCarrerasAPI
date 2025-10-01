import mysql.connector
from Carrera import Carrera
from CarreraDAO import CarreraDAO
print("1")

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="super3",
        database="universidad",
    )
    print("✅ Conexión exitosa.")

except Exception as e:
    print("❌ Error de conexión a MySQL:", e)

print("2")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM carrera")
myresult = mycursor.fetchall()
print(myresult)

dao = CarreraDAO(mycursor, mydb)

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Añadir  carrera")
        print("2. Actualizar carrera")
        print("3. Ver carrera")
        print("4. Borrar carrera")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nuevaCarrera = Carrera(input("Introduce el nombre de la carrera que quieres crear: "))
            dao.insert(nuevaCarrera)

        elif opcion == "2":
            carreras = [Carrera(c[1]) for c in dao.see_all()]
            if not carreras:
                print("No hay carreras registradas.")
                continue
            print("Carreras disponibles:")
            for i, c in enumerate(carreras):
                print(f"{i+1}. {c.get_nombre()}")

            seleccion = int(input("Selecciona el número de la carrera a actualizar: "))
            if seleccion > len(carreras) or seleccion < 1:
                print("Numero invalido")
            else:
                carrera_seleccionada = carreras[seleccion - 1]
                nuevo_nombre = input("Escribe el nuevo nombre: ")
                dao.update(carrera_seleccionada, nuevo_nombre)

            


        elif opcion == "3":
            carrera = input("Que carrera quieres ver?")

        elif opcion == "4":
            print("Opción: Borrar carrera (pendiente de implementar)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
main()