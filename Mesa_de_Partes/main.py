
import json

from ciudadano import Ciudadano
from expediente import Expediente
from trabajador import Trabajador
from subgerencia import Subgerencia


# LISTAS PRINCIPALES
ciudadanos = []
expedientes = []
trabajadores = []
subgerencias = []


# GERENCIAS
gerencias = [
    "Gestión Ambiental",
    "Seguridad Ciudadana y Vial",
    "Desarrollo Urbano"
]


# SUBGERENCIAS
limpieza = Subgerencia("Limpieza Pública", "Gestión Ambiental")
parques = Subgerencia("Parques y Jardines", "Gestión Ambiental")

subgerencias.append(limpieza)
subgerencias.append(parques)


# TRABAJADORES DE PRUEBA
trabajador1 = Trabajador(
    "12345678", "Carlos", "Perez", "carlos@gmail.com",
    "mesa", "mesa123", "Mesa de Partes"
)

trabajador2 = Trabajador(
    "87654321", "Pedro", "Lopez", "pedro@gmail.com",
    "g1", "demo123", "Gestión Ambiental"
)

trabajador3 = Trabajador(
    "11223344", "Luis", "Ramirez", "luis@gmail.com",
    "s1", "demo123", "Limpieza Pública"
)

trabajador4 = Trabajador(
    "44556677", "Miguel", "Torres", "miguel@gmail.com",
    "g2", "demo123", "Seguridad Ciudadana y Vial"
)

# NUEVO TRABAJADOR DE DESARROLLO URBANO
trabajador5 = Trabajador(
    "55667788", "Ana", "Gomez", "ana@gmail.com",
    "g3", "demo123", "Desarrollo Urbano"
)

trabajadores.append(trabajador1)
trabajadores.append(trabajador2)
trabajadores.append(trabajador3)
trabajadores.append(trabajador4)
trabajadores.append(trabajador5)


# CARGAR CIUDADANOS
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

    with open("datos/ciudadanos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# CARGAR EXPEDIENTES
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
            "respuesta": expediente.respuesta
        }

        datos.append(dato)

    with open("datos/expedientes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# MOSTRAR EXPEDIENTE COMPLETO
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


# REGISTRAR EXPEDIENTE
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


# CONSULTAR EXPEDIENTES
def consultar_expedientes(dni):

    print("\n=== MIS EXPEDIENTES ===")

    encontrado = False

    for expediente in expedientes:

        if expediente.dni == dni:

            mostrar_expediente_completo(expediente)
            encontrado = True

    if encontrado == False:
        print("No tienes expedientes registrados.")


# MENU CIUDADANO
def menu_ciudadano(dni):

    while True:

        print("\n=== MENU DEL CIUDADANO ===")
        print("1. Registrar solicitud")
        print("2. Consultar mis expedientes")
        print("3. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_expediente(dni)

        elif opcion == "2":
            consultar_expedientes(dni)

        elif opcion == "3":
            break

        else:
            print("ERROR: Opción incorrecta.")


# BUSCAR EXPEDIENTE POR CODIGO
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


# ORDENAR EXPEDIENTES POR CODIGO
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


# DERIVAR EXPEDIENTE A GERENCIA
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


# MENU MESA DE PARTES
def menu_mesa_partes():

    while True:

        print("\n=== MESA DE PARTES ===")
        print("1. Ver solicitudes pendientes")
        print("2. Validar solicitud")
        print("3. Derivar expediente a gerencia")
        print("4. Buscar expediente por código")
        print("5. Ver expedientes devueltos")
        print("6. Ordenar expedientes por código")
        print("7. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            encontrado = False

            for expediente in expedientes:

                if expediente.estado == "Pendiente de recepción":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay solicitudes pendientes.")

        elif opcion == "2":

            codigo = input("Ingrese código: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo:

                    encontrado = True

                    if expediente.estado == "Pendiente de recepción":

                        mostrar_expediente_completo(expediente)

                        print("\n1. Validar")
                        print("2. Cancelar")

                        confirmar = input("Elige una opción: ")

                        if confirmar == "1":

                            expediente.estado = "Validado"
                            guardar_expedientes()

                            print("Expediente validado correctamente.")

                        elif confirmar == "2":
                            print("Validación cancelada.")

                        else:
                            print("Opción incorrecta.")

                    else:
                        print("Este expediente ya fue procesado.")

                    break

            if encontrado == False:
                print("Expediente no encontrado.")

        elif opcion == "3":
            derivar_expediente()

        elif opcion == "4":
            buscar_expediente()

        elif opcion == "5":

            encontrado = False

            for expediente in expedientes:

                if expediente.estado == "Devuelto a Mesa de Partes":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay expedientes devueltos.")

        elif opcion == "6":
            ordenar_expedientes()

        elif opcion == "7":
            break

        else:
            print("ERROR: Opción incorrecta.")


# MENU GESTION AMBIENTAL
def menu_gestion_ambiental():

    while True:

        print("\n=== GERENCIA: GESTION AMBIENTAL ===")
        print("1. Ver expedientes")
        print("2. Recibir expediente")
        print("3. Derivar a subgerencia")
        print("4. Devolver por área incorrecta")
        print("5. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            encontrado = False

            for expediente in expedientes:

                if expediente.gerencia == "Gestión Ambiental":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay expedientes.")

        elif opcion == "2":

            codigo = input("Ingrese código: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.gerencia == "Gestión Ambiental":

                    encontrado = True

                    if expediente.estado == "Derivado a gerencia":

                        expediente.estado = "Recibido en gerencia"
                        guardar_expedientes()

                        print("Expediente recibido correctamente.")

                    else:
                        print("El expediente no está pendiente de recepción.")

                    break

            if encontrado == False:
                print("Expediente no encontrado.")

        elif opcion == "3":

            codigo = input("Ingrese código: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.gerencia == "Gestión Ambiental":

                    encontrado = True

                    if expediente.estado == "Recibido en gerencia":

                        print("\n=== SUBGERENCIAS ===")

                        for i in range(len(subgerencias)):
                            print(i + 1, "-", subgerencias[i].nombre)

                        opcion_sub = input("Seleccione subgerencia: ")

                        if opcion_sub.isdigit():

                            numero = int(opcion_sub)

                            if numero >= 1 and numero <= len(subgerencias):

                                expediente.subgerencia = subgerencias[numero - 1].nombre
                                expediente.estado = "Derivado a subgerencia"

                                guardar_expedientes()

                                print("Derivación realizada.")
                                print("Subgerencia:", expediente.subgerencia)

                            else:
                                print("Subgerencia incorrecta.")

                        else:
                            print("Ingrese un número.")

                    else:
                        print("Primero debe recibir el expediente.")

                    break

            if encontrado == False:
                print("Expediente no encontrado.")

        elif opcion == "4":

            codigo = input("Ingrese código: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.gerencia == "Gestión Ambiental":

                    encontrado = True

                    if expediente.estado == "Derivado a gerencia" or expediente.estado == "Recibido en gerencia":

                        motivo = input("Motivo de devolución: ").strip()

                        if motivo != "":

                            expediente.estado = "Devuelto a Mesa de Partes"
                            expediente.gerencia = "Sin asignar"
                            expediente.subgerencia = "Sin asignar"

                            guardar_expedientes()

                            print("Expediente devuelto correctamente.")
                            print("Motivo:", motivo)

                        else:
                            print("Debe ingresar un motivo.")

                    else:
                        print("Este expediente no se puede devolver.")

                    break

            if encontrado == False:
                print("Expediente no encontrado.")

        elif opcion == "5":
            break

        else:
            print("ERROR: Opción incorrecta.")


# MENU LIMPIEZA PUBLICA
def menu_limpieza_publica():

    while True:

        print("\n=== SUBGERENCIA: LIMPIEZA PUBLICA ===")
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

            encontrado = False

            for expediente in expedientes:

                if expediente.subgerencia == "Limpieza Pública":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay expedientes asignados.")

        elif opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":

            codigo = input("Ingrese código: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.subgerencia == "Limpieza Pública":

                    encontrado = True

                    if opcion == "2":

                        if expediente.estado == "Derivado a subgerencia":

                            expediente.estado = "Recibido en subgerencia"
                            guardar_expedientes()

                            print("Expediente recibido correctamente.")

                        else:
                            print("El expediente no está pendiente de recepción.")

                    elif opcion == "3":

                        if expediente.estado == "Recibido en subgerencia":

                            expediente.estado = "En evaluacion"
                            guardar_expedientes()

                            print("Evaluación iniciada.")

                        else:
                            print("Primero debe recibir el expediente.")

                    elif opcion == "4":

                        if expediente.estado == "En evaluacion":

                            atencion = input("Describa la atención realizada: ").strip()

                            if atencion != "":

                                expediente.atencion = atencion
                                expediente.estado = "Atendido"

                                guardar_expedientes()

                                print("Atención registrada correctamente.")

                            else:
                                print("La atención no puede estar vacía.")

                        else:
                            print("Primero debe iniciar la evaluación.")

                    elif opcion == "5":

                        if expediente.estado == "Atendido":

                            respuesta = input("Respuesta al ciudadano: ").strip()

                            if respuesta != "":

                                expediente.respuesta = respuesta
                                expediente.estado = "Cerrado"

                                guardar_expedientes()

                                print("Expediente cerrado correctamente.")

                            else:
                                print("La respuesta no puede estar vacía.")

                        else:
                            print("Primero debe registrar la atención.")

                    elif opcion == "6":

                        if expediente.estado == "Derivado a subgerencia" or expediente.estado == "Recibido en subgerencia" or expediente.estado == "En evaluacion":

                            motivo = input("Motivo de devolución: ").strip()

                            if motivo != "":

                                expediente.estado = "Devuelto a Mesa de Partes"
                                expediente.gerencia = "Sin asignar"
                                expediente.subgerencia = "Sin asignar"

                                guardar_expedientes()

                                print("Expediente devuelto correctamente.")
                                print("Motivo:", motivo)

                            else:
                                print("Debe ingresar un motivo.")

                        else:
                            print("Este expediente no se puede devolver.")

                    break

            if encontrado == False:
                print("Expediente no encontrado en Limpieza Pública.")

        else:
            print("ERROR: Opción incorrecta.")


# MENU SEGURIDAD CIUDADANA
def menu_seguridad_ciudadana():

    while True:

        print("\n=== GERENCIA: SEGURIDAD CIUDADANA Y VIAL ===")
        print("1. Ver expedientes")
        print("2. Recibir expediente")
        print("3. Iniciar evaluación")
        print("4. Registrar atención")
        print("5. Emitir respuesta y cerrar")
        print("6. Devolver por área incorrecta")
        print("7. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            encontrado = False

            for expediente in expedientes:

                if expediente.gerencia == "Seguridad Ciudadana y Vial":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay expedientes asignados.")

        elif opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":

            codigo = input("Ingrese código del expediente: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.gerencia == "Seguridad Ciudadana y Vial":

                    encontrado = True

                    if opcion == "2":

                        if expediente.estado == "Derivado a gerencia":

                            expediente.estado = "Recibido en gerencia"
                            guardar_expedientes()

                            print("Expediente recibido correctamente.")

                        else:
                            print("El expediente no está pendiente de recepción.")

                    elif opcion == "3":

                        if expediente.estado == "Recibido en gerencia":

                            expediente.estado = "En evaluacion"
                            guardar_expedientes()

                            print("Evaluación iniciada.")

                        else:
                            print("Primero debe recibir el expediente.")

                    elif opcion == "4":

                        if expediente.estado == "En evaluacion":

                            atencion = input("Describa la atención realizada: ").strip()

                            if atencion != "":

                                expediente.atencion = atencion
                                expediente.estado = "Atendido"

                                guardar_expedientes()

                                print("Atención registrada correctamente.")

                            else:
                                print("La atención no puede estar vacía.")

                        else:
                            print("Primero debe iniciar la evaluación.")

                    elif opcion == "5":

                        if expediente.estado == "Atendido":

                            respuesta = input("Ingrese respuesta al ciudadano: ").strip()

                            if respuesta != "":

                                expediente.respuesta = respuesta
                                expediente.estado = "Cerrado"

                                guardar_expedientes()

                                print("Expediente cerrado correctamente.")

                            else:
                                print("La respuesta no puede estar vacía.")

                        else:
                            print("Primero debe registrar la atención.")

                    elif opcion == "6":

                        if expediente.estado == "Derivado a gerencia" or expediente.estado == "Recibido en gerencia" or expediente.estado == "En evaluacion":

                            motivo = input("Motivo de devolución: ").strip()

                            if motivo != "":

                                expediente.estado = "Devuelto a Mesa de Partes"
                                expediente.gerencia = "Sin asignar"
                                expediente.subgerencia = "Sin asignar"

                                guardar_expedientes()

                                print("Expediente devuelto a Mesa de Partes.")
                                print("Motivo:", motivo)

                            else:
                                print("Debe ingresar un motivo.")

                        else:
                            print("Este expediente no se puede devolver.")

                    break

            if encontrado == False:
                print("Expediente no encontrado en Seguridad Ciudadana.")

        elif opcion == "7":
            break

        else:
            print("ERROR: Opción incorrecta.")


# NUEVO MENU DESARROLLO URBANO
def menu_desarrollo_urbano():

    while True:

        print("\n=== GERENCIA: DESARROLLO URBANO ===")
        print("1. Ver expedientes")
        print("2. Recibir expediente")
        print("3. Iniciar evaluación")
        print("4. Registrar atención")
        print("5. Emitir respuesta y cerrar")
        print("6. Devolver por área incorrecta")
        print("7. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":

            encontrado = False

            for expediente in expedientes:

                if expediente.gerencia == "Desarrollo Urbano":

                    mostrar_expediente_completo(expediente)
                    encontrado = True

            if encontrado == False:
                print("No hay expedientes asignados.")

        elif opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":

            codigo = input("Ingrese código del expediente: ").strip()
            encontrado = False

            for expediente in expedientes:

                if expediente.codigo == codigo and expediente.gerencia == "Desarrollo Urbano":

                    encontrado = True

                    if opcion == "2":

                        if expediente.estado == "Derivado a gerencia":

                            expediente.estado = "Recibido en gerencia"
                            guardar_expedientes()

                            print("Expediente recibido correctamente.")

                        else:
                            print("El expediente no está pendiente de recepción.")

                    elif opcion == "3":

                        if expediente.estado == "Recibido en gerencia":

                            expediente.estado = "En evaluacion"
                            guardar_expedientes()

                            print("Evaluación iniciada.")

                        else:
                            print("Primero debe recibir el expediente.")

                    elif opcion == "4":

                        if expediente.estado == "En evaluacion":

                            atencion = input("Describa la atención realizada: ").strip()

                            if atencion != "":

                                expediente.atencion = atencion
                                expediente.estado = "Atendido"

                                guardar_expedientes()

                                print("Atención registrada correctamente.")

                            else:
                                print("ERROR: La atención no puede estar vacía.")

                        else:
                            print("Primero debe iniciar la evaluación.")

                    elif opcion == "5":

                        if expediente.estado == "Atendido":

                            respuesta = input("Ingrese respuesta al ciudadano: ").strip()

                            if respuesta != "":

                                expediente.respuesta = respuesta
                                expediente.estado = "Cerrado"

                                guardar_expedientes()

                                print("Expediente cerrado correctamente.")

                            else:
                                print("ERROR: La respuesta no puede estar vacía.")

                        else:
                            print("Primero debe registrar la atención.")

                    elif opcion == "6":

                        if expediente.estado == "Derivado a gerencia" or expediente.estado == "Recibido en gerencia" or expediente.estado == "En evaluacion":

                            motivo = input("Motivo de devolución: ").strip()

                            if motivo != "":

                                expediente.estado = "Devuelto a Mesa de Partes"
                                expediente.gerencia = "Sin asignar"
                                expediente.subgerencia = "Sin asignar"

                                guardar_expedientes()

                                print("Expediente devuelto a Mesa de Partes.")
                                print("Motivo:", motivo)

                            else:
                                print("ERROR: Debe ingresar un motivo.")

                        else:
                            print("Este expediente no se puede devolver.")

                    break

            if encontrado == False:
                print("Expediente no encontrado en Desarrollo Urbano.")

        elif opcion == "7":
            break

        else:
            print("ERROR: Opción incorrecta.")


# INICIAR SESION
def iniciar_sesion():

    print("\n=== INICIAR SESION ===")

    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contraseña: ").strip()

    encontrado = False

    for trabajador in trabajadores:

        if trabajador.usuario == usuario and trabajador.contrasena == contrasena:

            encontrado = True

            print("\nBienvenido:", trabajador.nombre)
            print("Área:", trabajador.area)

            if trabajador.area == "Mesa de Partes":
                menu_mesa_partes()

            elif trabajador.area == "Gestión Ambiental":
                menu_gestion_ambiental()

            elif trabajador.area == "Limpieza Pública":
                menu_limpieza_publica()

            elif trabajador.area == "Seguridad Ciudadana y Vial":
                menu_seguridad_ciudadana()

            elif trabajador.area == "Desarrollo Urbano":
                menu_desarrollo_urbano()

            else:
                print("El menú de esta área todavía no está disponible.")

            break

    if encontrado == False:
        print("Usuario o contraseña incorrectos.")


# CARGAR DATOS AL INICIAR
cargar_ciudadanos()
cargar_expedientes()


# MENU PRINCIPAL
while True:

    print("\n=== MESA DE PARTES DIGITAL - SJM ===")
    print("1. Ciudadano")
    print("2. Trabajador municipal")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":

        print("\n=== ACCESO CIUDADANO ===")
        print("1. Registrar nuevo ciudadano")
        print("2. Ya estoy registrado")
        print("3. Volver")

        opcion_ciudadano = input("Elige una opción: ")

        if opcion_ciudadano == "1":

            print("\n=== REGISTRO DE CIUDADANO ===")

            while True:

                dni = input("Ingrese DNI: ").strip()

                if len(dni) == 8 and dni.isdigit():
                    break

                else:
                    print("ERROR: El DNI debe tener 8 números.")

            repetido = False

            for ciudadano in ciudadanos:

                if ciudadano.dni == dni:
                    repetido = True
                    break

            if repetido == True:

                print("Este ciudadano ya está registrado.")

            else:

                while True:

                    nombre = input("Ingrese nombre: ").strip()

                    if nombre != "" and not nombre.isdigit():
                        break

                    else:
                        print("Ingrese un nombre válido.")

                while True:

                    apellido = input("Ingrese apellido: ").strip()

                    if apellido != "" and not apellido.isdigit():
                        break

                    else:
                        print("Ingrese un apellido válido.")

                while True:

                    correo = input("Ingrese correo: ").strip()

                    if "@" in correo and "." in correo:
                        break

                    else:
                        print("Correo incorrecto.")

                ciudadano = Ciudadano(
                    dni, nombre, apellido, correo
                )

                ciudadanos.append(ciudadano)
                guardar_ciudadanos()

                print("\nCiudadano registrado correctamente.")
                ciudadano.mostrar_datos()

                menu_ciudadano(dni)

        elif opcion_ciudadano == "2":

            dni = input("Ingrese DNI: ").strip()

            encontrado = False

            for ciudadano in ciudadanos:

                if ciudadano.dni == dni:
                    encontrado = True
                    break

            if encontrado == True:

                print("Bienvenido al sistema.")
                menu_ciudadano(dni)

            else:
                print("Ciudadano no registrado.")

        elif opcion_ciudadano == "3":
            print("Volviendo al menú principal.")

        else:
            print("Opción incorrecta.")

    elif opcion == "2":
        iniciar_sesion()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("ERROR: Opción incorrecta.")
