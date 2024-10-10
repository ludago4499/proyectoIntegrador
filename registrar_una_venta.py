import config
import manejar_vendedores
import time
import manejar_inventario

ARCHIVO_COSTOS_Y_PRECIOS = "costos_y_precios.csv"
ARCHIVO_VENTAS = "listaVentas.csv"
def print_menu () -> None:
    # Luis González
    print("Ingrese el objeto que se vendió: ")
    print ("O ingrese 'salir' para salir")
    print("[1] Blizzard ")
    print ("[2] Cono ")
    print ("[3] Pastel")
    print("[4] Banana Split")
    print("[5] Cafe ")
    print( "[6] Malteadas")
    print ("[7] Extras ") 
    config.guiones()
'''
Pasos para hacer una venta en el sistema.
1. Obtener quien está haciendo la venta, preguntando iterando la lista de vendedores en ListaVendedores.csv
2.  Preguntar que se está vendiendo
3. Preguntar el tamaño y la cantidad
4.  Checar si hay suficiente, imprimir un mensaje de error que falta y cuánto falta exactamente
5. Si no hay error en el inventario, quitar esos objetos del inventaro y obtener el costo_precio e iva de los objetos obtenidos (se actualiza iva antes)
6. Asimismo, se agrega a la lista de Ventas con el id del vendedor que vendió el producto.
7. Se agrega directamente en costos_y_precios.
8. Hacer print al precio final y hacer un cálculo rápido de feria para ayudar al cajero, ingresar un 0 implica hacer skip a esto
9. Hacer print 'Listo' y preguntar si desea hacer otra venta o si quiere hacer 'salir' para salir.

'''

def preguntar_vendedor(lista):
    '''
    Pregunta al usuario por el vendedor que hace la venta
    Retorna el vendedor y el id de ese vendedor
    Luis González
    '''
    manejar_vendedores.ARCHIVO_VENDEDORES
    config.guiones()
    print("Qué vendedor esta haciendo la venta? ")
    print("O escriba 'salir' para salir")
    manejar_vendedores.print_nombre_vendedor
    config.guiones()
    seleccion = input("Seleccion: ")
    [id,row] = manejar_vendedores.obtener_id_y_fila(lista,seleccion)
    if (id == -2):
        print("Saliendo...")
        return [-1,0]
    if (id ==-1):
        print ("Vendedor no encontrado. Intente nuevamente")
        time.sleep(1)
        return preguntar_vendedor()
    print ("Se seleccionó ", seleccion, ".")
    config.guiones()
    return [seleccion,id]

def checar_suficiente_inventario(lista,cantidad,id) -> bool:

    '''Si hay suficiente en el inventario, esta función retorna true. 
    Luis González '''
    for i in range(1,len(lista)):
        if (lista[i][1] == id):
            if (lista[i][2] >= cantidad):
                return True
            else:
                return False
    return False

def preguntar_fecha():
    return
    

def blizzard() -> None:
    archivo_costos = "costos_y_precios.csv"
    nieve_size = [300,500,800]/1000 # cantidad de nieve a usar
    # la nieve es id 1
    fecha_tentativa = "08/12/2024"
    config.guiones()
    print("Cuál es el tamaño? ")
    print("O escriba 'salir' para salir")
    print("[1] Chico") 
    print("[2] Mediano")
    print("[3] Grande") 
    config.guiones()

    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return blizzard()
    if (seleccion < 0 or seleccion >3):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return blizzard
    

    flag = True
    while (flag):
        flag = False
        cantidad = (input("Cantidad: "))
        cantidad = config.checar_seleccion(cantidad)
        if (cantidad == -2):
            return -1
        if (seleccion == -1):
            flag = True
        if (seleccion <=0):
            print("El número debe ser mayor a 0. Intente nuevamente.")
            time.sleep(1)
            flag = True
    config.guiones()
    lista = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    cantidad_nieve_a_usar = nieve_size(seleccion -1) * cantidad # se calcula la nieve a utilizar
    hay_suficiente = checar_suficiente_inventario(lista,cantidad_nieve_a_usar,1)
    
    if (not hay_suficiente):
        print ("No hay suficiente en el inventario.")
        print( "Se regresará al menú anterior.")
        time.sleep(1)
        return -1
    
    # se actualizan los archivos para procesar la compra

    quitar_del_inventario(id,cantidad_nieve_a_usar,lista)
    [producto,costo,precio,iva] = obtener_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id)
    agregar_a_ventas(producto,cantidad,costo,precio,fecha_tentativa,iva,1) # falta id_vendedor
    config.guiones()
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    time.sleep(1)
    return -1



    # agarrar costo, precio e iva

    costo_y_precio = obtener_costo_precio_iva(archivo_costos,id)
    # agregar a la lista de ventas -> pedir cantidad, fecha
    # restar en inventario 



def cono():
    precio = []
    print("Cuál es el tamaño? ")
    print("Cono sencillo (1)")
    print("Cono doble (2)")
    print("Cono triple (3)") 


def pastel():
    print ("Qué tipo de pastel")
    print( "Pastel Oreo (1)")
    print ("Pastel Choco Xtreme (2)")
    print( "Pastel de Fresa (3)")


def banana_split():
    platanos = 1
    fresa = 3
    cereza = 3
    crema_batida = 0.5
    nieve = 500

# agarrar costo, precio e iva
def obtener_costo_precio_iva (filename: str, id: int) -> list:
    '''
    Desde un archivo y un id, se obtiene una lista 
    que incluye el costo precio e IVA
    '''
    # Hecho por Erick 
    lista_costos = config.recibir_archivo(filename) 

    ctd_filas = len(lista_costos)
    fila = -1
    for i in range(ctd_filas):
        if (lista_costos[i][1] == id):
            fila = i
    if not fila == -1:
        resultado = []
        resultado.append(lista_costos[fila][0]) # obtiene producto
        resultado.append(lista_costos[fila][2]) # obtiene costo
        resultado.append(lista_costos[fila][3]) # obtiene precio
        resultado.append(lista_costos[fila][4]) # obtiene iva
        return resultado
    else:
        return -1

 # agregar a la lista de ventas -> pedir cantidad, fecha

def agregar_a_ventas(producto: str,cantidad: int,costo:float, precio:float,fecha:str,iva:float,id_vendedor:int) -> None:
    '''
    Se agrega a la lista de Ventas para documentar el proceso. Asimismo, se agrega en costos_y_precios.csv'
    '''
    # agregar a ventas
    lista = config.recibir_archivo(ARCHIVO_VENTAS)
    contribucion = costo-precio
    newRow = [producto,cantidad,costo,precio,contribucion,fecha,iva,id_vendedor]
    lista = config.add_row(lista,newRow)
    config.actualizar_archivo(ARCHIVO_VENTAS,lista)

    lista_costos_y_precios = config.recibir_archivo(ARCHIVO_COSTOS_Y_PRECIOS)
    fila = obtener_fila_costos(lista,producto)
    lista_costos_y_precios[fila][5] = int( lista_costos_y_precios[fila][5]) + 1
    config.actualizar_archivo(ARCHIVO_COSTOS_Y_PRECIOS,lista_costos_y_precios)


def obtener_fila_costos (lista:list, producto:str ) -> int:
    '''De un producto vendido se obtiene el número de la fila 
    en "costos_y_precios.csv"'''
    for i in range(1,len(lista)):
        if (lista[i][0] == producto):
            return i
    return -1 # no encontrado

def quitar_del_inventario (id:int,cantidad:float,lista: list) -> None:
    '''Resta del inventario el objeto un id en particular
    una cantidad en particular
    Luis Gzz'''
    for i in range(1,len(lista)):
        if (lista[i][1] == id):
            lista[i][2] = float(lista[i][2]) - cantidad
    config.actualizar_archivo(manejar_inventario.ARCHIVO_INVENTARIO,lista)

def seleccion_registrar_venta(seleccion: int):
    match seleccion:
        case 1:
            return blizzard()
        case 2:
            return cono()
        case 3:
            return pastel()