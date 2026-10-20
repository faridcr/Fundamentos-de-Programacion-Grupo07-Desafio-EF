
class Expediente:
    def __init__(self, codigo, dni, asunto, descripcion, direccion):
        self.codigo = codigo
        self.dni = dni
        self.asunto = asunto
        self.descripcion = descripcion
        self.direccion = direccion
        self.estado = "Pendiente de recepción"
        self.gerencia = "Sin asignar"
        self.subgerencia = "Sin asignar"
        self.atencion = "Pendiente"
        self.respuesta = "Pendiente"
        self.motivo_devolucion = "Ninguno"

    def mostrar_datos(self):
        print("\n=== DATOS DEL EXPEDIENTE ===")
        print("Código:", self.codigo)
        print("DNI:", self.dni)
        print("Asunto:", self.asunto)
        print("Descripción:", self.descripcion)
        print("Dirección:", self.direccion)
        print("Estado:", self.estado)
        print("Gerencia:", self.gerencia)
        print("Subgerencia:", self.subgerencia)
        print("Atención realizada:", self.atencion)
        print("Respuesta:", self.respuesta)

        if self.estado == "Devuelto a Mesa de Partes":
            print("Motivo de devolución:", self.motivo_devolucion)
