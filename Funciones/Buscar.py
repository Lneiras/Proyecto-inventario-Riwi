from Funciones.aspectos_visuales import *
from Funciones.Archivos import *

def Busqueda(lista_inventario,Productos_buscado):

    for Producto in lista_inventario:
            if Producto["nombre"].lower() == Productos_buscado:
                return Producto
    return None        
''' Con esta función separamos la logica de la busqueda
De esta manera puede ser utilizada en las funciones
Buscar producto, actualizar producto y eliminar producto'''

def Buscar_producto(lista_inventario):
    Cargando()
    limpiar_pantalla()
    if not lista_inventario: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nEl inventario está vacío.{Reset}")
        return
    
    while True: 
        LineaB = "Busqueda de productos"
        print(f"{bordeM}")
        print(f"{Verde}{LineaB:^{AnchoM}}{Reset}")
        print(f"{bordeM}")

        Productos_buscado = input("\nIngrese el nombre del producto (o escribe 'salir' para volver al menú): ").strip().lower()
        '''El nombre del producto se ingresa utilizando strip() y lower() para que se pueda buscar sin importar si el usuario utiliza mayúsculas 
        o deja espacios antes o después del nombre'''

        if Productos_buscado == "salir": 
            print(f"\n{Amarillo}Búsqueda cancelada.{Reset}")
            break 
        #Esta parte sirve para que la búsqueda pueda detenerse en cualquier momento si el usuario no encuentra el producto
        
        Producto = Busqueda(lista_inventario,Productos_buscado)
        #Aquí llamamos la función Búsqueda para que se ejecute y mostramos el resultado de esa búsqueda en esta función
        if Producto :
            print(f"{bordeC}")
            print(f"{Verde}¡Producto localizado!{Reset}")
            print(f"{bordeC}")
            print(f"Nombre:   {Producto['nombre']}")
            print(f"Precio:   ${Producto['precio']:,}")
            print(f"Cantidad: {Producto['cantidad']} unidades")
            print(f"{bordeC}")              
            return

        else:
            print(f"\n{Rojo}Error: El producto '{Productos_buscado}' no existe.{Reset}")
            print("Inténtalo de nuevo...\n")

    '''En esta parte utilizamos el if para imprimir el resultado de la busqueda si la función (Busqueda) encuentra el producto
    y utilizamos else para que si no hay coincidencia vuelva a preguntar'''


'''En esta función utilizamos un while para que el ciclo de buscar se realice hasta de manera indefinida,
hasta que el usuario desee salir debido a no encontrar el producto buscado o que la opción se cierre al encontrarlo.
En esta función utilizamos también la función Búsqueda para encontrar el producto que se mostrara con esta función'''