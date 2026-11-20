

from persona import Persona

class Ciudadano(Persona):
    def __init__(self, dni, nombre, apellido, correo, fecha_emision_dni="No registrada"):
        super().__init__(dni, nombre, apellido, correo)
        self.fecha_emision_dni = fecha_emision_dni

    def mostrar_datos(self):
        print("=== DATOS DEL CIUDADANO ===")
        super().mostrar_datos()
        print("Fecha de emisión del DNI:", self.fecha_emision_dni)
