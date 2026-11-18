"""Determina si un número entero es primo (etapa 3, REFACTOR: mismo comportamiento, más claro y eficiente)."""


def es_primo(numero):
    """Devuelve True si el número es mayor que 1 y solo es divisible entre 1 y entre sí mismo."""
    if numero < 2:
        return False
    return not tiene_divisor(numero)


def tiene_divisor(numero):
    """Busca un divisor entre 2 y la raíz cuadrada del número."""
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return True
        divisor += 1
    return False