'''
Que pida por pantalla una temperatura en grados Celsius,
 muestre un menú para convertirlos a Fahrenheit o Kelvin y
   muestre el equivalente por pantalla, utilizar funciones.

Celsius a Fahrenheit(grados centígrados × 9/5) +32
Celsius a Kelvin(K = ºC + 273.15.)
'''
from os import system
def celsius_fahrenheit(temperatura):
    return (temperatura * 9/5)+32

def celsius_kelvin(temperatura):
    return temperatura + 273.15

def menu():
    
    print('Ahora, seleccione una opcion valida.')
    print('1. Celsius a Fahrenheit')
    print('2. Celsius a Kelvin')
    print('3. Salir')
    op = int(input("Digite un valor: "))
    match op:
        case 1:
            temperatura = float(input('Digite una temperatura en grados Celsius: '))
            print(f'El resultado de convertir Celsius a Fahrenheit es: {celsius_fahrenheit(temperatura)}')
        case 2:
            temperatura = float(input('Digite una temperatura en grados Celsius: '))
            print(f'El resultado de convertir Celsius a Kelvin es: {celsius_kelvin(temperatura)}')
        case 3:
            exit('Saliendo del programa')
        case _:
            exit('Valor invalido. Terminando ejecucion')
    input('Presione ENTER para continuar')
    system('cls')

while True:
    menu()

