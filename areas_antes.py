# Versión inicial (antes de refactorizar): funciona, pero tiene nombres poco claros y código repetido.
def f(t, a, b=0):
    r = 0
    if t == "c":
        r = 3.14159 * a * a
        print("El area del circulo es", r)
    elif t == "r":
        r = a * b
        print("El area del rectangulo es", r)
    elif t == "t":
        r = a * b / 2
        print("El area del triangulo es", r)
    else:
        print("Figura no valida")
    return r


f("c", 5)
f("r", 4, 6)
f("t", 3, 8)
f("x", 1)