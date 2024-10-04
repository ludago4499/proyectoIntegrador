import csv # utilizado para trabajar con archivos csv

# Archivo para actualizar, modificar y cambiar archivos

def recibir_archivo(filename) -> list:
    # recibe el nombre de la ubicación del archivo y 
    # retorna un arreglo con los datos del archivo
    with open(filename, 'r') as file: # read only
        data_list = []
        reader = csv.reader(file)
        for row in reader: # Cada fila del archivo
           stripped_row = [element.strip() for element in row] 
           if any(stripped_row): # checa si hay elemento despues de hacer strip() | Evita empty rows
                data_list.append(stripped_row) # Agrega la lista a la lista
    return data_list

def actualizar_archivo(filename, archivo)-> None: # el arhcivo es una lista de listas
    # Se recibe el nombre de la ubicación del archivo junto con el arreglo 
    # y se actualiza el archivo
    
    with open(filename,mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(archivo)

    return archivo

def add_row(archivo, fila):
    archivo.append(fila)
    return archivo

# checar is el usuario quiere salir, regresar un -1 si sí
def checar_salir(message):
    if message.lower() == 'salir':
        return -1 # return -1 case
    else:
        return # empty return

def actualizar_iva():
    filename = "costos_y_precios.csv"
    lista =  recibir_archivo(filename) # recibe el archivo
    for i in range(1,len(lista)):
        lista[i][4] = round(float(lista[i][3]) * (0.16) / 1.16 ,2)
    # actualiza el archivo nuevamente
    actualizar_archivo(filename,lista)


# testing below


actualizar_iva()