import menuPrincipal
import config
# Código Principal
def main():

    menuPrincipal.desplegar_menu_principal()
    seleccion = input("Seleccion: ")
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return
    seleccion = menuPrincipal.seleccion_menu_principal(seleccion) # checa si hay un error (-1)
        
    if (seleccion == -1):
        main()

main()


