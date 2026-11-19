from ciudadano import Ciudadano
from estado import ciudadanos
from almacenamiento import cargar_todo, guardar_ciudadanos
from menu_ciudadano import menu_ciudadano
from acceso import iniciar_sesion
from validaciones import dni_valido, correo_valido, nombre_valido, usuario_valido, contrasena_valida

def existe_ciudadano(dni):

    for ciudadano in ciudadanos:

        if ciudadano.dni == dni:
            return True

    return False


def existe_usuario(usuario):

    for ciudadano in ciudadanos:

        if ciudadano.usuario == usuario:
            return True

    return False


def buscar_por_usuario(usuario):

    for ciudadano in ciudadanos:

        if ciudadano.usuario == usuario:
            return ciudadano

    return None


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


def pedir_usuario():

    while True:

        usuario = input("Ingrese usuario: ").strip()

        if not usuario_valido(usuario):
            print("ERROR: El usuario debe tener de 4 a 20 caracteres y no llevar espacios.")

        elif existe_usuario(usuario):
            print("ERROR: El usuario no está disponible. Intente con otro.")

        else:
            return usuario


def pedir_contrasena():

    while True:

        contrasena = input("Ingrese contraseña: ").strip()

        if not contrasena_valida(contrasena):
            print("ERROR: La contraseña debe tener al menos 6 caracteres.")

        else:
            confirmacion = input("Confirme contraseña: ").strip()

            if contrasena == confirmacion:
                return contrasena

            else:
                print("ERROR: Las contraseñas no coinciden.")


def registrar_ciudadano():

    print("\n=== REGISTRO DE CIUDADANO ===")

    dni = pedir_dni()

    if existe_ciudadano(dni):
        print("Este ciudadano ya está registrado.")
        return

    nombre = pedir_nombre("nombre")
    apellido = pedir_nombre("apellido")
    correo = pedir_correo()
    usuario = pedir_usuario()
    contrasena = pedir_contrasena()

    ciudadano = Ciudadano(dni, nombre, apellido, correo, usuario, contrasena)

    ciudadanos.append(ciudadano)
    guardar_ciudadanos()

    print("\nCiudadano registrado correctamente.")
    ciudadano.mostrar_datos()

    menu_ciudadano(dni)


def acceso_ciudadano_registrado():

    print("\n=== INICIAR SESIÓN ===")

    intentos = 0

    while intentos < 3:

        usuario = input("Ingrese usuario: ").strip()
        contrasena = input("Ingrese contraseña: ").strip()

        ciudadano = buscar_por_usuario(usuario)

        if usuario != "" and ciudadano is not None and ciudadano.contrasena == contrasena:
            print("\nBienvenido:", ciudadano.nombre)
            menu_ciudadano(ciudadano.dni)
            return

        intentos = intentos + 1

        if intentos < 3:
            print("Usuario o contraseña incorrectos. Intentos restantes:", 3 - intentos)

    print("Demasiados intentos fallidos. Volviendo al menú de acceso.")


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
