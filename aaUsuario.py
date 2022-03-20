from aaPersona import Persona

class Usuario(Persona):
    def __init__ (self, run, nombre, apellido,correo):
        Persona.__init__(self,run,nombre, apellido)
        self.correo=correo        

    def imprimir_datos_usuario_inicio(self):       #imprime datos clientes c/s genero
            print('\n\n---Imprimir datos (run, nombre, apellido, correo)---')
            print('\nSus datos actualizados son')
            print('\nRUN\tNOMBRE\t\tAPELLIDO\tCORREO\n')
            print(self.run,'\t',self.nombre,'\t\t',self.apellido,'\t\t',self.correo)        

