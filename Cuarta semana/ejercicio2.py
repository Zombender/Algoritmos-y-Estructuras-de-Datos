'''
2. Escribir una clase en python con 2 métodos: 
get_string y print_string. get_string acepta una 
cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.
'''

class String_test():
    def __init__(self):
        self.cadena = None
    def get_string(self):
        self.cadena = str(input('Digite una cadena: '))
    def print_string(self):
        print(f'Resultado de la cadena en Mayusculas: {self.cadena.upper()}')

t1 = String_test()
t1.get_string()
t1.print_string()