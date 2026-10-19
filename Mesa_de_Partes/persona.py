
class Persona:
    def __init__(self, dni, nombre, apellido, correo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_datos(self):
        print("DNI:", self.dni)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Correo:", self.correo)
