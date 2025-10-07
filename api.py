from flask import Flask, jsonify, request as req
from CarreraDAO import CarreraDAO
from Carrera import Carrera
import pymysql

app = Flask(__name__)

user = input("Usuario de la base de datos: ")
password = input("Contraseña de la base de datos: ")

try:
    mydb = pymysql.connect(
        host="localhost",
        user=user,
        database="universidad",
        password=password,
        ssl_disabled=True
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM carrera")
    myresult = mycursor.fetchall()

    dao = CarreraDAO(mycursor, mydb)
    print("✅ Conexión exitosa.")

except Exception as e:
    print("❌ Error de conexión a MySQL:", e)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/carreras/", methods=["GET"])
def darCarreras():
    carreras = dao.see_all()
    carrerasEnClase = [Carrera(c[1]) for c in carreras]
    return jsonify({"about": [{"nombre": c.get_nombre()} for c in carrerasEnClase]}), 200

@app.route("/carreras/", methods=["PATCH"])
def actualizarCarrera():
    datos = req.form
    nuevo_nombre = datos["nuevo_nombre"]
    carrera = datos["carrera"]
    dao.update(carrera, nuevo_nombre)
    return jsonify({"status": "success", "nombre": nuevo_nombre}), 200

@app.route("/carreras/", methods=["POST"])
def crearCarrera():
    nombre = req.form["nombre"]
    carrera = Carrera(nombre)
    print(f"Creando carrera con nombre: {nombre}")
    dao.insert(carrera)
    return jsonify({"status": "success", "nombre": nombre}), 201

@app.route("/carreras/", methods=["DELETE"])
def borrarCarrera():
    datos = req.form
    nombre = datos["nombre"]
    carrera = Carrera(nombre)
    dao.delete(carrera)
    return jsonify({"status": "success", "nombre": nombre}), 200

if __name__ == "__main__":
    app.run(debug=True)
