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

def mostrar_hoja_de_ruta(expediente):

    print("\n=== HOJA DE RUTA DEL EXPEDIENTE", expediente.codigo, "===")

    if len(expediente.historial) == 0:
        print("Sin historial registrado")
        return

    for paso in expediente.historial:
        print("Paso", paso["paso"], "|", paso["fecha"], "|", paso["area"], "|", paso["estado"])
        print("   Detalle:", paso["detalle"])

