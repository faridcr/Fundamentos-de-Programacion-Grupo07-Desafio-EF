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
    # Formato dd/mm/aaaa y que sea una fecha real (rechaza 31/02/2020, 15/13/2018, etc.)
    if re.fullmatch(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", texto) is None:
        return False

    try:
        datetime.strptime(texto, "%d/%m/%Y")
        return True

    except ValueError:
        return False