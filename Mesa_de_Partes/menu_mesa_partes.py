from estado import expedientes
from operaciones import mostrar_expediente_completo, derivar_expediente, buscar_expediente, ordenar_expedientes
from almacenamiento import guardar_expedientes


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
