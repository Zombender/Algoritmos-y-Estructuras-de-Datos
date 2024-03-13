'''
Leer dos números e intercambiar sus valores.

'''

n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))

aux = n1
n1 = n2
n2 = aux

print(f'Valor del primer numero: {n1}')
print(f'Valor del segundo numero: {n2}')