from datetime import datetime, timedelta

from expediente import Expediente
from estado import ciudadanos, expedientes, gerencias
from almacenamiento import guardar_expedientes


def buscar_ciudadano(dni):

    for ciudadano in ciudadanos:

        if ciudadano.dni == dni:
            return ciudadano

    return None


def numero_de_codigo(expediente):
    # "E-12" -> 12. Si el código no tiene el formato esperado devuelve None.

    partes = expediente.codigo.split("-")

    if len(partes) == 2 and partes[1].isdigit():
        return int(partes[1])

    return None


def mostrar_expediente_completo(expediente):

    print("\n=== DATOS DEL CIUDADANO ===")

    ciudadano = buscar_ciudadano(expediente.dni)

    if ciudadano is None:
        print("Ciudadano no encontrado.")

    else:
        print("Nombre:", ciudadano.nombre)
        print("Apellido:", ciudadano.apellido)
        print("Correo:", ciudadano.correo)

    expediente.mostrar_datos()

def revisar_prioridad():
    codigo = input("Ingrese el código del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente.codigo == codigo:
            if expediente.estado == "Cerrado":
                print("El expediente está cerrado.")
                return

            print("\n=== REVISIÓN DE URGENCIA ===")
            print("Expediente:", expediente.codigo)
            print("Asunto:", expediente.asunto)
            print(
                "Prioridad solicitada:",
                expediente.prioridad_solicitada or "Sin registrar",
            )

            print("\nElige la prioridad de atención:")
            prioridad_elegida = seleccionar_prioridad()

            justificacion = input("Justifique su decisión: ").strip()
            while not justificacion:
                justificacion = input("La justificación es obligatoria: ").strip()

            expediente.prioridad = prioridad_elegida
            expediente.justificacion_prioridad = justificacion

            plazos = {"Normal": 7, "Urgente": 3, "Muy urgente": 1}
            fecha_revision = datetime.now()
            dias = plazos[prioridad_elegida]

            expediente.fecha_verificacion_prioridad = fecha_revision.isoformat(
                timespec="seconds"
            )
            expediente.fecha_limite = (
                fecha_revision.date() + timedelta(days=dias)
            ).isoformat()
            guardar_expedientes()

            print("Prioridad asignada:", expediente.prioridad)
            return

    print("No se encontró un expediente con ese código.")


def consultar_vencimientos():
    hoy = datetime.now().date()
    hay_resultados = False

    print("\n=== EXPEDIENTES PRÓXIMOS A VENCER O VENCIDOS ===")

    for expediente in expedientes:
        if expediente.estado == "Cerrado" or not expediente.fecha_limite:
            continue

        fecha_limite = datetime.fromisoformat(expediente.fecha_limite).date()
        dias_restantes = (fecha_limite - hoy).days

        if dias_restantes > 2:
            continue

        if dias_restantes < 0:
            aviso = "Vencido"
        elif dias_restantes == 0:
            aviso = "Vence hoy"
        else:
            aviso = f"Vence en {dias_restantes} día(s)"

        print(f"{expediente.codigo} | {expediente.fecha_limite} | {aviso}")
        hay_resultados = True

    if not hay_resultados:
        print("No hay expedientes próximos a vencer ni vencidos.")


def seleccionar_prioridad():
    while True:
        print("\n=== SELECCIONAR PRIORIDAD ===")
        print("1. Normal")
        print("2. Urgente")
        print("3. Muy urgente")

        opcion = input("Seleccione una opción: ").strip()

        prioridades = {
            "1": "Normal",
            "2": "Urgente",
            "3": "Muy urgente"
        }

        if opcion in prioridades:
            return prioridades[opcion]

        print("ERROR: Seleccione una opción válida.")
def registrar_expediente(dni):

    print("\n=== REGISTRAR SOLICITUD ===")

    while True:
        asunto = input("Ingrese asunto: ").strip()

        if asunto != "":
            break
        else:
            print("ERROR: El asunto no puede estar vacío.")

    while True:
        descripcion = input("Describa su solicitud: ").strip()

        if descripcion != "":
            break
        else:
            print("ERROR: La descripción no puede estar vacía.")

    while True:
        direccion = input("Ingrese dirección: ").strip()

        if direccion != "":
            break
        else:
            print("ERROR: La dirección no puede estar vacía.")

    # GENERAR CODIGO SIN REPETIR
    numero = 1

    for expediente in expedientes:

        numero_actual = numero_de_codigo(expediente)

        if numero_actual is not None and numero_actual >= numero:
            numero = numero_actual + 1

    codigo = "E-" + str(numero)


    expediente = Expediente(
        codigo, dni, asunto, descripcion, direccion
    )

    expediente.prioridad_solicitada = seleccionar_prioridad()

    expedientes.append(expediente)
    guardar_expedientes()

    print("\nSolicitud registrada correctamente.")
    mostrar_expediente_completo(expediente)


def consultar_expedientes(dni):

    print("\n=== MIS EXPEDIENTES ===")

    encontrado = False

    for expediente in expedientes:

        if expediente.dni == dni:

            mostrar_expediente_completo(expediente)
            encontrado = True

    if encontrado == False:
        print("No tienes expedientes registrados.")


def buscar_expediente():

    codigo = input("Ingrese código: ").strip()

    encontrado = False

    for expediente in expedientes:

        if expediente.codigo == codigo:

            mostrar_expediente_completo(expediente)
            encontrado = True
            break

    if encontrado == False:
        print("Expediente no encontrado.")

def ordenar_expedientes():
    print("\n=== EXPEDIENTES ORDENADOS ===")

    if len(expedientes) == 0:
        print("No hay expedientes para ordenar.")
        return

    # Ordenar por codigo
    ordenados = sorted(
        expedientes,
        key=lambda e: (
            numero_de_codigo(e) is None,
            numero_de_codigo(e) or 0
        )
    )

    for expediente in ordenados:
        print("\nCódigo:", expediente.codigo)
        print("Asunto:", expediente.asunto)
        print("Estado:", expediente.estado)
        print("Gerencia:", expediente.gerencia)
        print("Subgerencia:", expediente.subgerencia)

def ordenar_expedientes_por_prioridad():
    print("\n=== EXPEDIENTES POR PRIORIDAD ===")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    niveles = {
        "Muy urgente": 1,
        "Urgente": 2,
        "Normal": 3
    }

    ordenados = sorted(
        expedientes,
        key=lambda e: niveles.get(
            getattr(e, "prioridad", "Normal"), 3
        )
    )

    for expediente in ordenados:
        print("\nCódigo:", expediente.codigo)
        print("Asunto:", expediente.asunto)
        print("Prioridad:", getattr(expediente, "prioridad", "Normal"))
        print("Estado:", expediente.estado)

def derivar_expediente():

    print("\n=== DERIVAR EXPEDIENTE ===")

    codigo = input("Ingrese código: ").strip()
    encontrado = False

    for expediente in expedientes:

        if expediente.codigo == codigo:

            encontrado = True

            if expediente.estado == "Validado" or expediente.estado == "Devuelto a Mesa de Partes":

                mostrar_expediente_completo(expediente)

                print("\n=== GERENCIAS ===")

                for i in range(len(gerencias)):
                    print(i + 1, "-", gerencias[i])

                opcion = input("Seleccione gerencia: ")

                if opcion.isdigit():

                    numero = int(opcion)

                    if numero >= 1 and numero <= len(gerencias):

                        expediente.gerencia = gerencias[numero - 1]
                        expediente.subgerencia = "Sin asignar"
                        expediente.estado = "Derivado a gerencia"
                        expediente.motivo_devolucion = "Ninguno"

                        guardar_expedientes()

                        print("\nExpediente derivado correctamente.")
                        print("Gerencia:", expediente.gerencia)

                    else:
                        print("ERROR: Gerencia incorrecta.")

                else:
                    print("ERROR: Ingrese un número.")

            else:
                print("El expediente no está listo para derivarse.")

            break

    if encontrado == False:
        print("Expediente no encontrado.")
