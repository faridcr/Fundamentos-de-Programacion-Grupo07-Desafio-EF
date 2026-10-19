from operaciones import registrar_expediente, consultar_expedientes


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
