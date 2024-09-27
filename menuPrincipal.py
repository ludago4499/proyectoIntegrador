import time

def desplegar_menu_principal() -> None:
# Luis González
# Se despliega el menú principal
    print("Bienvenido al sistema de Manejo de Dairy Queen. ")
    print("Seleccione la opción del siguiente menú: ")
    print("[1] Registrar una venta")
    print("[2] Registrar llegado de artículos al almacén")
    print("[3] Consultar datos del inventario")
    print ("[4] Consultar datos de las ventas")
    print("[5] Mostrar reportes de ventas por vendedor o por artículo")
    print ( "[6] Salir")

def registrar_una_venta () -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")

    seleccion = input("")

def registrar_articulos() -> None:
    # follow up
    print("Ingrese 'salir' si quiere regresar al menú principal. ")
    seleccion = input("")

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

def seleccion_menu_principal(seleccion: int):
    # Case-match para abrir el menú correspondiente
    # Se regresa un "-1" si el número no se encuentra en las opciones
    # Luis González
    match seleccion:
        case 1:
            registrar_una_venta()
        case 2:
            registrar_articulos()
        case 3:
            consultar_datos_inventario()
        case 4:
            consultar_datos_ventas()
        case 5:
            mostrar_reportes()
        case 6:
            # Se termimna el programa debido a intención del usuario
            print ("Saliendo ... ")
            return # salir
        case _: 
            print ("Esa opción no está en la lista, intente nuevamente")
            time.sleep(1) # Se espera un segundo
            return -1
            
            
    
