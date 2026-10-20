from estado import expedientes, subgerencias
from operaciones import mostrar_expediente_completo
from almacenamiento import guardar_expedientes


# ---------------------------------------------------------------
# FUNCIONES COMUNES (las usan todos los menús)
# ---------------------------------------------------------------

def buscar_en_area(codigo, campo, area):
    # campo es "gerencia" o "subgerencia"

    for expediente in expedientes:

        if expediente.codigo == codigo and getattr(expediente, campo) == area:
            return expediente

    return None


def ver_expedientes(campo, area):

    encontrado = False

    for expediente in expedientes:

        if getattr(expediente, campo) == area:

            mostrar_expediente_completo(expediente)
            encontrado = True

    if encontrado == False:
        print("No hay expedientes asignados.")


def recibir(expediente, estado_pendiente, estado_recibido):

    if expediente.estado == estado_pendiente:

        expediente.estado = estado_recibido
        guardar_expedientes()

        print("Expediente recibido correctamente.")

    else:
        print("El expediente no está pendiente de recepción.")


def devolver(expediente, estados_permitidos):

    if expediente.estado not in estados_permitidos:
        print("Este expediente no se puede devolver.")
        return

    motivo = input("Motivo de devolución: ").strip()

    if motivo == "":
        print("ERROR: Debe ingresar un motivo.")
        return

    expediente.estado = "Devuelto a Mesa de Partes"
    expediente.gerencia = "Sin asignar"
    expediente.subgerencia = "Sin asignar"
    expediente.motivo_devolucion = motivo

    guardar_expedientes()

    print("Expediente devuelto a Mesa de Partes.")
    print("Motivo:", motivo)


# ---------------------------------------------------------------
# MENU PARA GERENCIAS QUE DERIVAN A SUBGERENCIAS (Gestión Ambiental)
# ---------------------------------------------------------------

def menu_gerencia_con_subgerencias(gerencia):

    propias = [s for s in subgerencias if s.gerencia == gerencia]

    while True:

        print("\n=== GERENCIA:", gerencia.upper(), "===")
        print("1. Ver expedientes")
        print("2. Recibir expediente")
        print("3. Derivar a subgerencia")
        print("4. Devolver por área incorrecta")
        print("5. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            break

        elif opcion == "1":
            ver_expedientes("gerencia", gerencia)

        elif opcion in ("2", "3", "4"):

            codigo = input("Ingrese código: ").strip()
            expediente = buscar_en_area(codigo, "gerencia", gerencia)

            if expediente is None:
                print("Expediente no encontrado.")
                continue

            if opcion == "2":
                recibir(expediente, "Derivado a gerencia", "Recibido en gerencia")

            elif opcion == "3":
                derivar_a_subgerencia(expediente, propias)

            elif opcion == "4":
                devolver(expediente, ["Derivado a gerencia", "Recibido en gerencia"])

        else:
            print("ERROR: Opción incorrecta.")


def derivar_a_subgerencia(expediente, propias):

    if expediente.estado != "Recibido en gerencia":
        print("Primero debe recibir el expediente.")
        return

    if len(propias) == 0:
        print("Esta gerencia no tiene subgerencias registradas.")
        return

    print("\n=== SUBGERENCIAS ===")

    for i in range(len(propias)):
        print(i + 1, "-", propias[i].nombre)

    opcion = input("Seleccione subgerencia: ")

    if not opcion.isdigit():
        print("Ingrese un número.")
        return

    numero = int(opcion)

    if numero < 1 or numero > len(propias):
        print("Subgerencia incorrecta.")
        return

    expediente.subgerencia = propias[numero - 1].nombre
    expediente.estado = "Derivado a subgerencia"

    guardar_expedientes()

    print("Derivación realizada.")
    print("Subgerencia:", expediente.subgerencia)


# ---------------------------------------------------------------
# MENU PARA AREAS QUE ATIENDEN Y CIERRAN EXPEDIENTES
# nivel = "gerencia"      -> Seguridad Ciudadana y Vial, Desarrollo Urbano
# nivel = "subgerencia"   -> Limpieza Pública, Parques y Jardines
# ---------------------------------------------------------------

def menu_atencion(area, nivel):

    estado_pendiente = "Derivado a " + nivel
    estado_recibido = "Recibido en " + nivel
    estados_devolucion = [estado_pendiente, estado_recibido, "En evaluacion"]

    while True:

        print("\n===", nivel.upper() + ":", area.upper(), "===")
        print("1. Ver expedientes")
        print("2. Recibir expediente")
        print("3. Iniciar evaluación")
        print("4. Registrar atención")
        print("5. Emitir respuesta y cerrar")
        print("6. Devolver por área incorrecta")
        print("7. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "7":
            break

        elif opcion == "1":
            ver_expedientes(nivel, area)

        elif opcion in ("2", "3", "4", "5", "6"):

            codigo = input("Ingrese código del expediente: ").strip()
            expediente = buscar_en_area(codigo, nivel, area)

            if expediente is None:
                print("Expediente no encontrado en", area + ".")
                continue

            if opcion == "2":
                recibir(expediente, estado_pendiente, estado_recibido)

            elif opcion == "3":
                iniciar_evaluacion(expediente, estado_recibido)

            elif opcion == "4":
                registrar_atencion(expediente)

            elif opcion == "5":
                cerrar_expediente(expediente)

            elif opcion == "6":
                devolver(expediente, estados_devolucion)

        else:
            print("ERROR: Opción incorrecta.")


def iniciar_evaluacion(expediente, estado_recibido):

    if expediente.estado != estado_recibido:
        print("Primero debe recibir el expediente.")
        return

    expediente.estado = "En evaluacion"
    guardar_expedientes()

    print("Evaluación iniciada.")


def registrar_atencion(expediente):

    if expediente.estado != "En evaluacion":
        print("Primero debe iniciar la evaluación.")
        return

    atencion = input("Describa la atención realizada: ").strip()

    if atencion == "":
        print("ERROR: La atención no puede estar vacía.")
        return

    expediente.atencion = atencion
    expediente.estado = "Atendido"
    guardar_expedientes()

    print("Atención registrada correctamente.")


def cerrar_expediente(expediente):

    if expediente.estado != "Atendido":
        print("Primero debe registrar la atención.")
        return

    respuesta = input("Ingrese respuesta al ciudadano: ").strip()

    if respuesta == "":
        print("ERROR: La respuesta no puede estar vacía.")
        return

    expediente.respuesta = respuesta
    expediente.estado = "Cerrado"
    guardar_expedientes()

    print("Expediente cerrado correctamente.")
