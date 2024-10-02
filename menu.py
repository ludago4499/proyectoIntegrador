import config

def print_menu () -> None:
    print("Ingrese el objeto que se vendió: ")
    print("Blizzard (1)")
    print ("Cono (2)")
    print ("Pastel (43")
    print("Banana Split (4)")
    print ("Extras (5)") # por ahora no


def blizzard():
    archivo_costos = "costos_y_precios.csv"
    nieveSize = [300,500,800] # cantidad de nieve a usar
    # precio = [60,70,80]
    # costo = [30,35,40]
    print("Cuál es el tamaño? ")
    print("Chico (1)")
    print("Mediano (2)")
    print("Grande (3)") 
    

    # agarrar costo, precio e iva

    costo_y_precio = obtener_costo_precio_iva(archivo_costos,)
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
def obtener_costo_precio_iva (filename, nombre_producto) -> list:
    # Hecho por Erick 
    lista_costos = config.recibir_archivo(filename) 

    ctd_filas = len(lista_costos)
    fila = -1
    for i in range(ctd_filas):
        if (lista_costos[i][0] == nombre_producto):
            fila = i
    if not fila == -1:
        return lista_costos [fila][1:3]
    else:
      return -1

 # agregar a la lista de ventas -> pedir cantidad, fecha

def agregar_a_ventas(producto,cantidad,precio,costo,fecha,iva) -> None:
    return

    # restar en inventario 

x = obtener_costo_precio_iva("costos_y_precios.csv", "Blizzard C")
print(x)