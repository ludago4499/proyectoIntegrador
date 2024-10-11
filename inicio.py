import menuPrincipal
import config

def main() -> None:
# Código Principal
    menuPrincipal.desplegar_menu_principal()
    seleccion = input("Seleccion: ")
    seleccion = config.checar_seleccion(seleccion)
    if (seleccion == -2):
        return
    seleccion = menuPrincipal.seleccion_menu_principal(seleccion) # checa si hay un error (-1)
        
    if (seleccion == -1):
        main()

main()


