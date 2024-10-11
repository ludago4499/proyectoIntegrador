import time
import config
import manejar_vendedores
import datos_de_ventas

ARCHIVO_COSTOS = "costos_y_precios.csv"

'''Clase para la opción 5 del menú del inicio'''

def print_submenu() -> None:
    config.guiones()
    print("Qué desea hacer?")
    print("O ingrese 'salir' para salir")
    config.guiones()
    print("[1] Mostrar archivo costos_y_precios.csv")
    print("[2] Generar datos de venta de un artículo")
    print("[3] Mostrar estadísticas de un vendedor")
    config.guiones()

def mostrar_archivo_costos() -> None:
   '''Función para desplegar el archivo de costos_y_precios.csv'''
   lista_inventario = config.recibir_archivo(ARCHIVO_COSTOS)
   config.guiones()
   header = lista_inventario[0]
   format_string = "{:<35} {:<5} {:<10} {:<10} {:<10} {:<10}"
   print(format_string.format(*header))
   for i in range(1,len(lista_inventario)):
      print_list = []
      for j in range(len(lista_inventario[i])):
         print_list.append(lista_inventario[i][j])
      print(format_string.format(*print_list))
   time.sleep(5)
   return -1 # regresar
def generar_datos_ventas():
   lista_costos = config.recibir_archivo(ARCHIVO_COSTOS)
   '''Genera datos básicos para un solo artículo'''
   print("Qué producto desea ver?") 
   print("O ingrese 'salir' para salir")
   config.guiones()
   config.actualizar_iva()
   print_nombre_productos(lista_costos)
   config.guiones()
   producto = input("Seleccion: ")
   [id_producto,fila] = manejar_vendedores.obtener_id_y_fila(lista_costos,producto)
   if (id_producto == -2):
      print ("Saliendo...")
      return -1
   if (id_producto == -1):
      print("El producto no fue encontrado. Intente nuevamente.")
      time.sleep(1)
      config.guiones()
      return generar_datos_ventas()
   
   
   producto_info = {
    "id": id_producto,
    "producto": producto,
    "costo": lista_costos[fila][2],
    "precio": lista_costos[fila][3],
    "iva": lista_costos[fila][4],
    "cantidad_vendida": lista_costos[fila][5]
}

   print(f"El producto {producto_info['producto']}")
   print(f"Tiene un id de {producto_info['id']}")
   print(f"Con un costo de {producto_info['costo']}")
   print(f"Vendido a un precio de {producto_info['precio']}")
   print(f"Con un IVA de {producto_info['iva']}")
   print(f"Se ha vendido el producto {producto_info['producto']} un total de {producto_info['cantidad_vendida']} veces.")


   config.guiones()
   time.sleep(2)
   print("Desea ver otro artículo?")
   valor = datos_de_ventas.checar_continuar()
   if (valor == -1):
      print("Saliendo..")
      return -1
   if (valor ==1):
      return generar_datos_ventas()
   if (valor ==2):
      return -1

def mostrar_estadisticas_vendedor():
   '''Muestra estadísticas de un vendedor'''
   config.guiones()
   print("De qué vendedor se desea generar estadísticas?")
   config.guiones()
   manejar_vendedores.print_nombre_vendedor()
   config.guiones()
   nombre_vendedor = input("Selección: ")
   lista_vendedores = config.recibir_archivo(manejar_vendedores.ARCHIVO_VENDEDORES)
   [id_vendedor, fila] = manejar_vendedores.obtener_id_y_fila(lista_vendedores,nombre_vendedor)
   if (id_vendedor == -2):
      print ("Saliendo...")
      return -1
   if (id_vendedor == -1):
      print("No encontrado. Intente nuevamente")
      return mostrar_estadisticas_vendedor()
   lista_ventas = config.recibir_archivo(datos_de_ventas.ARCHIVO_LISTA_VENTAS)
   lista_ventas_filtrada = datos_de_ventas.filtrar_filas_id(lista_ventas,id_vendedor)
   [cantidad, costo, precio, contribucion, iva] = obtener_cantidad_costo_precio_iva(lista_ventas_filtrada)
   config.guiones()
   print("El vendedor", nombre_vendedor)
   print("Con el id", id_vendedor)
   print("Ha vendida una cantidad de", cantidad, "artículos")
   print("Con un costo de producción de ", costo)
   print("Con un precio vendido de", precio)
   print("Con una contribución total de", contribucion)
   print("Que ha generado un iva de", iva)
   config.guiones()
   time.sleep(2)
   print("Desea ver otro vendedor?")
   valor = datos_de_ventas.checar_continuar()
   if (valor == -1):
      print("Saliendo..")
      return -1
   if (valor ==1):
      return mostrar_estadisticas_vendedor()
   if (valor ==2):
      return -1

def obtener_cantidad_costo_precio_iva(lista_ventas: list) -> list:
   '''Función que de una lista filtrada, suma y entregue en forma de lista
   la cantidad el costo el precio, contribución e iva totales de todas sus ventas'''
   suma_cantidad =0
   suma_costo = 0
   suma_precio = 0
   suma_contribucion = 0
   suma_iva =0
   for i in range(len(lista_ventas)):
      suma_cantidad += int(lista_ventas[i][1])
      suma_costo += float(lista_ventas[i][2])
      suma_precio += float(lista_ventas[i][3])
      suma_contribucion += float(lista_ventas[i][4])
      suma_iva += float(lista_ventas[i][6])
   return [suma_cantidad,suma_costo,suma_precio,suma_contribucion,suma_iva]

def seleccion_ventas (seleccion) -> int:
   '''Función para checar selección del submenú generado'''
   match seleccion:
      case 1:
         return mostrar_archivo_costos()
      case 2:
         return generar_datos_ventas()
      case 3:
         return mostrar_estadisticas_vendedor()
      case _:
         print("La selección no está en la lista")
         config.guiones()
         time.sleep(1)
         return -1
         
def print_nombre_productos(lista_costos) -> None:
   for i in range(1,len(lista_costos)):
      print(lista_costos[i][0])