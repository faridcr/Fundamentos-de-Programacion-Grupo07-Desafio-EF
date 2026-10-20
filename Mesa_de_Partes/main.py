from ciudadano import Ciudadano
from estado import ciudadanos
from almacenamiento import cargar_todo, guardar_ciudadanos
from menu_ciudadano import menu_ciudadano
from acceso import iniciar_sesion
from validaciones import dni_valido, correo_valido, nombre_valido


def existe_ciudadano(dni):

    for ciudadano in ciudadanos:

        if ciudadano.dni == dni:
            return True

    return False


def pedir_dni():

    while True:

        dni = input("Ingrese DNI: ").strip()

        if dni_valido(dni):
            return dni

        print("ERROR: El DNI debe tener 8 números.")


def pedir_nombre(etiqueta):

    while True:

        texto = input("Ingrese " + etiqueta + ": ").strip()

        if nombre_valido(texto):
            return texto

        print("Ingrese un", etiqueta, "válido (solo letras).")


def pedir_correo():

    while True:

        correo = input("Ingrese correo: ").strip()

        if correo_valido(correo):
            return correo

        print("Correo incorrecto. Ejemplo: nombre@dominio.com")


def registrar_ciudadano():

    print("\n=== REGISTRO DE CIUDADANO ===")

    dni = pedir_dni()

    if existe_ciudadano(dni):
        print("Este ciudadano ya está registrado.")
        return

    nombre = pedir_nombre("nombre")
    apellido = pedir_nombre("apellido")
    correo = pedir_correo()

    ciudadano = Ciudadano(dni, nombre, apellido, correo)

    ciudadanos.append(ciudadano)
    guardar_ciudadanos()

    print("\nCiudadano registrado correctamente.")
    ciudadano.mostrar_datos()

    menu_ciudadano(dni)


def acceso_ciudadano_registrado():

    dni = pedir_dni()

    if existe_ciudadano(dni):
        print("Bienvenido al sistema.")
        menu_ciudadano(dni)

    else:
        print("Ciudadano no registrado.")


def menu_acceso_ciudadano():

    print("\n=== ACCESO CIUDADANO ===")
    print("1. Registrar nuevo ciudadano")
    print("2. Ya estoy registrado")
    print("3. Volver")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_ciudadano()

    elif opcion == "2":
        acceso_ciudadano_registrado()

    elif opcion == "3":
        print("Volviendo al menú principal.")

    else:
        print("Opción incorrecta.")


# CARGAR DATOS AL INICIAR
cargar_todo()


# MENU PRINCIPAL
while True:

    print("\n=== MESA DE PARTES DIGITAL - SJM ===")
    print("1. Ciudadano")
    print("2. Trabajador municipal")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        menu_acceso_ciudadano()

    elif opcion == "2":
        iniciar_sesion()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("ERROR: Opción incorrecta.")
