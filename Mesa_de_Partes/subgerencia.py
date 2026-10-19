
class Subgerencia:
    def __init__(self, nombre, gerencia):
        self.nombre = nombre
        self.gerencia = gerencia

    def mostrar_datos(self):
        print("\n=== DATOS DE LA SUBGERENCIA ===")
        print("Nombre:", self.nombre)
        print("Gerencia:", self.gerencia)
