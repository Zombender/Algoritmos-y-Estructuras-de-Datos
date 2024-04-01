'''
. Que pida por pantalla un número del 1 al 10 y mediante una función muestre por pantalla el número escrito en letras.
'''

def mostrar_numero_en_letras(n):
    match n:
        case 1:
            return 'Uno'
        case 2:
            return 'Dos'
        case 3:
            return 'Tres'
        case 4:
            return 'Cuatro'
        case 5:
            return 'Cinco'
        case 6:
            return 'Seis'
        case 7:
            return 'Siete'
        case 8:
            return 'Ocho'
        case 9:
            return 'Nueve'
        case 10:
            return 'Diez'

def comprobar_numero(n):
    return True if 0 < n <=10 else False
n = int(input('Digite un numero entre 1 y 10: '))

if not comprobar_numero(n):
    exit('El numero digitado no se encuentra en el valor establecido.')

print(f'El resultado en letras del numero {n} es: {mostrar_numero_en_letras(n)}')