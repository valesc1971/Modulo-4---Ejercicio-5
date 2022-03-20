from datetime import date
import random
from random import randint
import aaProveedores
import aaClientes
import aaVendedores
import aaProductos

class Transaccion:          #clase traansaccion donde ocurre la operacion de la orden de compra
    def __init__(self, numero_orden, fecha):
        self.numer_orden=numero_orden
        self.fecha=fecha
        self.producto_venta=aaProductos.producto1.nombre
        self.proveedor = aaProveedores.proveedor1.nombre
        self.stock = aaProductos.producto1.stock
        self.valor_neto = aaProductos.producto1.valor_neto
        self.__impuesto=aaProductos.producto1.retornar_iva()
        self.comision_perc=2
        self.__comision = aaVendedores.vendedor1.retornar_comision()
        
    def vender_producto(self, cliente_inst, producto_inst, vendedor_inst, proveedor_inst):  #instanciamiento de clase con atributos de otras clases
                uni_venta=int(input ('ingrese unidades a vender: '))        #solicita unidades de venta
                if uni_venta>producto_inst.stock:               #verificacion de unidades en stock suficientes para efectual la venta
                    print('\nno hay stock suficiente en inventario para esta venta')
                else:
                    venta_pesos=producto_inst.valor_neto*uni_venta      
                    valor_final=int(venta_pesos*aaProductos.producto1.retornar_iva())
                    if valor_final>cliente_inst.retornar_saldo():  #verificacion de saldo suficientes para efectual la venta
                        print('\nUsted no tiene saldo suficiente para efectuar esta compra')
                    else:    
                        iva_total=int(valor_final-venta_pesos)      #calculo de venta final
                        print('\nUnidades vendidas:   ',uni_venta)
                        print('--------------------------------------------')
                        print('La venta total es $', venta_pesos)
                        print('\nvalor neto:\t', venta_pesos)
                        print('IVA:\t\t', iva_total)
                        print('      \t\t---------')
                        print('valor final:\t',int(valor_final),'\n')
                        print('--------------------------------------------')
                        print('\nEl stock inicial es ', producto_inst.stock)    # calculo para descontar stock
                        print('Se vendieron ' ,uni_venta)
                        producto_inst.stock=producto_inst.stock-uni_venta
                        print('Stock despues de la venta: ',producto_inst.stock,'\n')
                        print('--------------------------------------------')           
                        print('\nLa comision inicial es ', vendedor_inst.retornar_comision())
                        comision_pesos_calculada=int(venta_pesos*self.comision_perc/100)   #calculo comision en base a % data en init
                        vendedor_inst.modificar_comision(comision_pesos_calculada)
                        print('La comision obtenida por la venta es ', comision_pesos_calculada)
                        print('La comision acumulada es ', vendedor_inst.retornar_comision())
                        print('--------------------------------------------')
                        print('\nEl saldo inicial es: ',cliente_inst.retornar_saldo())      #descuenta venta a saldo inicial
                        print('El gasto en su compra: ',valor_final)
                        cliente_inst.modificar_saldo_restar(valor_final)
                        print('El nuevo saldo es ', cliente_inst.retornar_saldo())
                        print('--------------------------------------------')
                        print('\nel resumen de su compra es: \n')        #aentrega resumen de venta con nuemro de orden
                        print('#orden:\t',venta.numer_orden)
                        print('fecha:\t',self.fecha)
                        print('producto:\t',producto_inst.nombre)
                        print('proveedor:\t',proveedor_inst.nombre)
                        print('unidades:\t',uni_venta)
                        print('valor venta (incluye IVA):\t', valor_final)
                        acumula_venta.append([producto_inst.nombre, uni_venta, venta.numer_orden,int(venta_pesos)])     # agrega transccion a lista para almacenar las disitnas transacciones
                        print('Hasta el momento sus ventas son:', acumula_venta)
                        return acumula_venta
    
    def muestra_venta_acumulada(self):      ###  nuevo metodo ###  imprime venta acumulada 1 cliente, 1 vendedor y 1 producto
        print('su venta acumulada es: ')
        #print(acumula_venta)
        for i in range(len(acumula_venta)):
            print(acumula_venta[i])


acumula_venta=[]
x=random.randint(1000,9999)
venta=Transaccion(x, date.today(), )


