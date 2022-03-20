import aaProductos

class ProveedorDatosPrincipales:
    def __init__(self, run, nombre):
        self.run=run
        self.nombre=nombre

    def imprimir(self):
        print('\nimprime de datos principales ', self.run, self.nombre, '\n')

class ProveedorDatosOrigen:
    def __init__(self, origen):
        self.origen=origen
        
    def imprimir(self):
        print('\nimprime de datos origen ', self.origen, '\n')

class Proveedor(ProveedorDatosOrigen, ProveedorDatosPrincipales ):
    def __init__(self, run, nombre, origen, telefono=None):
        ProveedorDatosPrincipales.__init__(self,run,nombre)
        ProveedorDatosOrigen.__init__(self,origen)
        self.telefono=telefono
        
    def imprimir_datos_proveedor(self):     #imprime datos proveedor c/s telefono ### ejercicio sobreescritura###
        print('\nDatos de Proveedor:')
        if proveedor1.telefono is not None:
            print('\nRUN\t\t\tNOMBRE\t\t\t\tORIGEN\t\tTELEFONO\n')
            print(proveedor1.run,'\t',proveedor1.nombre,'\t\t',proveedor1.origen,'\t\t',proveedor1.telefono)
        elif proveedor1.telefono is None:
            print('\nRUN\t\t\tNOMBRE\t\t\t\tORIGEN\n')
            print(proveedor1.run,'\t',proveedor1.nombre,'\t\t',proveedor1.origen)
            
    def modificar_nombre_proveedor(self):           #modifica nombre proveedor
        print('\n\n---Modificar nombre proveedor---')
        nuevo_nombre=input('\ningresar nuevo nombre de proveedor: ')
        proveedor1.nombre=nuevo_nombre
        print('el nombre del proveedor ha sido cambiado')
        print('\nRUN\t\t\tNOMBRE\t\t\t\tORIGEN\t\tTELEFONO\n')
        print(proveedor1.run,'\t',proveedor1.nombre,'\t\t',proveedor1.origen,'\t\t',proveedor1.telefono)
        
    
proveedor1=Proveedor('77.666.555-6','\tmimbres_consuelo','chile','+56-9-11155577')     #instanciacion   
#proveedor1.imprimir_datos_proveedor()
