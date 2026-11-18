import re

from datetime import datetime, date

LETRAS = "A-Za-zÁÉÍÓÚáéíóúÑñÜü"


def dni_valido(dni):
    return re.fullmatch(r"[0-9]{8}", dni) is not None


def correo_valido(correo):
    patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+"
    return re.fullmatch(patron, correo) is not None


def nombre_valido(texto):
    patron = rf"[{LETRAS}]+([ '\-][{LETRAS}]+)*"
    return re.fullmatch(patron, texto) is not None

def fecha_formato_valido(texto):
    # Formato dd/mm/aaaa (dos dígitos, dos dígitos y cuatro dígitos)
    return re.fullmatch(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", texto) is not None