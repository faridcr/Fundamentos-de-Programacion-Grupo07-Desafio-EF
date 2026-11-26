from operaciones import cancelar_solicitud, registrar_expediente, consultar_expedientes, editar_solicitud


def menu_ciudadano(dni):

    while True:

        print("\n=== MENU DEL CIUDADANO ===")
        print("1. Registrar solicitud")
        print("2. Consultar mis expedientes")
        print("3. Editar una solicitud")
        print("4. Cancelar una solicitud")
        print("5. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_expediente(dni)

        elif opcion == "2":
            consultar_expedientes(dni)

        elif opcion == "3":
            editar_solicitud(dni)

        elif opcion == "4":
            cancelar_solicitud(dni)

        elif opcion == "5":
            break

        else:
            print("ERROR: Opción incorrecta.")