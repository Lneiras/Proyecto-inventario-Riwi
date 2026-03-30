from Funciones.aspectos_visuales import *

def menu(): #Menú principal del programa
    
    print(f"{Magenta}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Agregar producto":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Mostrar inventario":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Buscar producto":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"4. Actualizar producto":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"5. Eliminar producto":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"6. Calcular estadísticas":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"7. Guardar CSV":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"8. Cargar CSV":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"9. Salir":<{AnchoC}}{Reset}{Magenta}│")
    print(f"└{bordeC}┘{Reset}")

    
    opcion = input(f"{Blanco}\nIngresa la opción deseada: ")
    return opcion


def salir(): #Función de salida, encargada del mensaje de cierre del programa
    Saliendo()
    lineasalida = "Gracias por usar el sistema de gestión de inventario"
    print(f"\n{Azul}┌{bordeP}┐")
    print(f"│{lineasalida:^{AnchoP}}│")
    print(f"└{bordeP}┘{Reset}\n")

def menu_actualizacion(): #Menú secundario que se despliega en la función de actualizar producto del programa
    print(f"{Cian}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Actualizar cantidad":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"2. Actualizar precio":<{AnchoC}}{Reset}{Cian}│")
    print(f"│{Blanco}{"3. Salir":<{AnchoC}}{Reset}{Cian}│")
    print(f"└{bordeC}┘{Reset}")
    
    opcion_Actualizar = input(f"{Blanco}\nIngresa la opción deseada: ")
    return opcion_Actualizar