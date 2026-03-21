from Funciones.aspectos_visuales import *
from Funciones.FAgregar import *
from Funciones.Mostrar import *
from Funciones.Estadísticas import *
from Funciones.Otras_funciones import *


def menu():
    print(f"{Magenta}┌{bordeC}┐")
    print(f"│{Blanco}{"1. Agregar producto":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Mostrar inventario":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Calcular estadísticas":<{AnchoC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"4. Salir":<{AnchoC}}{Reset}{Magenta}│")
    print(f"└{bordeC}┘{Reset}")

def main():
    print(f"\n{Azul}Bienvenido al sistema de inventario{Reset}")

    lista_inventario = [] #esta es la lista donde se guardan a manera de diccionario los articulos

    Salir = ""

    while Salir != "si": #con este while salir evitamos usar el break para finalizar 
        menu()
        opcion = input(f"{Blanco}\nIngresa la opción deseada: ")

        if opcion == "1": #Esta opción nos lleva a ejecutar la función de agregar producto
            Producto = agregar_producto()
            lista_inventario.append(Producto) #Con esta función se agrega el producto a lista_inventario
            Volviendo()
        
        elif opcion == "2": #Con esta opción se muestran los articulos guardados en lista_inventario
            Cargando()
            Mostrar_inventario(lista_inventario)
            input(f"\n{Amarillo}Presiona Enter para volver al menú{Reset}") 
            Volviendo()
            #Con el input hacemos que el usuario vuelva al menú de manera interactiva 
            #con la función volviendo le damos un toque visual al usuario
        
        elif opcion == "3": #En esta opción se calculan las estadisticas (HU de esta semana)
            Cargando() #Esto es un toque visual para el usuario
            Calcular_estadísticas(lista_inventario)
            input(f"\n{Amarillo}Presiona Enter para volver al menú{Reset}")
            Volviendo()

        elif opcion == "4":
            Salir = Salir = input(f"\n{Amarillo}Deseas salir del programa?: {Reset}").strip().lower()
            if Salir == "si":
                salir()
            else:
                Volviendo()
            ''' En esta parte nos ayuda a confirmar que el usuario quiere salir. 
            Al escribir "si" se cierra el while; si escribe otra cosa, con el "else" vuelve al menú, 
            evitando que el programa se cierre o bloquee por el error de tipeo.'''
            
        else:
            print(f"{Rojo}\nError: Opción invalida, intente de nuevo{Reset}")

main()



''' En esta historia de usuario se agrega la parte de calcular estadisticas,
para saber la cantidad total de unidades agregadas al inventario y el valor total del mismo.
En esta semana he decidido separar todas las funciones en un archivo dedicado, 
esto para que se pueda revisar y cambiar sin afectar a otras funciones.
También se han aplicado funciones que mejoran el aspecto y se han aplicado colores, 
esto con la idea de mejorar la parte visual del programa y que el usuario lo vea más claro.
'''