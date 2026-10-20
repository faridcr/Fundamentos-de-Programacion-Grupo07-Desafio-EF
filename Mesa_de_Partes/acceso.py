from estado import trabajadores, gerencias, subgerencias
from menu_mesa_partes import menu_mesa_partes
from menu_gerencias import menu_gerencia_con_subgerencias, menu_atencion


def abrir_menu(area):

    if area == "Mesa de Partes":
        menu_mesa_partes()
        return

    if area in gerencias:

        tiene_subgerencias = False

        for subgerencia in subgerencias:
            if subgerencia.gerencia == area:
                tiene_subgerencias = True

        if tiene_subgerencias:
            menu_gerencia_con_subgerencias(area)
        else:
            menu_atencion(area, "gerencia")

        return

    for subgerencia in subgerencias:

        if subgerencia.nombre == area:
            menu_atencion(area, "subgerencia")
            return

    print("El menú de esta área todavía no está disponible.")


def iniciar_sesion():

    print("\n=== INICIAR SESION ===")

    usuario = input("Ingrese usuario: ").strip()
    contrasena = input("Ingrese contraseña: ").strip()

    for trabajador in trabajadores:

        if trabajador.usuario == usuario and trabajador.verificar_contrasena(contrasena):

            print("\nBienvenido:", trabajador.nombre)
            print("Área:", trabajador.area)

            abrir_menu(trabajador.area)
            return

    print("Usuario o contraseña incorrectos.")
