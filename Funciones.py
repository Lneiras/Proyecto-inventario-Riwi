from aspectos_visuales import *

def listar_productos(inventario): #ver los productos del inventario
    if not inventario:
        print("\nEl inventario está vacío.")
        return

    LineaL = "lista de productos"
    print(f"{bordeL}")
    print(f"{Verde}{LineaL:^{AnchoL}}{Reset}")
    print(f"{bordeL}")
    print(f"{'Nombre':<16} | {'Cant.':<7} | {'Precio U.':<10} | {'Total':<10}")
    print(f"{bordeL}")
    
    for p in inventario:
        total = p['cantidad'] * p['precio']  #esta funcion calcula el valor total de todas las unidades del producto
        print(f"{p['nombre']:<16} | {p['cantidad']:<7} | ${p['precio']:<9.2f} | ${total:<9.2f}")



def salir(): #funcion de salida
    limpiar_pantalla()
    import time
    print("Saliendo...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()
    lineasalida = "Gracias por usar el sistema de gestión de inventario"
    print(f"{Azul}┌{bordeP}┐")
    print(f"│{lineasalida:^{AnchoP}}│")
    print(f"└{bordeP}┘{Reset}")
