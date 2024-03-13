'''
Calcular el total a pagar por la compra de artículos en una tienda. 
Se sabe que el impuesto que se aplica es el 10%.

'''
from os import system
from time import sleep
dict_product = {
    "Teclado": [200,0],
    "Mouse" : [150,0],
    "Cuadernos": [100,0],
    "Libro" : [117,0],
    "Cargador para celular": [50,0]
}
def chooseQuantity(product):
    cantidad = int(input(f"Digite la cantidad que desea comprar para el producto '{product}': "))
    print("Cantidad agregada en el carrito")
    return cantidad
def showProduct(producto):
    return False if dict_product[producto][1] == 0 else True

def showBill():
    print("Factura --- Tienda de productos")
    print("Nombre --- Precio ---Cantidad")
    if showProduct("Teclado"):
        print(f"Teclado --- {dict_product["Teclado"][0]} --- {dict_product["Teclado"][1]}")
    if showProduct("Mouse"):
        print(f"Mouse --- {dict_product["Mouse"][0]} --- {dict_product["Mouse"][1]}")
    if showProduct("Cuadernos"):
        print(f"Cuadernos --- {dict_product["Cuadernos"][0]} --- {dict_product["Cuadernos"][1]}")
    if showProduct("Libro"):
        print(f"Libro --- {dict_product["Libro"][0]} --- {dict_product["Libro"][1]}")
    if showProduct("Cargador para celular"):
        print(f"Cargador para celular --- {dict_product["Cargador para celular"][0]} --- {dict_product["Cargador para celular"][1]}")
    precio_individual = lambda cantidad, precio: cantidad * precio
    precio_total = 0
    for producto in dict_product.values():
        precio_total += precio_individual(producto[0],producto[1])
    print(f"Total a pagar: C${precio_total + (precio_total *0.10)}")
def menu():

    print("Tienda de productos")
    print("1. Teclado --- C$200")
    print('2. Mouse --- C$150')
    print('3. Cuadernos --- C$100')
    print("4. Libro --- C$117")
    print("5. Cargador para celular --- C$50")
    print("6. Mostrar factura final")
    print("7. Salir")
    op = int(input("Digite una opcion valida: "))
    match op:
        case 1:
            dict_product["Teclado"][1] += chooseQuantity("Teclado")
        case 2:
            dict_product["Mouse"][1] += chooseQuantity("Mouse")
        case 3:
            dict_product["Cuadernos"][1] +=chooseQuantity("Cuadernos")
        case 4:
            dict_product["Libro"][1] +=chooseQuantity("Libro")
        case 5: 
            dict_product["Cargador para celular"][1] += chooseQuantity("Cargador para celular")
        case 6:
            showBill()
            exit("Gracias por usar nuestro servicio")
        case 7:
            exit("Gracais por usar nuestro servicio")
        case _:
            print("Valor invalido. Volver a intentar")
    sleep(1)
    system('cls')
    
while True:
    menu()