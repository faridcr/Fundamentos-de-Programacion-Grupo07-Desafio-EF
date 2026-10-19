

from persona import Persona

class Ciudadano(Persona):
    def __init__(self, dni, nombre, apellido, correo):
        super().__init__(dni, nombre, apellido, correo)

    def mostrar_datos(self):
        print("=== DATOS DEL CIUDADANO ===")
        super().mostrar_datos()
