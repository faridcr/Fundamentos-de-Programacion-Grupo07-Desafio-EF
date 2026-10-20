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

    # Los códigos con formato raro van al final
    ordenados = sorted(
        expedientes,
        key=lambda e: (numero_de_codigo(e) is None, numero_de_codigo(e) or 0)
    )

    for expediente in ordenados:

        print("\nCódigo:", expediente.codigo)
        print("Asunto:", expediente.asunto)
        print("Estado:", expediente.estado)
        print("Gerencia:", expediente.gerencia)
        print("Subgerencia:", expediente.subgerencia)


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
