
from infija import infija_postfija

def decorator_validate(function):
    def wrap(*args, **kwargs):
        while True:
            try:
                result = function(*args, **kwargs)
            except ValueError:
                print('Valor invalido. Volver a intentarlo')
                continue
            return result
    return wrap

@decorator_validate
def validar_entero(message : str):
    numero = int(input(message))
    return numero


def menu():
    print('''
    Menu para expresiones
    1. Infija a postfija
    2. Infija a prefija
    3. Salir
    ''')

    op = validar_entero('Digite una opcion valida: ')
    match op:
        case 1:
            expresion = str(input('Digite la expresion infija: ')).strip().upper()
            resultado = infija_postfija(expresion)
            print(f'El resultado de esta expresion infija a postfija es: {resultado}')
        case 2:
            pass
        case 3:
            exit("Saliendo del sistema")
        case _:
            print('Valor invalido. Volver a intentar')

while True: 
    menu()