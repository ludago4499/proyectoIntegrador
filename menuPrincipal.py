import time
import config
import manejar_inventario
import manejar_vendedores
import datos_de_ventas
import menu_ventas
import reportes_ventas

def desplegar_menu_principal() -> None:
# Luis González
# Se despliega el menú principal
    config.guiones()
    print("Bienvenido al sistema de Manejo de Dairy Queen. ")
    print("Seleccione la opción del siguiente menú: ")
    print("O ingrese 'salir' para salir")
    config.guiones()
    print("[1] Registrar una venta")
    print("[2] Registrar llegado de artículos al almacén")
    print("[3] Consultar datos del inventario")
    print ("[4] Consultar datos de las ventas")
    print("[5] Mostrar reportes de ventas por vendedor o por artículo")
    print ("[6] Modificar a los vendedores")
    config.guiones()

def registrar_una_venta () -> None:
    '''Submenu para registrar una venta en el sistema y actualizar los archivos necesarios'''
    [nombre_vendedor, id_vendedor] = menu_ventas.preguntar_vendedor()
    if (id_vendedor == -2):
        return -1


    #obtener fecha
    flag = True
    while flag:
        flag = False
        print("Ingrese la fecha en donde se realizó la venta, que siga el formato (dd/mm/yyyy) Ejemplo 04/12/2005")
        print("O ingrese 'salir' para salir")
        fecha = input("Selección: ")
        valor = menu_ventas.checar_fecha_completa(fecha)
        if (valor == -2):
            print("Saliendo...")
            time.sleep(1)
            return -1
        if (not valor):
            flag = True
        
    flag = True
    while flag:
        flag = False
        menu_ventas.print_menu(nombre_vendedor)
        seleccion = input("Selección: ") # se obtiene la seleccion de productos
        config.actualizar_iva()
        seleccion = config.checar_seleccion(seleccion)
        if (seleccion == -2): # opción salir
            return -1
        elif (seleccion == -1): # error
            flag = True
        else:
             valor = menu_ventas.seleccion_registrar_venta(seleccion,fecha,id_vendedor)
             if (valor == -1):
                 flag = True
    return -1

def registrar_articulos() -> None:
    '''Registra articulos en el inventario'''
    config.guiones()
    valor = manejar_inventario.llegada_articulos()
    if (valor ==-1):
        return -1
    
def consultar_datos_inventario() -> None:
    print("Se imprimirá todo el menú del archivo")
    valor = datos_de_ventas.checar_continuar()
    if (not valor == -1 and not valor ==2):
        manejar_inventario.print_todo_inventario()
    return -1

def consultar_datos_ventas() -> None:
    '''Consulta datos de una venta ''' 
    # follow up
    config.guiones()
    datos_de_ventas.menu_datos_ventas()
    seleccion = input("Selección: ")
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2): # opción salir
        return -1
    if (seleccion == -1): # error
        return consultar_datos_ventas()
    valor = datos_de_ventas.seleccion_datos_ventas(seleccion)

    if (valor == -1):
        return consultar_datos_ventas()

def mostrar_reportes() -> None:
    reportes_ventas.print_submenu()
    seleccion = input("Seleccion: ")
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (not seleccion == -1):
        seleccion = reportes_ventas.seleccion_ventas(seleccion)
    if (seleccion == -1):
        return mostrar_reportes()


def modificar_vendedores():
    '''Modifica los datos de un vendedor'''
    manejar_vendedores.menu_vendedor()
    seleccion = input("Selección: ")
    seleccion = config.checar_seleccion(seleccion)

    if (seleccion == -2): # opción salir
        return -1
    if (seleccion == -1): # error
        return modificar_vendedores()
    valor = manejar_vendedores.seleccion_menu_vendedores(seleccion)

    if (valor == -1):
        return modificar_vendedores()

def seleccion_menu_principal(seleccion: int):
    ''' # Case-match para abrir el menú correspondiente
    # Se regresa un "-1" si el número no se encuentra en las opciones
    # Luis González'''
 
    match seleccion:
        case 1:
            return registrar_una_venta()
        case 2:
            return registrar_articulos()
        case 3:
            return consultar_datos_inventario()
        case 4:
           return consultar_datos_ventas()
        case 5:
            return mostrar_reportes()
        case 6:
            return modificar_vendedores()        
        case _: 
            print ("Esa opción no está en la lista, intente nuevamente")
            time.sleep(1) # Se espera un segundo
            return -1
            
            
    
