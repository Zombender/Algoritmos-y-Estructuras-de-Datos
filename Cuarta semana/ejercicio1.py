'''
1. Escribir una clase en python llamada circulo que contenga un radio, 
con un método que devuelva el área y otro que devuelva el perímetro del circulo.
'''
from math import pi
class Circulo():
    def __init__(self, radio):
        self.radio = radio
    def get_radio(self):
        return self.radio
    def area(self):
        return pi * pow(self.radio,2)
    def perimetro(self):
        return pi * (self.radio*2)

c1 = Circulo(10)
print(f'El area del circulo con radio {c1.get_radio()} es: {round(c1.area(),2)}')
print(f'El perimetro del circulo con radio {c1.get_radio()} es: {round(c1.perimetro(),2)}')