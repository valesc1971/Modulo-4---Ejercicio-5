from datetime import date

class Persona:
    def __init__(self, run, nombre, apellido ):
        self.run=run
        self.nombre=nombre
        self.apellido=apellido
        
    def imprime_saludo(self):
        print('hola, bienvenido ', self.nombre, 'hoy es ', date.today())