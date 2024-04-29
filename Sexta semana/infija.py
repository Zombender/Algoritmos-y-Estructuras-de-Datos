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
        primer_nodo = self.top
        segundo_nodo = self.top.siguiente
        self.top = segundo_nodo
        primer_nodo.siguiente = segundo_nodo.siguiente
        self.top.siguiente = primer_nodo
        
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

def validar_expresion(expresion : str):
    operadores = set('*/+-^√')
    for i in range(len(expresion)-1):
        if expresion[i] in operadores and expresion[i+1] in operadores:
            return False
    return True
def infija_postfija(expresion : str):
    if not(validar_expresion(expresion)):
        return False
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
        try:
            if preferencia == None: raise ValueError
        except ValueError:
            print("Valor invalido encontrado en la expresion.")
            return False
        preferencia_pila = operandos.get(pila.top.dato)
        if preferencia > preferencia_pila:
            pila.apilar(caracter)
            continue
        elif preferencia == preferencia_pila:
            pila.apilar(caracter)
            resultado += pila.cambio()
            continue
        elif preferencia < preferencia_pila:
            pila.apilar(caracter)
            while True:
                valor = pila.desapilar()
                if valor is None:
                    break
                resultado +=valor
    while True:
        valor = pila.desapilar()
        if valor is None:
            break
        resultado +=valor
    
    return resultado

               
               
        