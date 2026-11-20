

from persona import Persona

class Ciudadano(Persona):

    def __init__(self, dni, nombre, apellido, correo, usuario="", contrasena="", fecha_emision_dni="No registrada"):
        super().__init__(dni, nombre, apellido, correo)
        self.usuario = usuario
        self.contrasena = contrasena
        self.fecha_emision_dni = fecha_emision_dni

    def mostrar_datos(self):
        print("=== DATOS DEL CIUDADANO ===")
        super().mostrar_datos()
        if self.usuario != "":
            print("Usuario:", self.usuario)
        print("Fecha de emisión del DNI:", self.fecha_emision_dni)