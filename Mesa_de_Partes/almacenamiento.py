import json
import os

from ciudadano import Ciudadano
from expediente import Expediente
from subgerencia import Subgerencia
from trabajador import Trabajador
from estado import ciudadanos, expedientes, trabajadores, subgerencias, gerencias


# UBICACION DE LOS ARCHIVOS JSON
# Usa la carpeta "datos" si existe; si no, la misma carpeta de los .py
CARPETA = os.path.dirname(os.path.abspath(__file__))
CARPETA_DATOS = os.path.join(CARPETA, "datos")


def ruta(nombre):
    if os.path.isdir(CARPETA_DATOS):
        return os.path.join(CARPETA_DATOS, nombre)

    return os.path.join(CARPETA, nombre)


def leer_json(nombre, por_defecto):

    try:
        with open(ruta(nombre), "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print("AVISO: no se encontró", nombre, "- se inicia vacío.")

    except json.JSONDecodeError:
        print("AVISO:", nombre, "está vacío o dañado - se inicia vacío.")

    return por_defecto


def escribir_json(nombre, datos):

    with open(ruta(nombre), "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# CARGAR AREAS (GERENCIAS Y SUBGERENCIAS)
def cargar_areas():

    datos = leer_json("areas.json", {})

    gerencias.clear()
    subgerencias.clear()

    for nombre in datos.get("gerencias", []):
        gerencias.append(nombre)

    for dato in datos.get("subgerencias", []):
        subgerencias.append(Subgerencia(dato["nombre"], dato["gerencia"]))


# CARGAR TRABAJADORES
def cargar_trabajadores():

    datos = leer_json("trabajadores.json", [])

    trabajadores.clear()

    for dato in datos:

        trabajador = Trabajador(
            dato["dni"],
            dato["nombre"],
            dato["apellido"],
            dato["correo"],
            dato["usuario"],
            dato["contrasena"],
            dato["area"]
        )

        trabajadores.append(trabajador)

    if len(trabajadores) == 0:
        print("AVISO: no hay trabajadores cargados, nadie podrá iniciar sesión.")


# CARGAR CIUDADANOS
def cargar_ciudadanos():

    datos = leer_json("ciudadanos.json", [])

    ciudadanos.clear()

    for dato in datos:

        ciudadano = Ciudadano(
            dato["dni"],
            dato["nombre"],
            dato["apellido"],
            dato["correo"]
        )

        ciudadanos.append(ciudadano)


# GUARDAR CIUDADANOS
def guardar_ciudadanos():

    datos = []

    for ciudadano in ciudadanos:

        dato = {
            "dni": ciudadano.dni,
            "nombre": ciudadano.nombre,
            "apellido": ciudadano.apellido,
            "correo": ciudadano.correo
        }

        datos.append(dato)

    escribir_json("ciudadanos.json", datos)


# CARGAR EXPEDIENTES
def cargar_expedientes():

    datos = leer_json("expedientes.json", [])

    expedientes.clear()

    for dato in datos:

        expediente = Expediente(
            dato["codigo"],
            dato["dni"],
            dato["asunto"],
            dato["descripcion"],
            dato["direccion"]
        )

        expediente.estado = dato["estado"]
        expediente.gerencia = dato["gerencia"]
        expediente.subgerencia = dato["subgerencia"]
        expediente.atencion = dato["atencion"]
        expediente.respuesta = dato["respuesta"]
        expediente.motivo_devolucion = dato.get("motivo_devolucion", "Ninguno")

        expedientes.append(expediente)


# GUARDAR EXPEDIENTES
def guardar_expedientes():

    datos = []

    for expediente in expedientes:

        dato = {
            "codigo": expediente.codigo,
            "dni": expediente.dni,
            "asunto": expediente.asunto,
            "descripcion": expediente.descripcion,
            "direccion": expediente.direccion,
            "estado": expediente.estado,
            "gerencia": expediente.gerencia,
            "subgerencia": expediente.subgerencia,
            "atencion": expediente.atencion,
            "respuesta": expediente.respuesta,
            "motivo_devolucion": expediente.motivo_devolucion
        }

        datos.append(dato)

    escribir_json("expedientes.json", datos)


# CARGAR TODO AL INICIAR
def cargar_todo():
    cargar_areas()
    cargar_trabajadores()
    cargar_ciudadanos()
    cargar_expedientes()
