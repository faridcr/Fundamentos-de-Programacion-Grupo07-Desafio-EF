from estado import trabajadores
from menu_mesa_partes import menu_mesa_partes
from menu_gerencias import menu_gestion_ambiental, menu_limpieza_publica, menu_seguridad_ciudadana, menu_desarrollo_urbano


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
