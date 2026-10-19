from trabajador import Trabajador
from subgerencia import Subgerencia

# LISTAS PRINCIPALES
ciudadanos = []
expedientes = []
trabajadores = []
subgerencias = []


# GERENCIAS
gerencias = [
    "Gestión Ambiental",
    "Seguridad Ciudadana y Vial",
    "Desarrollo Urbano"
]


# SUBGERENCIAS
limpieza = Subgerencia("Limpieza Pública", "Gestión Ambiental")
parques = Subgerencia("Parques y Jardines", "Gestión Ambiental")

subgerencias.append(limpieza)
subgerencias.append(parques)


# TRABAJADORES DE PRUEBA
trabajador1 = Trabajador(
    "12345678", "Carlos", "Perez", "carlos@gmail.com",
    "mesa", "mesa123", "Mesa de Partes"
)

trabajador2 = Trabajador(
    "87654321", "Pedro", "Lopez", "pedro@gmail.com",
    "g1", "demo123", "Gestión Ambiental"
)

trabajador3 = Trabajador(
    "11223344", "Luis", "Ramirez", "luis@gmail.com",
    "s1", "demo123", "Limpieza Pública"
)

trabajador4 = Trabajador(
    "44556677", "Miguel", "Torres", "miguel@gmail.com",
    "g2", "demo123", "Seguridad Ciudadana y Vial"
)

# NUEVO TRABAJADOR DE DESARROLLO URBANO
trabajador5 = Trabajador(
    "55667788", "Ana", "Gomez", "ana@gmail.com",
    "g3", "demo123", "Desarrollo Urbano"
)

trabajadores.append(trabajador1)
trabajadores.append(trabajador2)
trabajadores.append(trabajador3)
trabajadores.append(trabajador4)
trabajadores.append(trabajador5)
