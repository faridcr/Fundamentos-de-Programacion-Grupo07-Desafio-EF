from datetime import datetime

FORMATO_FECHA = "%d/%m/%Y %H:%M"


def registrar_paso(expediente, detalle):

        # Área donde está el expediente en este momento
    if expediente.subgerencia != "Sin asignar":
        area = expediente.subgerencia

    elif expediente.gerencia != "Sin asignar":
        area = expediente.gerencia

    else:
        area = "Mesa de Partes"

    paso = {
        "paso": len(expediente.historial) + 1,
        "fecha": datetime.now().strftime(FORMATO_FECHA),
        "area": area,
        "estado": expediente.estado,
        "detalle": detalle
    }

    expediente.historial.append(paso)