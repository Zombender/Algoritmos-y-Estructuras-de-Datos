'''
    Calcular el promedio de tres números enteros leídos.
'''

n1 = int(input('Digite el primer numero: '))
n2 = int(input('Digite el segundo numero: '))
n3 = int(input('Digite el tercer numero: '))

prom = lambda n1,n2,n3 : (n1+n2+n3) / 3

print(f'El promedio de los tres numeros es: {prom(n1,n2,n3)}')