from expediente import Expediente
from estado import ciudadanos, expedientes, gerencias
from almacenamiento import guardar_expedientes
from datetime import datetime

def buscar_ciudadano(dni):

    for ciudadano in ciudadanos:

        if ciudadano.dni == dni:
            return ciudadano

    return None


def numero_de_codigo(expediente):
    if expediente is None:
        return None

    codigo = getattr(expediente, "codigo", None)

    if not isinstance(codigo, str):
        return None

    codigo = codigo.strip().upper()
    partes = codigo.split("-")

    if len(partes) != 2:
        return None

    if partes[0] != "E" or not partes[1].isdigit():
        return None

    numero = int(partes[1])

    if numero <= 0:
        return None

    return numero



def mostrar_expediente_completo(expediente):

    print("\n=== DATOS DEL CIUDADANO ===")

    ciudadano = buscar_ciudadano(expediente.dni)

    if ciudadano is None:
        print("Ciudadano no encontrado.")

    else:
        print("Nombre:", ciudadano.nombre)
        print("Apellido:", ciudadano.apellido)
        print("Correo:", ciudadano.correo)
        print("Fecha de emisión del DNI:", ciudadano.fecha_emision_dni)

    expediente.mostrar_datos()

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

    expediente.prioridad = seleccionar_prioridad()

    expedientes.append(expediente)
    guardar_expedientes()

    print("\nSolicitud registrada correctamente.")
    print("Fecha y hora de registro:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
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
def ver_tiempos():

    print("\n=== TIEMPO DE TRAMITE (SOLO PERSONAL) ===")

    if len(expedientes) == 0:
        print("No hay expedientes.")
        return

    for expediente in expedientes:

        print("\nCódigo:", expediente.codigo)
        print("Estado:", expediente.estado)
        print("Fecha de registro:", expediente.fecha_registro)
        print("Fecha de cierre:", expediente.fecha_cierre)
        print("Tiempo total:", expediente.tiempo_total())


def solicitudes_pendientes(dni):

    # Solicitudes del ciudadano que todavía no fueron recibidas
    pendientes = []

    for expediente in expedientes:

        if expediente.dni == dni and expediente.estado == "Pendiente de recepción":
            pendientes.append(expediente)

    return pendientes


def pedir_texto_no_vacio(mensaje):

    while True:

        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("ERROR: Este dato no puede estar vacío.")


def editar_solicitud(dni):

    print("\n=== EDITAR SOLICITUD ===")

    pendientes = solicitudes_pendientes(dni)

    if len(pendientes) == 0:
        print("No tienes solicitudes pendientes de recepción para editar.")
        return

    print("Solicitudes que puedes editar:")

    for expediente in pendientes:
        print("-", expediente.codigo, ":", expediente.asunto)

    codigo = input("Ingrese el código de la solicitud: ").strip().upper()

    seleccionado = None

    for expediente in pendientes:

        if expediente.codigo == codigo:
            seleccionado = expediente

    if seleccionado is None:
        print("ERROR: El código no existe o la solicitud no se puede editar.")
        return

    print("\n¿Qué dato desea cambiar?")
    print("1. Asunto")
    print("2. Descripción")
    print("3. Dirección")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        seleccionado.asunto = pedir_texto_no_vacio("Nuevo asunto: ")

    elif opcion == "2":
        seleccionado.descripcion = pedir_texto_no_vacio("Nueva descripción: ")

    elif opcion == "3":
        seleccionado.direccion = pedir_texto_no_vacio("Nueva dirección: ")

    else:
        print("ERROR: Opción incorrecta.")
        return

    guardar_expedientes()

    print("\nSolicitud actualizada correctamente.")
    mostrar_expediente_completo(seleccionado)