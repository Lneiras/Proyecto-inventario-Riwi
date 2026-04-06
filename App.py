from Funciones.aspectos_visuales import *
from Funciones.FAgregar import *
from Funciones.Mostrar import *
from Funciones.Estadísticas import *
from Funciones.Otras_funciones import *
from Funciones.Archivos import *
from Funciones.Buscar import *
from Funciones.Actualizar import *
from Funciones.Eliminar import *


def main():
    limpiar_pantalla()
    print(f"\n{Azul}Bienvenido al sistema de inventario{Reset}\n")

    Salir = ""

    while Salir != "si": #Con este while salir evitamos usar el break para finalizar
        opcion = menu()

        if opcion == "1": #Esta opción nos lleva a ejecutar la función de agregar producto
            Producto = agregar_producto(lista_inventario)
            lista_inventario.append(Producto) #Con esta función se agrega el producto a lista_inventario
            Regresando()
        
        elif opcion == "2": #Con esta opción se muestran los articulos guardados en lista_inventario
            Cargando()
            Mostrar_inventario(lista_inventario)
            Volviendo() #con la función volviendo le damos un toque visual al usuario
            
        
        elif opcion == "3":
            Buscar_producto(lista_inventario)            
            Volviendo()

        elif opcion == "4":
            Actualizar_producto(lista_inventario)
            Volviendo()         

        elif opcion == "5":
            Eliminar_producto(lista_inventario)        
            Volviendo()

        elif opcion == "6": #En esta opción se calculan las estadisticas (HU de esta semana)
            Cargando() #Esto es un toque visual para el usuario
            Calcular_estadísticas(lista_inventario)            
            Volviendo()

        elif opcion == "7":
            guardar_inventario(lista_inventario)
            Volviendo()         

        elif opcion == "8":
            cargar_inventario(lista_inventario)
            Volviendo()          

        elif opcion == "9":
            Salir = input(f"\n{Amarillo}Deseas salir del programa?(Si/No):  {Reset}").strip().lower()
            if Salir == "si":
                salir()
            else:
                Regresando()

            ''' En esta parte nos ayuda a confirmar que el usuario quiere salir. 
            Al escribir "si" se cierra el while; si escribe otra cosa, con el "else" vuelve al menú, 
            evitando que el programa se cierre o bloquee por el error de tipeo.'''
            
        else:
            print(f"{Rojo}\nError: Opción invalida, intente de nuevo{Reset}")

main()



''' 
HU3
En esta historia de usuario se agrega el uso de archivos CSV para la persistencia de datos
También se agregan las funciones (modularizadas) de Buscar, Actualizar y Eliminar producto.
En este HU se modifica el diagrama de flujo y se actualiza el Readme para que contenga la 
Información total del programa, además de que se agrega a la función de calcular estadísticas.
La parte de ver el producto más caro y el producto con más stock del inventario.
'''