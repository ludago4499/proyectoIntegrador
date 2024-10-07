import config
import time
archivo_inventario = "Inventario.csv"
def is_correcta_seleccion (seleccion) -> int:
   # regresa la seleccion normal si es válida. 
   # regresa un -1 si no es válida
   # regresa un -2 para salir
   try:
            seleccion = int(seleccion)  
   except ValueError:
            if (not seleccion == 'salir'):
               print("Hubo un error en su selección. Verifique nuevamente.")  # mensaje de error
               time.sleep(1)
               return -1
            else:
                return -2
   
   if (seleccion <= 0):
      print("El número seleccionado debe ser mayor a 0. ")    
      time.sleep(1)
      return -1
      
   return seleccion

def buscar_id(nombre,lista) -> list:
   # Luis González
   # regresa un -1 si no se encuentra
   # regresa un -2 para salir
   # regresa una lista -> [id,num_fila]

   if (nombre == 'salir'):
       return [-2,0] # salir

   for i in range(1,len(lista)):
      if (lista[i][0] == nombre):
        return [lista[i][1],i] # se regresa el id y la fila en donde está
   return [-1,0] # no se encontró

def llegada_articulos () -> None:
    # regresa un -1 para salir
    def print_columna(lista,num_columna)-> None:
       for i in range(1,len(lista)): # evita el título
          print(lista[i][num_columna])
        
    flag = True
    lista = config.recibir_archivo(archivo_inventario)
    
    while (flag):
      flag = False
      print("Qué artículo(s) han llegado?")
      print("O ingrese 'salir' para salir.")
      print_columna(lista,0)
      seleccion = input("Selección: ")
      [id,row] = buscar_id(seleccion,lista)
      if (id == -1):
         print("No se encontró")
         time.sleep(1)
         flag = True
      elif (id ==-2):
          return -1 #salir
      print("Se seleccionó", seleccion)
      
    flag = True
    while (flag):
      flag = False
      print( "Cuánto ha llegado? Exprese su respuesta como un número únicamente. ")
      print(lista[row][3])
      seleccion = input("Seleccion: ") # el resultado debe ser mayor a 0
      seleccion = is_correcta_seleccion(seleccion)
      if (seleccion == -1):
         flag = True
      else:
         # si ambas selecciones son válidas se cambia el archivo del inventario
         lista[row][2] = seleccion + int (lista[row][2])
         cambiar_articulo(lista)
         print("Se ha realizado con éxito. Se regresa al menú principal.")
         time.sleep(1)
         return -1


# este método actualiza el inventario
def cambiar_articulo (lista) -> None:
   archivo_inventario = "Inventario.csv"
   config.actualizar_archivo(archivo_inventario,lista)
