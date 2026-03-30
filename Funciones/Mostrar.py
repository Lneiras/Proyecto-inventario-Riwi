from Funciones.aspectos_visuales import *

def Mostrar_inventario(inventario):
    limpiar_pantalla()
    if not inventario: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nEl inventario está vacío.{Reset}")
        return
    
    #Esto es un aspecto visual que hace que el inventario se muestre en forma de lista
    LineaL = "lista de productos"
    print(f"{bordeM}")
    print(f"{Verde}{LineaL:^{AnchoM}}{Reset}")
    print(f"{bordeM}")
    print(f"{'Nombre':<16} | {'Cant.':<7} | {'Precio U.':<10} | {'Total':<10}")
    print(f"{bordeM}")

    #En esta parte hacemos que se busque toda la información guardada en el inventario
    for p in inventario:
        total = p['cantidad'] * p['precio']  #esta funcion calcula el valor total de todas las unidades del producto
        print(f"{p['nombre']:<16} | {p['cantidad']:<7} | ${p['precio']:<9.2f} | ${total:<9.2f}")
        #Esta parta hace que la información se muestre en formato de lista
