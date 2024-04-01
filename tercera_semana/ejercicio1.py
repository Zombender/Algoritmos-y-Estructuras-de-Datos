'''
. Desarrollar un programa con las siguientes opciones:
a)   Introducir un valor entero impar comprendido entre 1 y 19

b)   Calcular la serie numérica 1 + 3 + 5 + ··· + n

c)   Calcular 1 * 3 * 5 * ··· * n

d)   Salir del programa.

Nota: los cálculos se han de realizar a través de un array(lista) que almacene los valores impares comprendidos entre 1y n, usando bucles y acumuladores para recorrer el vector y obtener resultados.

'''

def comprobar_impar(n):
    return True if (n % 2 == 0 and not(0 < n <= 19)) else False

def calcular_suma_impar(n):
    start = 1
    suma = 0
    while start < n:
        suma += start
        start +=2
    return suma
def calcular_multiplicacion_impar(n):
    start = 1
    mult = 1
    while start < n:
        mult *= start
        start +=2
    return mult

n = int(input('Digite un numero entero impar comprendido entre 1 y 19: '))

if comprobar_impar(n):
    exit('El numero digitado no es impar o es mayor a 19')

print(f'La serie numerica de numeros impares hasta {n} en suma es igual a: {calcular_suma_impar(n)}')
print(f'La serie numerica de numeros impares hasta {n} en multiplicacion es igual a: {calcular_multiplicacion_impar(n)}')
