from datetime import datetime

FORMATO = "%d/%m/%Y %H:%M:%S"


def ahora():
    return datetime.now().strftime(FORMATO)


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
        self.fecha_registro = ahora()
        self.fecha_cierre = "Pendiente"

    def tiempo_total(self):
        if self.fecha_registro == "Sin fecha":
            return "Sin datos"

        inicio = datetime.strptime(self.fecha_registro, FORMATO)

        if self.fecha_cierre == "Pendiente":
            fin = datetime.now()
        else:
            fin = datetime.strptime(self.fecha_cierre, FORMATO)

        segundos = int((fin - inicio).total_seconds())
        horas, resto = divmod(segundos, 3600)
        minutos, seg = divmod(resto, 60)

        return str(horas) + "h " + str(minutos) + "m " + str(seg) + "s"

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
