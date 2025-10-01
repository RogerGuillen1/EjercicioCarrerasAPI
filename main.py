import mysql.connector

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
            print("Opción: Añadir carrera (pendiente de implementar)")
        elif opcion == "2":
            print("Opción: Actualizar carrera (pendiente de implementar)")
        elif opcion == "3":
            print("Opción: Ver carreras (pendiente de implementar)")
        elif opcion == "4":
            print("Opción: Borrar carrera (pendiente de implementar)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
