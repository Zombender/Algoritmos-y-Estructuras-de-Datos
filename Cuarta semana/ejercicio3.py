'''
3. Realizar un programa que conste de una clase llamada Estudiante, que tenga como 
atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


'''
APROBADO = 70
def obtener_nota(message):
    while True:
        nota = float(input(message))
        if not(0<=nota<=100):
            print('Valor ingresado no valido. Volver a intentar')
            continue
        return nota
class Estudiante():
    def __init__(self):
        self.nombre = str(input("Digite el nombre del estudiante: "))
        self.nota = obtener_nota('Digite la nota del estudiante: ')
    def show_student(self):
        print(f'El estudiante {self.nombre} tiene la nota de: {self.nota}')
        print(f'Estado: {'Aprobado' if self.nota >=70 else 'Reprobrado'}')

e1 = Estudiante()
e1.show_student()