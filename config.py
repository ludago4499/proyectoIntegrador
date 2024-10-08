import csv # utilizado para trabajar con archivos csv
import time

# Archivo para actualizar, modificar y cambiar archivos

def recibir_archivo(filename: str) -> list:
    # recibe el nombre de la ubicación del archivo y 
    # retorna un arreglo con los datos del archivo
    # Luis González
    with open(filename, 'r', encoding='utf-8-sig') as file: # read only, encodificador latin-1 para incluir acentos
        data_list = []
        reader = csv.reader(file)
        for row in reader: # Cada fila del archivo
           stripped_row = [element.strip() for element in row] 
           if any(stripped_row): # checa si hay elemento despues de hacer strip() | Evita empty rows
                data_list.append(stripped_row) # Agrega la lista a la lista
    return data_list

def actualizar_archivo(filename: str, archivo: list)-> None: # el arhcivo es una lista de listas
    # Se recibe el nombre de la ubicación del archivo junto con el arreglo 
    # y se actualiza el archivo
    # Luis González
    
    with open(filename,mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(archivo)


def add_row(archivo, fila):
    # Luis González
    archivo.append(fila)
    return archivo



def actualizar_iva():
    # Luis González
    filename = "costos_y_precios.csv"
    lista =  recibir_archivo(filename) # recibe el archivo
    for i in range(1,len(lista)):
        lista[i][4] = round(float(lista[i][3]) * (0.16) / 1.16 ,2)
    # actualiza el archivo nuevamente
    actualizar_archivo(filename,lista)
# imprime guiones para hacer más claro hacia el usuario
def guiones()-> None:
    # Luis González
    print("-----------------")

# automatiza el check de si quiere salir el usuario

def desea_salir(texto) -> bool:
    # Luis González
    if texto ==  'salir' or texto == 'cancelar':
        return True
    else:
        return False
    
def checar_seleccion (seleccion) -> int:
    # regresa -1 si contiene algún error
    # regresa -2 si el usuario desea salir
    # Luis González
    try:
        seleccion = int(seleccion)
        return seleccion
    except ValueError:
        if (desea_salir(seleccion)):
            print("Saliendo ...")
            return -2
        print("Hubo un error en su selección. Verifique nuevamente.")
        time.sleep(1)
        return -1


