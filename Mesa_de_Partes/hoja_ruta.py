from datetime import datetime

FORMATO_FECHA = "%d/%m/%Y %H:%M"


def registrar_paso(expediente, detalle):

    area = "Mesa de Partes"

    paso = {
        "paso": len(expediente.historial) + 1,
        "fecha": datetime.now().strftime(FORMATO_FECHA),
        "area": area,
        "estado": expediente.estado,
        "detalle": detalle
    }

    expediente.historial.append(paso)