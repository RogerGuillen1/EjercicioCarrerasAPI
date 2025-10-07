from Carrera import Carrera
from CarreraDAO import CarreraDAO
import pymysql
import requests as req

try:
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        database="universidad",
        password="123456",
        ssl_disabled=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM carrera")
    myresult = mycursor.fetchall()

    dao = CarreraDAO(mycursor, mydb)
    print("✅ Conexión exitosa.")

except Exception as e:
    print("❌ Error de conexión a MySQL:", e)

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Añadir carrera")
        print("2. Actualizar carrera")
        print("3. Ver carreras")
        print("4. Borrar carrera")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nuevaCarrera = input("Introduce el nombre de la carrera que quieres crear: ")
            datos = {'nombre': nuevaCarrera}
            response = req.post('http://localhost:5000/carreras/', data=datos)
            print("Carrera "+ nuevaCarrera + " creada correctamente.")

        elif opcion == "2":
            carreras = req.get('http://localhost:5000/carreras/')
            carrerasLista = carreras.json()["about"]
            if not carreras:
                print("No hay carreras registradas.")
                continue
            print("Carreras disponibles:")
            for i, c in enumerate(carrerasLista):
                print(f'{i+1}. {c["nombre"]}')

            seleccion = int(input("Selecciona el número de la carrera a actualizar: "))
            if seleccion > len(carrerasLista) or seleccion < 1:
                print("Numero invalido")
            else:
                carrera_seleccionada = carrerasLista[seleccion - 1]
                nuevo_nombre = input("Escribe el nuevo nombre: ")
                response = req.patch(f'http://localhost:5000/carreras/', data={'nuevo_nombre': nuevo_nombre, 'carrera': carrera_seleccionada["nombre"]})
                print(f"La carrera {carrera_seleccionada['nombre']} ahora tiene el nombre {nuevo_nombre}")

        elif opcion == "3":
            carreras = req.get('http://localhost:5000/carreras/')
            carrerasLista = carreras.json()["about"]
            if not carreras:
                print("No hay carreras registradas.")
                continue
            print("Carreras disponibles:")
            for i, c in enumerate(carrerasLista):
                print(f'{i+1}. {c["nombre"]}')

        elif opcion == "4":
            carreras = req.get('http://localhost:5000/carreras/')
            carrerasLista = carreras.json()["about"]
            if not carreras:
                print("No hay carreras registradas.")
                continue
            print("Carreras disponibles:")
            for i, c in enumerate(carrerasLista):
                print(f"{i+1}. {c['nombre']}")

            seleccion = int(input("Selecciona el número de la carrera para borrar: "))
            if seleccion > len(carrerasLista) or seleccion < 1:
                print("Numero invalido")
            else:
                carrera_seleccionada = carrerasLista[seleccion - 1]
                carreras = req.delete('http://localhost:5000/carreras/', data={'nombre': carrera_seleccionada["nombre"]})
                print(f"La carrera {carrera_seleccionada['nombre']} ha sido eliminada.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
main()