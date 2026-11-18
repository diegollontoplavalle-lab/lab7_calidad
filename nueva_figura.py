"""Nueva figura agregada SIN modificar areas_solid.py (principio Open/Closed)."""
from areas_solid import Circulo, Figura, ImpresoraDeAreas, Rectangulo


class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def nombre(self):
        return "trapecio"

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2


if __name__ == "__main__":
    impresora = ImpresoraDeAreas()
    for figura in [Circulo(5), Rectangulo(4, 6), Trapecio(6, 4, 3)]:
        impresora.mostrar(figura)