from aspectos_visuales import *

def salir(): #Función de salida, encargada de cerrar el programa
    Saliendo()
    lineasalida = "Gracias por usar el sistema de gestión de inventario"
    print(f"{Azul}┌{bordeP}┐")
    print(f"│{lineasalida:^{AnchoP}}│")
    print(f"└{bordeP}┘{Reset}")
