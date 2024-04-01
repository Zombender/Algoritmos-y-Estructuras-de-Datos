'''
3. Que muestre un menú con las opciones sumar, restar, multiplicar y dividir, el programa solicitará una opción y realizará la tarea elegida,
 se debe usar una función para mostrar el menú, pedir los datos en el main (programa principal) y después usar funciones para realizar los cálculos.
'''

from os import system

def pedir_datos():
    n1 = int(input('Digite el primer numero: '))
    n2 = int(input('Digite el segundo numero: '))
    return n1,n2
def suma():
    n1, n2 = pedir_datos()
    return n1+n2
def resta():
    n1, n2 = pedir_datos()
    return n1-n2
def multiplicacion():
    n1, n2 = pedir_datos()
    return n1*n2
def division():
    n1, n2 = pedir_datos()
    if n2 == 0:
        raise ZeroDivisionError("No se puede dividir un numero entre cero")
    return n1/n2

def menu():
    print('Menu para ejercicio tres')
    print('1. Sumar dos numeros')
    print('2. Restar dos numeros')
    print('3. Multiplicar dos numeros')
    print('4. Dividir dos numeros')
    print('5. Salir')
    op = int(input('Digite una opcion valida: '))
    match op:
        case 1:
            valor = suma()
            print(f'El resultado de la suma con la operacion seleccionada es: {valor}')
        case 2:
            valor = resta()
            print(f'El resultado de la resta con la operacion seleccionada es: {valor}')
        case 3:
            valor = multiplicacion()
            print(f'El resultado de la multiplicacion con la operacion seleccionada es: {valor}')
        case 4:
            valor = division()
            print(f'El resultado de la division con la operacion seleccionada es: {valor}')
        case 5:
            exit("Saliendo del programa")
        case _:
            print('Valor invalido. Volver a intentar')
    input('Presione enter para continuar')
    system('cls')

while True:
    menu()