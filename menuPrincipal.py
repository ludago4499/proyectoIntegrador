import time
import config
import manejar_inventario
import manejar_vendedores

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

def registrar_una_venta () -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")
    print("(2) Ingrese la cantidad vendida")
    seleccion = input("")

def registrar_articulos() -> None:
    # follow up
    config.guiones()
    valor = manejar_inventario.llegada_articulos()
    if (valor ==-1):
        return -1
    

def consultar_datos_inventario() -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")
    seleccion = input("")

def consultar_datos_ventas() -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")
    seleccion = input("")

def mostrar_reportes() -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")
    seleccion = input("")

def modificar_vendedores():
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
    # Case-match para abrir el menú correspondiente
    # Se regresa un "-1" si el número no se encuentra en las opciones
    # Luis González
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
            
            
    
