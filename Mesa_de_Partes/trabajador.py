from persona import Persona


class Trabajador(Persona):
    def __init__(self, dni, nombre, apellido, correo, usuario, contrasena, area):
        super().__init__(dni, nombre, apellido, correo)

        self.usuario = usuario
        self.contrasena = contrasena
        self.area = area

    def verificar_contrasena(self, contrasena):
        return self.contrasena == contrasena

    def mostrar_datos(self):
        print("\n=== DATOS DEL TRABAJADOR ===")
        super().mostrar_datos()
        print("Usuario:", self.usuario)
        print("Área:", self.area)
