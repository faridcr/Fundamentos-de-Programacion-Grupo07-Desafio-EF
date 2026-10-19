from ciudadano import Ciudadano
from estado import ciudadanos
from almacenamiento import cargar_ciudadanos, guardar_ciudadanos, cargar_expedientes
from menu_ciudadano import menu_ciudadano
from acceso import iniciar_sesion


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
