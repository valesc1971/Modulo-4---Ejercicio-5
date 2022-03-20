from aaUsuario import Usuario

class Vendedor(Usuario):                #### herencia de clases
    def __init__ (self, run, nombre, apellido,correo, seccion, comision, edad=None):
        self.seccion=seccion
        self.comision_perc=2
        self.__comision=comision
        self.edad=edad
        Usuario.__init__(self, run, nombre, apellido,correo)
        
    def retornar_comision(self):        #extrae comision q esta encriptado
            return self.__comision
    
    def modificar_comision(self, nueva_comision):       #asigna un nuevo valor a comision (agrega la nueva comision a la antigua)
        self.__comision=self.__comision + nueva_comision

        
    def imprimir_vendedor(self):        #imprime datos vendedor  --- sobreescritura metodos
        if vendedor1.edad is not None:
            print('\nnombre vendedor: ', vendedor1.nombre, vendedor1.apellido)
            print('\nseccion: ', vendedor1.seccion)
            print('\nedad: ', vendedor1.edad)
        elif vendedor1 is None:
            print('\nnombre vendedor: ', vendedor1.nombre, vendedor1.apellido)
            print('\nseccion: ', vendedor1.seccion)

    def imprimir_inicio(self):      #imprime venedor elegido
        print('\nVENDEDOR:')
        print(self.nombre, self.apellido)
        
    def imprimir_comision_actualizada(self):           ### nuevo metodo ###
        print('\ntiene acumulada una comision de',format(vendedor1.retornar_comision(), '6,d'))

# instancia vendedores en base a una lista       
staff=[['a_001', 'caro', 'lara', 'caro@mail.com','accesorios', 100, 40], ['b_002', 'oli', 'castro', 'oli@mail.com','dulces', 50, 15]]
print('\n----- VENDEDORES -----\n')
for i in range (0,len(staff)):
    vendedor1=Vendedor(staff[i][0], staff[i][1],staff[i][2],staff[i][3],staff[i][4],staff[i][5],staff[i][6])  
    print([i+1], staff[i][1], staff[i][2])
vend_elegido=int(input('\ningrese vendedor elegido '))
vendedor1=Vendedor(staff[vend_elegido-1][0], staff[vend_elegido-1][1],staff[vend_elegido-1][2],staff[vend_elegido-1][3],staff[vend_elegido-1][4],staff[vend_elegido-1][5],staff[vend_elegido-1][6])  
