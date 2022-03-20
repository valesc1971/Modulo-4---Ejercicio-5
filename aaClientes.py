from datetime import date

from aaUsuario import Usuario

class Clientes(Usuario):
    def __init__ (self, run, nombre, apellido,correo, direccion, saldo, genero=None):
        self.direccion=direccion
        self.__saldo=saldo
        self.genero=genero
        Usuario.__init__(self, run, nombre, apellido,correo)
        
    def retornar_saldo(self):           #extrae atributo saldo q esta encriptado
                return self.__saldo
    
    def modificar_saldo_agregar(self, nuevo_saldo):  #asigna un valor para el atributo encriptado (agrega saldo)
        self.__saldo=self.__saldo + nuevo_saldo 
    
    def modificar_saldo_restar(self, nuevo_saldo):  #asigna un valor para el atributo encriptado (resta saldo)
        self.__saldo=self.__saldo - nuevo_saldo 

    def impresion_modificar_saldo(self):#saludo a cliente            #impresion de saludo para cliente instanciado
        print('\nBuenos dias ', cliente1.nombre, cliente1.apellido)
        print('Su saldo es: ', format(cliente1.retornar_saldo(),"6,d"))
        nuevo_saldo=int(input('\nIngrese cantidad para agregar a saldo: '))
        cliente1.modificar_saldo_agregar=cliente1.modificar_saldo_agregar(nuevo_saldo)
        print('\nSu nuevo saldo es: ', format(cliente1.retornar_saldo(),"6,d") )

    def modificar_direccion(self):      #modifica direccion cliente
        print('\nBuenos dias ', cliente1.nombre, cliente1.apellido)
        print('Su direccion es: ', cliente1.direccion)
        nueva_direccion=input('\ningresar nueva direccion: ')
        cliente1.direccion=nueva_direccion
        print('\nSu nueva direccion es: ', cliente1.direccion)
        
    def imprimir_datos_cliente(self):       #imprime datos clientes c/s genero
        print('\nLos datos del cliente son: ')
        if cliente1.genero is None:
            print('\nUSUARIO\tNOMBRE\tAPELLIDO\tCORREO\t\t\tDIRECCION \t\t\tSALDO\n')
            print(cliente1.run,'\t',cliente1.nombre,'\t',cliente1.apellido,'\t',cliente1.correo,'\t',cliente1.direccion,'\t\t\t',format(cliente1.retornar_saldo(),"6,d"))
        elif cliente1.genero is not None:
            print('\nUSUARIO\tNOMBRE\t\tAPELLIDO\tCORREO\t\tDIRECCION \tSALDO\tGENERO\n')
            print(cliente1.run,'\t',cliente1.nombre,'\t\t',cliente1.apellido,'\t\t',cliente1.correo,'\t\t',cliente1.direccion,'\t\t',format(cliente1.retornar_saldo(),"6,d"),'\t\t', cliente1.genero)

    def imprimir_inicio(self):   #imprime cliente elegido
        print('\nCLIENTE:')
        print(self.nombre, self.apellido)
        
# instancia clientes en base a una lista        
print('\nBuenos dias , hoy es ,', date.today())
customers=[["0001","vale","sanchez","vale@hotmail.com",'stgo',100000], ["0002","elena","castro","ele@hotmail.com",'olmue',100000]]
print('\n----- CLIENTES -----\n')
for i in range (0,len(customers)):
    cliente1=Clientes(customers[i][0], customers[i][1],customers[i][2],customers[i][3],customers[i][4],customers[i][5])  
    print([i+1], customers[i][1], customers[i][2])
customer_elegido=int(input('\ningrese cliente elegido '))
cliente1=Clientes(customers[customer_elegido-1][0], customers[customer_elegido-1][1],customers[customer_elegido-1][2],customers[customer_elegido-1][3],customers[customer_elegido-1][4],customers[customer_elegido-1][5])  