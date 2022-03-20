class Productos:
    def __init__(self, sku,nombre,categoria,proveedor,stock, valor_neto, origen=None):   #define init clase productos
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto=1.19
        self.origen=origen
        
    def retornar_iva(self):
        iva_impuesto=producto1.__impuesto       #extrae vaalor impuesto q esta encriptado
        return iva_impuesto
        
    def imprimir_producto(self):    #impresion producto 
        if producto1.origen is not None:
            print('\nProducto elegido:\t', producto1.nombre) 
            print('Categoria:\t\t', producto1. categoria)
            print('Proveedor:\t\t',producto1.proveedor)        #composicion de producto/proveedor en instanciamiento
            print('Stock actual es:\t',producto1.stock)
            print('Valor neto por unidad:\t$', producto1.valor_neto)
            print('Origen del producto es:\t', producto1.origen)
        elif producto1.origen is None:
            print('\nProducto elegido:\t', producto1.nombre) 
            print('Categoria:\t\t', producto1. categoria)
            print('Proveedor:\t\t',producto1.proveedor)        #composicion de producto/proveedor en instanciamiento
            print('Stock actual es:\t',producto1.stock)
            print('Valor neto por unidad:\t$', producto1.valor_neto)

    def imprime_stock_producto(self):
        print('\nEl stock actualizado es: ', producto1.stock)  

    def agregar_stock(self):            #agrega stock    
        stock_agregar=int(input('\ningresar stock a agregar: '))
        producto1.stock=producto1.stock+stock_agregar
        print('\nEl stock actualizado es: ', producto1.stock)  
        return producto1.stock
    
    def modifica_valor_neto_prod(self, per_subir=None):     #cambia valor neto al producto  / nuevo metodo sobreescritura metodos
        print('\nel valor unitario neto del producto es $ ', format(producto1.valor_neto, '6,d'))
        if per_subir is None:
            nuevo_precio=int(input('Ingrese nuevo precio '))
            producto1.valor_neto=int(nuevo_precio)
            print('El valor del producto ha sido actualizado a $ ', format(producto1.valor_neto, '6,d'))
        elif per_subir is not None:
            porc_subir=int(input('Ingrese procentaje a subir precio '))
            producto1.valor_neto=int(producto1.valor_neto*(1+(porc_subir/100)))
            print('El valor del producto ha sido actualizado a $ ', format(producto1.valor_neto, '6,d'))    
    
    def imprimir_inicio(self):   #imprime producto elegido
        print('\nPRODUCTO')
        print(self.nombre)

# instancia productos en base a una lista
catalogo=[["001","canasto_1","canastos","mimbres_consuelo",50,1500 ], ["001","sillon_1","muebles","mimbres_consuelo",3,23000 ]]
print('\n----- PRODUCTOS -----\n')
for i in range (0,len(catalogo)):
    producto1=Productos(catalogo[i][0], catalogo[i][1],catalogo[i][2],catalogo[i][3],catalogo[i][4],catalogo[i][5])  
    print([i+1], catalogo[i][1], catalogo[i][2])
prod_elegido=int(input('\ningrese producto elegido '))
producto1=Productos(catalogo[prod_elegido-1][0], catalogo[prod_elegido-1][1],catalogo[prod_elegido-1][2],catalogo[prod_elegido-1][3],catalogo[prod_elegido-1][4],catalogo[prod_elegido-1][5])  
