from Funciones.aspectos_visuales import *
from Funciones.Archivos import *
from Funciones.Buscar import Busqueda

#nombre = el nombre del producto a Eliminar

def Eliminar_producto(lista_inventario):
    limpiar_pantalla()

    if not lista_inventario: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nEl inventario está vacío.{Reset}")
        return

    LineaEL = "Eliminación de productos"
    print(f"{bordeM}")
    print(f"{Verde}{LineaEL:^{AnchoM}}{Reset}") 
    print(f"{bordeM}")

    '''En este while encerramos en un bucle el input del nombre de producto que el usuario desea eliminar
    de esta manera nos aseguramos que el programa no se cierre si por un error de tipeo del usuario.
    Si el usuario desea salir solo tiene que escribir el texto salir en lugar del nombre de un producto, esto romperá el while y volverá al menú
    En esta función también utilizamos la función Búsqueda para buscar el producto
    si la función retorna None el programa mostrara el mensaje de que el producto no existe'''

    while True:

        nombre = input("\nIngrese el nombre del producto (o escribe 'salir' para volver al menú): ").strip().lower()

        if nombre == "salir":
            print(f"\n{Amarillo}Eliminación cancelada{Reset}")
            break

        Producto = Busqueda(lista_inventario,nombre)

        if Producto is None:
            limpiar_pantalla()
            print(f"\n{Rojo}Error: El producto '{nombre}' no existe.{Reset}")
            continue
        
        print(f"\n{Verde}El producto '{nombre}' fue encontrado.{Reset}")
        

        #En este while se confirma la eliminación del producto, aquí el usuario puede cancelar la eliminación sin cerrar el programa

        salir = ""

        while salir != 1:

            Eliminar = input(f"\n{Amarillo}Confirma si deseas eliminar este producto (Si/No):  {Reset}").strip().lower()

            if Eliminar == "si":
                lista_inventario.remove(Producto)
                print(f"\n{Rojo}Producto eliminado{Reset}")
                return
            
            elif Eliminar == "no":
                print(f"\n{Amarillo}Eliminación cancelada{Reset}")
                salir = 1

            else:
                print(f"\n{Rojo}Error: opcion invalida, intenta de nuevo{Reset}")
                continue