"""Áreas de figuras con principios SOLID: cada clase tiene una responsabilidad y se puede extender sin modificar."""
from abc import ABC, abstractmethod

PI = 3.14159


class Figura(ABC):
    """Abstracción común: toda figura sabe su nombre y calcular su propia área."""

    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def nombre(self):
        return "circulo"

    def area(self):
        return PI * self.radio * self.radio


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def nombre(self):
        return "rectangulo"

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def nombre(self):
        return "triangulo"

    def area(self):
        return self.base * self.altura / 2


class ImpresoraDeAreas:
    """Única responsabilidad: mostrar el resultado. Funciona con cualquier Figura (Open/Closed)."""

    def mostrar(self, figura):
        print(f"El area del {figura.nombre()} es {figura.area()}")


if __name__ == "__main__":
    impresora = ImpresoraDeAreas()
    for figura in [Circulo(5), Rectangulo(4, 6), Triangulo(3, 8)]:
        impresora.mostrar(figura)