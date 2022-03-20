import aaClientes       ##llama a los archivos donde estan contenidas cada una delas clases
import aaVendedores
import aaProductos
import aaTransaccion
import aaProveedores
from aaTransaccion import *

aaClientes          ## elige cliente 
aaVendedores        ## elige vendedor 


print('\nHa elegido:')
aaClientes.cliente1.imprimir_inicio()
aaVendedores.vendedor1.imprimir_inicio()

aaProductos     ## elige producto
aaProductos.producto1.imprimir_inicio()
aaProveedores

resp_ingreso_tienda=True        ## menu principal de ingreso a tienda - 
while resp_ingreso_tienda: 
    ingreso_tienda=input('\npresione 1 para continuar / presione 2 para salir ')
    if ingreso_tienda=='1':
        solicita_menu=True         ## ingreso al menu
        while solicita_menu: 
            print('\n\n***** MENU *****\n')
            print('1    imprimir datos cliente')
            print('2    agregar saldo a cliente')
            print('3    imprimir producto')
            print('4    revisar stock producto')
            print('5    agregar stock')
            print('6    modificar valor neto producto')
            print('7    imprimir datos vendedor')
            print('8    modificar nombre proveedor') 
            print('9    transaccion VENTA')
            print('10   imprime resumen venta')
            print('11    SALIR')  
            print('\n***************')
            respuesta_menu_principal=input('ingrese su opcion ')
            if respuesta_menu_principal=='1':
                aaClientes.cliente1.imprimir_datos_cliente()
            elif respuesta_menu_principal=='2':
                aaClientes.cliente1.imprime_saludo()
                aaClientes.cliente1.impresion_modificar_saldo()
            elif respuesta_menu_principal=='3':
                aaProductos.producto1.imprimir_producto()
            elif respuesta_menu_principal=='4':
                aaProductos.producto1.imprime_stock_producto()
            elif respuesta_menu_principal=='5':
                aaProductos.producto1.agregar_stock()
            elif respuesta_menu_principal=='6':    
                aaProductos.producto1.modifica_valor_neto_prod('')
            elif respuesta_menu_principal=='7':
                aaVendedores.vendedor1.imprimir_vendedor()
                aaVendedores.vendedor1.imprimir_comision_actualizada()
            elif respuesta_menu_principal=='8':
                aaProveedores.proveedor1.imprimir_datos_proveedor()
                aaProveedores.proveedor1.modificar_nombre_proveedor()
            elif respuesta_menu_principal=='9':
                aaTransaccion.venta.vender_producto(aaClientes.cliente1, aaProductos.producto1, aaVendedores.vendedor1, aaProveedores.proveedor1)#instanciacion
            elif respuesta_menu_principal=='10':
                aaTransaccion.venta.muestra_venta_acumulada()
            elif respuesta_menu_principal=='11':
                solicita_menu=False
    elif ingreso_tienda=='2':
        resp_ingreso_tienda=False       ## sale del menu


#print(acumula_venta)
#for i in range(len(acumula_venta)):
    #print(acumula_venta[i])
