import menuPrincipal
import time

# Código Principal
def main():
    flag = True # condicion while

    # While para la primera selección
    while (flag):

        menuPrincipal.desplegar_menu_principal()
        seleccion = input("Seleccion: ")
        try:
            seleccion = int(seleccion)  
            flag = False  # se sale del while
        except ValueError:
            print("Hubo un error en su selección. Verifique nuevamente.")  # mensaje de error
        time.sleep(1) # Se espera un segundo y se vuelve a repetir el while  
    valor = menuPrincipal.seleccion_menu_principal(seleccion) # checa si hay un error (-1)
    if (valor == - 1):
        main()

main()


