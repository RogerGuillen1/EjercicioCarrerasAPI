import mysql.connector
print("1")

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="universidad",
    )
    print("✅ Conexión exitosa.")

except Exception as e:
    print("❌ Error de conexión a MySQL:", e)

print("2")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM carreras")

myresult = mycursor.fetchall()

print(myresult)

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Añadir carrera")
        print("2. Actualizar carrera")
        print("3. Ver carrera")
        print("4. Borrar carrera")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Opción: Añadir carrera (pendiente de implementar)")
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