from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validar_columna_1(valor):
    if not valor.isdigit() or not (3 <= len(valor) <= 10):
        return "Columna 1: debe ser un número de 3 a 10 dígitos"


def validar_columna_2(valor):
    try:
        validate_email(valor)
    except ValidationError:
        return "Columna 2: correo inválido"


def validar_columna_3(valor):
    if valor not in ("CC", "TI"):
        return "Columna 3: debe ser 'CC' o 'TI'"


def validar_columna_4(valor):
    try:
        val = int(valor)
        if not (500000 <= val <= 1500000):
            return "Columna 4: valor fuera de rango (500000 - 1500000)"
    except ValueError:
        return "Columna 4: debe ser número entero"


def validar_fila(fila, numero_fila):
    errores = []

    if len(fila) != 5:
        errores.append(f"Fila {numero_fila}: cantidad incorrecta de columnas ({len(fila)})")
        return errores

    col1, col2, col3, col4, col5 = fila

    # Ejecutar cada validador de forma ordenada
    validadores = [
        validar_columna_1(col1),
        validar_columna_2(col2),
        validar_columna_3(col3),
        validar_columna_4(col4),
    ]

    for error in validadores:
        if error:
            errores.append(f"Fila {numero_fila}, {error}")

    return errores
