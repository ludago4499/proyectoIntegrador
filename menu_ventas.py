import config
import manejar_vendedores
import time
import manejar_inventario

ARCHIVO_COSTOS_Y_PRECIOS = "costos_y_precios.csv"
ARCHIVO_VENTAS = "listaVentas.csv"
def print_menu (nombre_vendedor) -> None:
    '''Se imprime el menú que se puede vender dentro de Dairy Queen. Se requiere
    del nombre del vendedor para asegurar que es la persona correcta
    Luis Gzz
    '''
    print("Vendedor:", nombre_vendedor)
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
Pasos para hacer una venta en el sistema. (ALGORITMO)
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

def preguntar_vendedor():
    '''
    Pregunta al usuario por el vendedor que hace la venta
    Retorna el vendedor y el id de ese vendedor
    Luis González
    '''
    lista = config.recibir_archivo(manejar_vendedores.ARCHIVO_VENDEDORES)
    config.guiones()
    print("Qué vendedor esta haciendo la venta?")
    print("O escriba 'salir' para salir")
    manejar_vendedores.print_nombre_vendedor()
    config.guiones()
    seleccion = input("Seleccion: ")
    [id,row] = manejar_vendedores.obtener_id_y_fila(lista,seleccion)
    if (id == -2):
        print("Saliendo...")
        return [0,-2]
    if (id ==-1):
        print ("Vendedor no encontrado. Intente nuevamente")
        time.sleep(1)
        return preguntar_vendedor()
    print ("Se seleccionó ", seleccion, ".")
    config.guiones()
    return [seleccion,id]

def checar_suficiente_inventario(lista_inventario: list,cantidad: int,id_inventario: int) -> bool:

    '''Si hay suficiente en el inventario, esta función retorna true sino retorna false. 
    Se requiere de la lista de inventario, la cantidad que se ocupa, y el id del inventario
    Luis González '''
    for i in range(1,len(lista_inventario)):
        if (int(lista_inventario[i][1]) == id_inventario):
            if (float(lista_inventario[i][2]) >= cantidad):
                return True
            else:
                return False
    return False

def preguntar_cantidad() -> int:
     
     '''Función de utilidad que pregunta la cantidad '''
     flag = True
     while (flag):
        flag = False
        cantidad = (input("Cantidad: "))
        cantidad = config.checar_seleccion(cantidad)
        if (cantidad == -2):
            return -1
        if (cantidad == -1):
            flag = True
        if (cantidad <=0):
            print("El número debe ser mayor a 0. Intente nuevamente.")
            time.sleep(1)
            flag = True
     return cantidad

def print_no_hay_suficiente() -> None:
    '''Función para automatizar el mensaje de no hay suficiente'''
    print ("No hay suficiente en el inventario.")
    print( "Se regresará al menú anterior.")
    config.guiones()
    time.sleep(1)

def checar_fecha_completa (fecha: str) -> bool:
    '''Similar a checar_fecha de datos_de_venta se checa si la fecha está en el formato
    correcto. Sin embargo este también incluye el día. Se retorna un valor booleano.
    Se podría mejorar utilizando una librería ya existente, pues se aceptan casos como el 31
    de febrero
    Luis Gzz'''
# 12/12/2008

    if (config.desea_salir(fecha)):
        return -2 # salir
    
    day = fecha[0:2]
    month = fecha[3:5]
    year = fecha[6:]
    day = config.checar_seleccion(day)
    if day == -1:
        return False
    month = config.checar_seleccion(month)
    if month == -1:
        return False
    year = config.checar_seleccion(year)
    if (year == -1):
        return False
    if (day >0 and day <= 31 and month>0 and month <=12 and year >= 1000 and year <=9999):
        print("Fecha aceptada")
        return True
    print("Fecha no es válida. Cheque el formato nuevamente.")
    time.sleep(1)
    return False

def blizzard(fecha: str, id_vendedor:str ) -> None:

    '''Función para vender un Blizzard en específico.
    Se requiere de la fecha y el id vendedor que hace la venta.'''
    archivo_costos = "costos_y_precios.csv"
    nieve_size = [0.300,0.500,0.800] # cantidad de nieve a usar
    id_nieve = 1
    id_costos = [1,2,3]
    # la nieve es id 1
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
        return blizzard(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >3):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return blizzard(fecha,id_vendedor)
    seleccion -= 1
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    cantidad_nieve_a_usar = nieve_size[seleccion -1] * cantidad # se calcula la nieve a utilizar
    hay_suficiente = checar_suficiente_inventario(lista_inventario,cantidad_nieve_a_usar,id_nieve)
    
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    
    # se actualizan los archivos para procesar la compra

    quitar_del_inventario(id_nieve,cantidad_nieve_a_usar,lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor) 
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def cono(fecha: str, id_vendedor:str):
    '''Función para vender cualquier tipo de cono'''
    nieve_size = [0.2, 0.3, 0.4, 0.4, 0.4]
    id_nieve_inventario = 1
    id_costos = [4,5,6,19,20]
    config.guiones()
    print("Cuál tipo de cono desea.? ")
    print("Cono sencillo (1)")
    print("Cono doble (2)")
    print("Cono triple (3)") 
    print("Cono Waffle (4)")
    print("Cono Cubierto (5)")
    config.guiones()
    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return cono(fecha, id_vendedor)
    if (seleccion < 1 or seleccion >5):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return cono(fecha, id_vendedor) 
    if (seleccion <4):
        cono_id = seleccion + 5 # se acomoda para tener cono de 6,7,8
    else:
        cono_id = 13 + seleccion
    seleccion -=1
    cantidad = preguntar_cantidad()
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    cantidad_nieve_a_usar = nieve_size[seleccion -1] * cantidad
    # la cantidad de conos siempre va a ser igual a cantidad de compra 
    hay_suficiente = checar_suficiente_inventario(lista_inventario,cantidad_nieve_a_usar,id_nieve_inventario)
    if (hay_suficiente):
        hay_suficiente = checar_suficiente_inventario(lista_inventario, cantidad,cono_id)
    
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    
    # se actualizan los archivos para procesar la compra
    quitar_del_inventario(id_nieve_inventario,cantidad_nieve_a_usar,lista_inventario)
    quitar_del_inventario(cono_id,cantidad,lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor) 
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def pastel(fecha: str, id_vendedor:str):

    ''''
    Función que completa la venta de un pastel. Requiere
    de la fecha y el id_vendedor del vendedor.
    Luis Gzz
    '''
    id_pastel_inventario = [9,10,11,12,13]
    id_pastel_costos = [7,12,13,14,15,11]
    config.guiones()
    print ("Qué tipo de pastel?")
    print( "Pastel Oreo (1)")
    print ("Pastel Choco Xtreme (2)")
    print( "Pastel de Fresa (3)")
    print( "Pastel de Fresa Pay de Queso (4)")
    print ("Pastel de la Rosa (5)")
    config.guiones()
    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return pastel(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >5):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return pastel(fecha,id_vendedor)
    seleccion -=1
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    cantidad_pasteles = cantidad
    hay_suficiente = checar_suficiente_inventario(lista_inventario,cantidad_pasteles,id_pastel_inventario[seleccion])
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    quitar_del_inventario(id_pastel_inventario[seleccion],cantidad_pasteles,lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_pastel_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor)
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def banana_split(fecha: str,id_vendedor:str):
    '''Opción de ventas para banana splits'''
    ctd_platanos = [0.5,0.75,1]
    id_platanos = 2
    ctd_fresa = [3,4,5]
    id_fresa = 4
    ctd_cereza = [3,4,5]
    id_cereza = 3
    ctd_crema_batida = [0.5,0.75,0.8] #medio bote
    id_crema_batida = 5

    ctd_nieve = [0.500,0.75,1]
    id_nieve = 1

    id_bs_costos = [8,9,10]
    config.guiones()
    print("Qué tamaño de Banana Split?")
    print("[1] Banana Split Chico")
    print("[2] Banana Split Mediano")
    print("[3] Banana Split Grande")
    config.guiones()

    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return banana_split(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >3):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return banana_split(fecha,id_vendedor)
    seleccion = seleccion -1 # cambia la selección, pues python trabajo iniciando con 0
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)


    # checa si hay suficiente
    hay_suficiente = checar_suficiente_inventario(lista_inventario,ctd_platanos[seleccion] * cantidad,id_platanos)
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    hay_suficiente = checar_suficiente_inventario(lista_inventario,ctd_fresa[seleccion] * cantidad,id_fresa)
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    hay_suficiente = checar_suficiente_inventario(lista_inventario,ctd_cereza[seleccion] * cantidad,id_cereza)
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    hay_suficiente = checar_suficiente_inventario(lista_inventario, ctd_crema_batida[seleccion] * cantidad,id_crema_batida)
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    hay_suficiente = checar_suficiente_inventario(lista_inventario,ctd_nieve[seleccion] * cantidad,id_nieve)
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    
    # quitar del inventario los productos
    quitar_del_inventario(id_platanos,ctd_platanos[seleccion],lista_inventario)
    quitar_del_inventario(id_fresa,ctd_fresa[seleccion],lista_inventario)
    quitar_del_inventario(id_cereza,ctd_cereza[seleccion],lista_inventario)
    quitar_del_inventario(id_crema_batida,ctd_crema_batida[seleccion],lista_inventario)
    quitar_del_inventario(id_nieve,ctd_nieve[seleccion],lista_inventario)
    
    [producto,costo,precio,iva] =  obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_bs_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor)
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def cafe(fecha: str, id_vendedor:str):

    '''
    Se agrega la función para vender cafés. 
    '''
    config.guiones()
    print("Qué tipo de café se desea vender?")
    print("[1] Café Frappe")
    print("[2] Café Latte")
    print("[3] Cafe Slush")
    config.guiones()

    id_inventario = [19,20,21] 
    id_costos = [21,22,23]
    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return cafe(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >3):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return cafe(fecha,id_vendedor)
    seleccion = seleccion -1 # cambia la selección, pues python trabajo iniciando con 0
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    
    #checa si hay suficiente

    hay_suficiente = checar_suficiente_inventario(lista_inventario,cantidad,id_inventario[seleccion])
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    
    #quitar del inventario los productos
    quitar_del_inventario(id_inventario[seleccion],cantidad,lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor)
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def malteadas(fecha:str, id_vendedor:str):
    '''Se agrega la función para vender malteadas'''

    config.guiones()
    print("Qué tipo de malteada se desea vender?")
    print("[1] Malteada Frutos Rojos")
    print("[2] Malteada Crema de Avellana")
    print("[3] Malteada Mango")
    print("[4] Malteada Caramelo")
    print("[5] Malteada Vainilla")
    print("[6] Malteada Chocolate")
    print("[7] Malteada Fresa")
    config.guiones()

    id_costos = [24,25,26,27,28,29,30]
    id_inventario = [22,23,24,25,26,27,28]
    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return malteadas(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >7):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return malteadas(fecha,id_vendedor)
    seleccion -= 1
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    
    #checa si hay suficiente

    hay_suficiente = checar_suficiente_inventario(lista_inventario,cantidad,id_inventario[seleccion])
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    quitar_del_inventario(id_inventario[seleccion],cantidad, lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_costos[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor)
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def extras(fecha:str, id_vendedor: str):
    '''Función para cualquier extra no encontrado en el menú anterior'''
    config.guiones()
    print("Cuáles de los extras desea vender?")
    print("[1] Blizzard Familiar")
    print("[2] DQ Sandwich")
    print("[3] Dilly Bar")
    print("[4] Sundae")
    print("[5] Triple Chocolate Parfait")
    print("[6] Pecan Mudslide")
    print("[7] Canasta Waffle")
    print("[8] Ingrediente Extra")
    id_costo = [15,16,17,18,31,32,33,34]
    id_inventario = [1,14,15,16,29,30,31,32]
    config.guiones()
    seleccion = (input("Selección: "))
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    if (seleccion == -1):
        return extras(fecha,id_vendedor)
    if (seleccion < 1 or seleccion >8):
        print("Ese número no está en la lista. Intente nuevamente")
        time.sleep(1)
        return extras(fecha,id_vendedor)
    seleccion = seleccion -1 # cambia la selección, pues python trabajo iniciando con 0
    cantidad = preguntar_cantidad() # se pregunta la cantidad
    if (cantidad == -1):
        return -1
    config.guiones()
    lista_inventario = config.recibir_archivo(manejar_inventario.ARCHIVO_INVENTARIO)
    
    # checa si hay suficiente

    hay_suficiente = checar_suficiente_inventario (lista_inventario,cantidad,id_inventario[seleccion])
    if (not hay_suficiente):
        print_no_hay_suficiente()
        return -1
    #quitar del inventario

    quitar_del_inventario(id_inventario[seleccion], cantidad, lista_inventario)
    [producto,costo,precio,iva] = obtener_producto_costo_precio_iva(ARCHIVO_COSTOS_Y_PRECIOS,id_costo[seleccion])
    costo = float(costo) * cantidad
    precio = float(precio) * cantidad
    iva = float(iva) * cantidad
    agregar_a_ventas(producto,cantidad,costo,precio,fecha,iva, id_vendedor)
    print ("Precio: ", precio)
    print( "Listo! Se regresará al menú principal.")
    config.guiones()
    time.sleep(1)
    return -1

def obtener_producto_costo_precio_iva (filename: str, id_producto: int) -> list:
    '''
    Desde un archivo y un id, se obtiene una lista 
    que incluye el producto costo precio e IVA en ese orden
    '''
    # Hecho por Erick 
    lista_costos = config.recibir_archivo(filename) 

    ctd_filas = len(lista_costos)
    fila = -1
    for i in range(1,ctd_filas):
        if (int(lista_costos[i][1]) == id_producto):
            fila = i
    if not fila == -1:
        resultado = []
        resultado.append(lista_costos[fila][0]) # obtiene producto
        resultado.append(lista_costos[fila][2]) # obtiene costo
        resultado.append(lista_costos[fila][3]) # obtiene precio
        resultado.append(lista_costos[fila][4]) # obtiene iva
        return resultado
    else:
        return [-1,0,0,0] # error

 # agregar a la lista de ventas -> pedir cantidad, fecha

def agregar_a_ventas(producto: str,cantidad: int,costo:float, precio:float,fecha:str,iva:float,id_vendedor:int) -> None:
    '''
    Se agrega a la lista de Ventas para documentar el proceso. Asimismo, se agrega en costos_y_precios.csv'
    Se requiere de varias características del producto para esto.
    '''

    # agregar a ventas
    if (producto == -1): # caso error
        return
    
    lista_ventas = config.recibir_archivo(ARCHIVO_VENTAS)
    contribucion = round(float(precio)- float(costo),2)
    newRow = [producto,cantidad,costo,precio,contribucion,fecha,iva,id_vendedor]
    lista_ventas = config.add_row(lista_ventas,newRow)
    config.actualizar_archivo(ARCHIVO_VENTAS,lista_ventas)

    lista_costos_y_precios = config.recibir_archivo(ARCHIVO_COSTOS_Y_PRECIOS)
    fila = obtener_fila_costos(lista_costos_y_precios,producto)
    lista_costos_y_precios[fila][5] = int( lista_costos_y_precios[fila][5]) + 1
    config.actualizar_archivo(ARCHIVO_COSTOS_Y_PRECIOS,lista_costos_y_precios)

def obtener_fila_costos (lista_costos:list, producto:str ) -> int:
    '''De un producto vendido se obtiene el número de la fila 
    en "costos_y_precios.csv"'''
    for i in range(1,len(lista_costos)):
        if (lista_costos[i][0] == producto):
            return i
    return -1 # no encontrado

def quitar_del_inventario (id:int,cantidad:float,lista_inventario: list) -> None:
    '''Resta del inventario el objeto un id en particular
    una cantidad en particular
    Luis Gzz'''
    for i in range(1,len(lista_inventario)):
        if (int(lista_inventario[i][1]) == id):
            lista_inventario[i][2] = round(float(lista_inventario[i][2]) - cantidad,2)
            config.actualizar_archivo(manejar_inventario.ARCHIVO_INVENTARIO,lista_inventario)
            return
        
def seleccion_registrar_venta(seleccion: int, fecha: str, id_vendedor: str):
    '''
    Se utiliza la seleccion de producto, la fecha y el id_vendedor 
    para realizar la venta en el sistema. Cada selección tiene diferentes
    características, pues cada producto lleva diferentes cosas del inventario 
    '''
    match seleccion:
        case 1:
            return blizzard(fecha,id_vendedor)
        case 2:
            return cono(fecha,id_vendedor)
        case 3:
            return pastel(fecha, id_vendedor) 
        case 4:
            return banana_split(fecha, id_vendedor)
        case 5:
            return cafe(fecha, id_vendedor)
        case 6:
            return malteadas(fecha, id_vendedor)
        case 7:
            return extras(fecha, id_vendedor)
        case _:
            print("Esa opción no está en la lista. Intente nuevamente")
            time.sleep(1)
            config.guiones()
            return -1