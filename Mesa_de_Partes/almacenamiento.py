import json
from ciudadano import Ciudadano
from expediente import Expediente
from estado import ciudadanos, expedientes


def cargar_ciudadanos():

    with open("datos/ciudadanos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for dato in datos:

        ciudadano = Ciudadano(
            dato["dni"],
            dato["nombre"],
            dato["apellido"],
            dato["correo"]
        )

        ciudadanos.append(ciudadano)


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

    with open("datos/ciudadanos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_expedientes():

    with open("datos/expedientes.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

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

        expedientes.append(expediente)


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
            "respuesta": expediente.respuesta
        }

        datos.append(dato)

    with open("datos/expedientes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
