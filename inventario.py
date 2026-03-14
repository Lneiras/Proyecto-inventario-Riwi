from aspectos_visuales import *
from Funciones import *
from FAgregar import *


def menu():
    print(f"{Magenta}┌{borde_h}┐")
    print(f"│{Blanco}{"1. Agregar producto":<{Ancho}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Listar productos":<{Ancho}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Salir":<{Ancho}}{Reset}{Magenta}│")
    print(f"└{borde_h}┘{Reset}")

def main():
    print(f"{Cian}┌{bordeP}┐")
    print(f"│{Cian}{"Bienvenido al sistema de gestión de inventario":^{AnchoP}}{Reset}{Cian}│")
    print(f"└{bordeP}┘{Reset}")

    lista_inventario = []

    while True:
        menu()
        opcion = input(f"{Amarillo}Seleccione una opción: {Reset}")

        if opcion == "1": #agregar 
            limpiar_pantalla()
            print(f"{Magenta}Agregando productos{Reset}\n")
            Producto = agregar_producto()
            lista_inventario.append(Producto)
            input(f"\n{Cian}Presiona Enter para volver al menú{Reset}")
            Volviendo() #esta funcion la utilizo para darle un toque mas visual al usuario
            
        elif opcion == "2": #ver los productos
            limpiar_pantalla()
            listar_productos(lista_inventario)
            input(f"\n{Cian}Presiona Enter para volver al menú{Reset}")
            Volviendo()


        elif opcion == "3":
            salir()
            break

        else:
            print(f"{Rojo}Opción no válida. Por favor, intente nuevamente.{Reset}")

main()