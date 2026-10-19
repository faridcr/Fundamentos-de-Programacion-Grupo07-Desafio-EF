from estado import expedientes, subgerencias
from operaciones import mostrar_expediente_completo
from almacenamiento import guardar_expedientes


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
