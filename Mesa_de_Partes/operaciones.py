from expediente import Expediente
from estado import ciudadanos, expedientes, gerencias
from almacenamiento import guardar_expedientes


def mostrar_expediente_completo(expediente):

    print("\n=== DATOS DEL CIUDADANO ===")

    encontrado = False

    for ciudadano in ciudadanos:

        if ciudadano.dni == expediente.dni:

            print("Nombre:", ciudadano.nombre)
            print("Apellido:", ciudadano.apellido)
            print("Correo:", ciudadano.correo)

            encontrado = True
            break

    if encontrado == False:
        print("Ciudadano no encontrado.")

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

        partes = expediente.codigo.split("-")

        if len(partes) == 2 and partes[1].isdigit():

            numero_actual = int(partes[1])

            if numero_actual >= numero:
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

    codigos = []

    for expediente in expedientes:

        partes = expediente.codigo.split("-")

        if len(partes) == 2 and partes[1].isdigit():

            numero = int(partes[1])
            codigos.append(numero)

    codigos.sort()

    if len(codigos) == 0:
        print("No hay expedientes para ordenar.")

    for numero in codigos:

        codigo = "E-" + str(numero)

        for expediente in expedientes:

            if expediente.codigo == codigo:

                print("\nCódigo:", expediente.codigo)
                print("Asunto:", expediente.asunto)
                print("Estado:", expediente.estado)
                print("Gerencia:", expediente.gerencia)
                print("Subgerencia:", expediente.subgerencia)

                break


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
