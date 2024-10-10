import config
import time

ARCHIVO_VENDEDORES = "listaVendedores.csv"

def menu_vendedor ():
    config.guiones()
    print("Este es el menú para los vendedores")
    print("Qué se desea hacer?")
    print("O ingrese 'salir' para salir")
    print("[1] Agregar a un vendedor")
    print("[2] Cambiar datos de un vendedor")
    print ("[3] Eliminar a un vendedor")

def agregar_vendedor():
    '''
    Se agrega un vendedor al archivo, se hacen varias comprobaciones 
    para asegurar un manejo correcto de los archivos.
    
    '''
    # Luis González
    config.guiones()
    flag = True
    print ("Recuerde que puede escribir 'salir' en cualquier momento para salir")
    while flag:
        flag = False
        nombre_vendedor = input("Ingrese el nombre del vendedor: ") 
        nombre_vendedor = checar_nombre(nombre_vendedor)
        if nombre_vendedor == -1:
          flag = True
        if nombre_vendedor == -2:
            print("Saliendo...")
            return -1
    flag = True
    while flag:
        flag = False
        telefono_vendedor = input("Teléfono del vendedor (solo números): ")
        telefono_vendedor = checar_telefono(telefono_vendedor)
        if telefono_vendedor == -1:
            flag = True
    
    flag = True
    while flag:
        flag = False
        descripcion_vendedor = input("Descripcion: ")
        descripcion_vendedor = checar_descripcion(descripcion_vendedor)
        if (descripcion_vendedor == -1):
            flag = True
    lista = config.recibir_archivo(ARCHIVO_VENDEDORES)
    id_vendedor = generar_id(lista)
    fila = [nombre_vendedor, id_vendedor, telefono_vendedor, descripcion_vendedor]

    print ("Se agregará un vendedor con la siguiente información: ")
    for i in range(len(fila)):
        if (not i == 1):
            print(fila[i])
    config.guiones()

    flag = True
    while flag:
        print("Escriba 'confirmar' si desea continuar.")
        print("O escriba 'reiniciar' para reiniciar.")
        seleccion = input("Su respuesta: ") 
        if (seleccion == 'confirmar'):
            flag = False
        elif (seleccion == 'reiniciar'):
            return agregar_vendedor() # se reinicia
        else:
            print("Hubo un error. Verifique nuevamente.")
            time.sleep(1)


    config.add_row(lista,fila)
    config.actualizar_archivo(ARCHIVO_VENDEDORES,lista)
    print ("Se ha actualizado con éxito")
    return -1 # se regresa para que se repita el menú nuevamente

def cambiar_datos():
    # Luis González
    config.guiones()
    lista = config.recibir_archivo(ARCHIVO_VENDEDORES)
    print("De qué vendedor se desea cambiar datos? ")
    print("O escriba 'salir' para salir.")
    config.guiones()
    print_nombre_vendedor()
    config.guiones()
    seleccion = input("Selección: ")
    [id,row] = obtener_id_y_fila(lista,seleccion)
    if (id == -2):
        print("Saliendo...")
        return -1
    if (id ==-1):
        print ("Vendedor no encontrado. Intente nuevamente")
        time.sleep(1)
        return cambiar_datos()
    print ("Se seleccionó ", seleccion, ".")
    config.guiones()
    print ( "Los datos del vendedor son los siguientes: ")
    print_datos_vendedor(row, lista)
    config.guiones()
    print ("Qué se desea modificar?")
    print_columnas(lista,0)
    config.guiones()
    flag = True
    while (flag):
        seleccion = input("Selección: ") 
        col = obtener_columna(seleccion,lista)
        if ( col == -2):
            return cambiar_datos()
        if (not col == -1):
            flag = False
    config.guiones()
    flag = True
    while (flag):
        print( "El valor actual de ", lista[0][col], "es de: ", lista[row][col])
        print ("A que lo desea cambiar? ")
        print( "O escriba 'cancelar' para cancelar.")
        nuevo_valor = input("Cambio: ")
        if (col == 2):
            nuevo_valor = checar_telefono(nuevo_valor)
            if (nuevo_valor == -2):
                return cambiar_datos()
            if (not nuevo_valor == -1):
                flag = False
            
        else: # si no es un número hacer verificación básica
            nuevo_valor = checar_nombre(nuevo_valor)
            if (nuevo_valor == -2):
                return cambiar_datos()
            if (not nuevo_valor == -1):
                flag = False

    lista[row][col] =nuevo_valor
    config.actualizar_archivo(ARCHIVO_VENDEDORES,lista)
    print ("Cambiado con éxito. Regresando al menú principal")
    time.sleep(1)
    return -1

def eliminar_vendedor():
    print("En este menú se podrá eliminar a un vendedor")
    print("Los cambios de esta decisión son finales. ")
    print ("Esta seguro que desea continuar? Escriba 'continuar' para continuar")
    seleccion = input("Confirmación: ")
    if not (seleccion == 'continuar' or seleccion == 'confirmar'):
        print("Operación cancelada. Se regresa el menú anterior.")
        time.sleep(1)
        return -1
    config.guiones()
    lista = config.recibir_archivo(ARCHIVO_VENDEDORES)
    print_nombre_vendedor()
    flag = True
    while flag:
        config.guiones()
        print("Cuál vendedor se deséa eliminar?")
        seleccion = input("Seleccion: ")
        [id,row] = obtener_id_y_fila(lista,seleccion) 
        if (id == -2):
            print( "Saliendo ...")
            return -1
        if (not id == -1):
            flag = False
    config.guiones()

    print( "Vendedor eliminado con éxito")
    print("Regresando al menú principal")
    lista[row][0] = "ELIMINADO " + lista[row][0] # se agrega el tag de eliminado'
    config.actualizar_archivo(ARCHIVO_VENDEDORES, lista)
    time.sleep(1)
    return -1

def seleccion_menu_vendedores(seleccion: int):
    # Case-match para abrir el menú correspondiente
    # Se regresa un "-1" si el número no se encuentra en las opciones
    # sin terminar
    match seleccion:
        case 1:
            return agregar_vendedor()
        case 2:
            return cambiar_datos()
        case 3:
            return eliminar_vendedor()
        case _: 

            print ("Esa opción no está en la lista, intente nuevamente")
            time.sleep(1) # Se espera un segundo
            return -1
            
def print_nombre_vendedor() -> None:
    lista = config.recibir_archivo(ARCHIVO_VENDEDORES)
    # imprime todos los nombres de los vendedores
    # excepto si estan eliminados
    for i in range(1,len(lista)):
        if (not lista[i][0][:9] == "ELIMINADO"):
         print(lista[i][0])

def print_datos_vendedor(row: int,lista: list) -> None:
    #imprime los datos de un solo vendedor
    for i in range(2,len(lista[row])):
        print(lista[0][i], lista[row][i])
    return

def print_columnas(lista: list, start = 0)-> None:
    #imprime las categorías de un vendedor
    for i in range (start,len(lista[0])):
        if (not i == 1):
            print (lista[0][i])

def obtener_id_y_fila (lista: list,nombre: str) -> list:
    '''
    Obtiene el id y la posición de la fila en donde 
    este encontrado un nombre.
    '''
    # obtiene
    if (config.desea_salir(nombre)):
        return [-2,0] # salir
    for i in range(1,len(lista)):
        if (lista[i][0] == nombre):
            return [int(lista[i][1]),i]
    return [-1,0] # no encontrado

def obtener_columna(nombre:str,lista:list) -> int:
    '''
    Obtiene que datos de la columna inicial se quiere modificar
    Es decir, nombre, telefono o descripción
    '''
    if (config.desea_salir(nombre)):
        print("Saliendo...")
        return -2 # salir
    for i in range (len(lista[0])):
        if (not i ==1 and lista[0][i] == nombre): # se evita el id
            return i
    print("No se ha encontrado. Intente nuevamente")
    return -1 # error 
    
def generar_id (lista:list) -> int:
    # obtiene el siguiente ID para evitar duplicados en el archivo
    return len(lista) 

def checar_nombre(nombre: str) -> str:
    # falta checar que no tenga commas
    # regresa -1 si contiene algún error
    # regresa -2 si el usuario desea salir
    if ',' in nombre:
        print("El nombre contiene commas. Favor de evitar las commas.")
        return -1
    if config.desea_salir(nombre):
        return -2
    else:
        return nombre

def checar_telefono(numero: int) -> int:
    # regresa -1 si contiene algún error
    # regresa -2 si el usuario desea salir
    if config.desea_salir(numero):
        return -2
    try:
        numero = int(numero)
    except ValueError:
        print ("Algo salió mal. Intente nuevamente.")
        return -1
    if len(str(numero)) == 10:
        return numero
    else:
        print ("El número no contiene 10 dígitos. Intente nuevamente")
        time.sleep(1)
        return -1

def checar_descripcion (descripcion: str) ->str:
    # falta checar que no tenga commas
    # regresa -1 si contiene algún error
    # regresa -2 si el usuario desea salir

    if ',' in descripcion:
        print("El nombre contiene commas. Favor de evitar las commas.")
        return -1
    elif config.desea_salir(descripcion):
        return -2
    else:
        return descripcion