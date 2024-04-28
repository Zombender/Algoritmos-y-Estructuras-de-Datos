from re import findall

class Pila:
    def __init__(self):
        self.top = None
    
    def apilar(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.top is None:
            self.top = nuevo_nodo
            return
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo
    
    def desapilar(self):
        if self.top is None:
            return None
        valor = self.top.dato
        self.top = self.top.siguiente
        return valor
    
    def cambio(self):
        aux = self.top.siguiente
        self.top.siguiente = self.top
        self.top = aux
        return self.desapilar()
        
    def imprimir(self):
        actual = self.top
        while actual:
            print(actual.dato)
            actual = actual.siguiente


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Reglas
'''
Operador con misma importancia que el de precedencia = cambio
Operador con mayor importancia que el de precedencia = se agrega a pila
Operador con menor importancia que el de precedencia = sacar elementos de pila
Parentesis derecho = Vaciar pila hasta otro parentesis
'''

operandos = {
    '^': 3,
    '√': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    ')': 0
}

letras = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def infija_postfija(expresion : str):
    global letras
    global operandos
    resultado = ""
    pila = Pila()
    for caracter in expresion:
        
        if caracter.isdigit() or caracter in letras:
           resultado +=caracter
           continue
        elif pila.top == None or caracter == '(':
            pila.apilar(caracter)
            continue
        elif caracter == ')':
            while True:
                valor = pila.desapilar()
                if valor == '(':
                    break
                resultado +=valor
            continue

        preferencia = operandos.get(caracter)
        preferencia_pila = operandos.get(pila.top.dato)

        if preferencia > preferencia_pila:
            pila.apilar(caracter)
            continue
        elif preferencia < preferencia_pila:
            resultado += pila.cambio()
            continue
        while True:
            valor = pila.desapilar()
            if valor is None:
                break
            resultado +=valor
        print(f'Elemento evaluado: {caracter}')
    while True:
        valor = pila.desapilar()
        if valor is None:
            break
        resultado +=valor
    return resultado

               
               
        