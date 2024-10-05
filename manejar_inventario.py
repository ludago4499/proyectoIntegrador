import config
import time

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

def buscar_id(nombre,lista) -> int:
   # Luis González
   # regresa un -1 si no se encuentra
   # regresa un -2 para salir

   if (nombre == 'salir'):
       return -2 # salir

   for i in range(1,len(lista)):
      if (lista[i][0] == nombre):
        return lista[i][1]
   return -1 # no se encontró

def llegada_articulos () -> None:
    # regresa un -1 para salir
    def print_columna(lista,num_columna)-> None:
       for i in range(1,len(lista)): # evita el título
          print(lista[i][num_columna])
        
    flag = True
    archivo_inventario = "Inventario.csv"
    lista = config.recibir_archivo(archivo_inventario)
    
    while (flag):
      flag = False
      print("Qué artículo(s) han llegado?")
      print("O ingrese 'salir' para salir.")
      print_columna(lista,0)
      seleccion = input("Selección: ")
      id = int(buscar_id(seleccion,lista))
      if (id == -1):
         print("No se encontró")
         time.sleep(1)
         flag = True
      elif (id ==-2):
          return -1 #salir
          flag = True
      else:
        
        print("Se seleccionó", seleccion)
        print( "Cuánto ha llegado? Exprese su respuesta como un número únicamente. ")
        print(lista[id][3])
        seleccion = input("Seleccion: ") # el resultado debe ser mayor a 0
        seleccion = is_correcta_seleccion(seleccion)
        if (seleccion == -1):
            flag = True
        else:
            # si ambas selecciones son válidas se cambia el archivo del inventario
            lista[id][2] = seleccion + int (lista[id][2])
            cambiar_articulo(lista)


# este método actualiza el inventario
def cambiar_articulo (lista) -> None:
   archivo_inventario = "Inventario.csv"
   config.actualizar_archivo(archivo_inventario,lista)

llegada_articulos()