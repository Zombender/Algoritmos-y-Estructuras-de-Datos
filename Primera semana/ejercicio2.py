'''
Leer el precio de un producto, calcule el impuesto de valor agregado.

'''

producto = float(input('Digite el precio de un producto: '))

impuesto = lambda producto : producto + (producto*0.15)

print(f'El producto con impuesto de valor agregado es: {impuesto(producto)}')