import config
import time
import manejar_vendedores
# archivo para analizar datos de las ventas
ARCHIVO_LISTA_VENTAS = "listaVentas.csv"

def menu_datos_ventas() -> None:
    '''Imprime el menú de datos de ventas'''
    print("Qué desea hacer?")
    print("O ingrese 'salir' para salir")
    print("[1] Ver una vista general de las Ventas")
    print("[2] Ver lo vendido por un vendedor en específico")
    print("[3] Calculación de IVA en un mes en específico")
    print("[4] Calculación de Contribución en un mes en específico")

def print_listaVentas(lista: list):
    '''
    Se requiere formatear las listas por diferentes tamaños para mostrarse correctamente
    en la terminal sin tener que abrirse el archivo. Se utiliza el .format()
    Luis González
    '''
    if (lista == None):
        return
    lista_original = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)
    header = lista_original[0]
    format_string = "{:<15} {:<10} {:<10} {:<10} {:<15} {:<12} {:<10} {:<12}" 
    print(format_string.format(*header))
    for i in range(0,len(lista)):
        print_list =[] 
        for j in range(len(lista[i])):
            print_list.append(lista[i][j]) 
        print(format_string.format(*print_list))     

def vista_general ():
    '''Permite al usuario generar una vista general de las ventas por una cierta cantidad a la vez.'''

    # Luis González
    config.guiones()
    flag = True
    print("Cuántos datos quiere mostrar a la vez? ")
    max = input("Selección: ")
    max = config.checar_seleccion(max)
    if (max == -1):
        print("Número no aceptado. Intente nuevamente")
        return vista_general()
    elif(max == -2):
        return -1

    lista = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)
    ctd_filas = len(lista)
    filas_faltantes = ctd_filas - 1 # se quita el header
    while (filas_faltantes > 0 and flag == True):
        print("Desea ver los siguientes", max, "datos?")
        seleccion = checar_continuar()
        if (seleccion == -1):
            return -1
        if (seleccion == 2):
            print("Se ha terminado con éxito")
            flag = False


        if (flag):
            ctd_filas_leidas = ctd_filas - filas_faltantes
            if (filas_faltantes > max):
                lista_reducida = lista[ctd_filas_leidas:ctd_filas_leidas + max]
                filas_faltantes -= max
                print_listaVentas(lista_reducida)
            else:
                filas_faltantes = 0
                lista_reducida= lista[ctd_filas_leidas:]
                print_listaVentas(lista_reducida)
                print("Se ha terminado de leer.")
           
            config.guiones()
    return -1 # regresa al menu principal

def vista_vendedor():
    '''Permite al usuario ver todas las ventas de un vendedor en particular'''
    print("De que vendedor se desea ver sus ventas?")
    print("O escriba 'salir' para salir")
    config.guiones()
    lista_vendedores = config.recibir_archivo(manejar_vendedores.ARCHIVO_VENDEDORES)
    manejar_vendedores.print_nombre_vendedor()
    config.guiones()
    seleccion = input("Selección: ")
    [id,row_vendedores] = manejar_vendedores.obtener_id_y_fila(lista_vendedores,seleccion)
    if (id == -2):
        print("Saliendo...")
        return -1
    if (id ==-1):
        print ("Vendedor no encontrado. Intente nuevamente")
        time.sleep(1)
        return vista_vendedor()
    lista_ventas = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)

    filtered_rows = filtrar_filas_id(lista_ventas,id)
    if (not len(filtered_rows) == 0 ):
        print_listaVentas(filtered_rows)
        print("Se han imprimido todas las ventas con éxito.")
    else: 
        print("No hay ventas de este vendedor en particular. ")

    print("Se regresará para seleccionar otro vendedor.")
    config.guiones()
    time.sleep(1)
    return vista_vendedor()

def calculacion_iva_mes ():

    '''Se suma todo el iva generado por ventas en un mes específico'''

    print("Se calculará el total de IVA a pagar en un mes en específico.")
    print("Ingrese el mes y el año siguiente el formato (mm/yyyy). Ejemplo '12/2008' ")
    print("O ingrese 'salir' para salir")
    fecha = input("Selección: ")

    if (config.desea_salir(fecha)):
        print("Saliendo...")
        return -1
    if (not checar_fecha(fecha)):
        return calculacion_iva_mes()
    lista = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)

    filtered_rows = filtrar_filas_fecha(lista, fecha)
    print_listaVentas(filtered_rows)
    iva_total = sumar_iva(filtered_rows)
    print("Se imprimió todos los resultados.")
    print("El total de IVA del mes", fecha, "es el siguiente:",iva_total)
    print("Se regresará a este menú para escoger otro mes")
    return calculacion_iva_mes()
def calculacion_contribucion_mes():
    '''Calcula el dinero obtenido con la contribución, que es 
    básicamente ganancias sin considerar costos fijos'''
    print("Se calculará el total de contribución  en un mes en específico.")
    print("Ingrese el mes y el año siguiente el formato (mm/yyyy). Ejemplo '12/2008' ")
    print("O ingrese 'salir' para salir")
    fecha = input("Selección: ")
    
    if (config.desea_salir(fecha)):
        print("Saliendo... ")
        return -1
    if (not checar_fecha(fecha)):
        return calculacion_iva_mes()
    lista = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)
    lista = config.recibir_archivo(ARCHIVO_LISTA_VENTAS)

    filtered_rows = filtrar_filas_fecha(lista, fecha)
    print_listaVentas(filtered_rows)
    contribucion_total = sumar_contribucion(lista)
    print("Se imprimieron todos los resultados.")
    print("El total de contribución de este mes es de:", contribucion_total)
    print("Se regresará a este menú para escoger otro mes.")
    return calculacion_contribucion_mes()

def checar_fecha(fecha) -> bool:
    '''
    Se valida que la fecha sea una fecha correcta
    '''
    month = fecha[0:2]
    year = fecha[3:] 
    month = config.checar_seleccion(month)
    year = config.checar_seleccion(year)
    if (month == -1 or year == -1):
        return False
    if (month > 0 and month <= 12 and year >= 1000 and year <= 9999):
        print ("Fecha aceptada.")
        return True
    print("Fecha no es válida. Cheque el formato nuevamente.")
    config.guiones()
    time.sleep(1)
    return False

def filtrar_filas_id (lista: list,id: int)-> list:
    '''
    Crea una lista filtrada con únicamente filas que tienen en la columna
    de id vendedor un id en particular
    # Luis González
    '''
    filtered_rows = []
    for i in range(len(lista)):
        if (lista[i][7] == str(id)):
            filtered_rows.append(lista[i])
    return filtered_rows

def filtrar_filas_fecha (lista: list,fecha) -> list:

    '''
    Regresa las filas con la fecha especificada.
    '''
    pos_fecha = 5 # esta en la columna 5 fecha
    filtered_rows = []
    for i in range(1,len(lista)):
        fecha_venta = lista[i][pos_fecha][3:]
        if (fecha_venta == fecha):
            filtered_rows.append(lista[i])
    return filtered_rows

def sumar_iva (lista_filtrada: list)-> float:
    '''suma todo el iva usando la lista filtrada'''
    pos_iva = 6
    iva_total = 0
    if (lista_filtrada == None):
        return
    for i in range(len(lista_filtrada)):
        iva_total += float(lista_filtrada[i][pos_iva])
    return iva_total

def sumar_contribucion(lisa_filtrada:list)->float:
    '''Suma toda la contribucion de una lista_filtrada'''
    pos_contribucion = 4
    contribucion_total = 0
    if (lisa_filtrada == None):
        return
    for i in range(1,len(lisa_filtrada)):
        contribucion_total += float(lisa_filtrada[i][pos_contribucion])
    return contribucion_total

def checar_continuar() -> int:
    '''Checa si desea continuar el usuario'''
    print("Escriba '1' para confirmar")
    print ("Escriba '2' para terminar")
    seleccion = input("Seleccion: ")
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return -1
    elif (seleccion == -1):
        print("No es un número válido")
        config.guiones()
        return checar_continuar()
    
    if seleccion == 1 or seleccion == 2:
        return seleccion
    else:
        print("No se ha entendido. Verifique su entrada nuevamente.")
        time.sleep(1)
        return checar_continuar()
    
def seleccion_datos_ventas(seleccion: int):
    '''Seleccion para el submenú de análisis de ventas'''
    match seleccion:

        case 1:
            return vista_general()
        case 2:
            return vista_vendedor()
        case 3:
            return calculacion_iva_mes()
        case 4:
            return calculacion_contribucion_mes()
        case _:
            print ("Esa opción no está en la lista, intente nuevamente")
            time.sleep(1) # Se espera un segundo
            return -1

