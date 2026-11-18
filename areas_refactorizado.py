"""Cálculo del área de figuras geométricas (versión refactorizada: mismo resultado, código más claro)."""

PI = 3.14159


def area_circulo(radio):
    return PI * radio * radio


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


def mostrar_area(nombre_figura, area):
    print(f"El area del {nombre_figura} es {area}")


def procesar_figura(codigo, medida1, medida2=0):
    """Calcula y muestra el área según el código de la figura: c, r o t."""
    if codigo == "c":
        mostrar_area("circulo", area_circulo(medida1))
    elif codigo == "r":
        mostrar_area("rectangulo", area_rectangulo(medida1, medida2))
    elif codigo == "t":
        mostrar_area("triangulo", area_triangulo(medida1, medida2))
    else:
        print("Figura no valida")


if __name__ == "__main__":
    procesar_figura("c", 5)
    procesar_figura("r", 4, 6)
    procesar_figura("t", 3, 8)
    procesar_figura("x", 1)