'''
Que muestre por pantalla si un número es par o impar, 
utilizar una función. Además, mediante una función imprimir la tabla de multiplicar del número leído.
'''

def impar_o_par(n):
    return True if numero %2 == 0 else False
#
def tabla_multiplicar(n):
    for tab in range(n+1):
        print(f'{n} * {tab} = {n*tab}')
        
numero = int(input("Digite un numero: "))
if impar_o_par(numero):
    print(f"El numero {numero} es par")
else:
    print(f'El numero {numero} es impar')

print(f"Tabla de multiplicar del numero {numero}")
tabla_multiplicar(numero)