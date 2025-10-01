import mysql.connector
from Carrera import Carrera
from CarreraDAO import CarreraDAO
import logging
import pymysql
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1', 3306))
print('Socket connect result:', result)  # 0 means success
sock.close()

logging.basicConfig(level=logging.DEBUG)

print("1")

try:
    print("Trying")
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        database="universidad",
        password="123456",
        ssl_disabled=True
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
            print("Opción: Actualizar carrera (pendiente de implementar)")
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