from Funciones.aspectos_visuales import *
from Funciones.Archivos import *
from Funciones.Buscar import Busqueda
from Funciones.Otras_funciones import menu_actualizacion

#nombre = el nombre del producto a actualizar

def Actualizar_producto(lista_inventario):
    limpiar_pantalla()

    if not lista_inventario: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nEl inventario está vacío.{Reset}")
        return

    LineaAC = "Actualización de productos"
    print(f"{bordeM}")
    print(f"{Verde}{LineaAC:^{AnchoM}}{Reset}")
    print(f"{bordeM}")

    while True: 
        nombre = input("\nIngrese el nombre del producto (o escribe 'salir' para volver al menú): ").strip().lower()

        if nombre == "salir":
            print(f"\n{Amarillo}Actualización cancelada{Reset}")
            break

        Producto = Busqueda(lista_inventario,nombre)

        if Producto is None:
            limpiar_pantalla()
            print(f"\n{Rojo}Error: El producto '{nombre}' no existe.{Reset}")
            continue
        
        print(f"\n{Verde}El producto '{nombre}' fue encontrado.{Reset}")
        print(f"\nSeleciona la actualización que deseas realizar o salir para volver al menú")
        
        Salir = ""

        while Salir != 1 :
            opcion_Actualizar = menu_actualizacion()

            if opcion_Actualizar == "1":
                Exit = ""
                while Exit != 1 :
                    print(f"\n{Magenta}Estas actualizando la cantidad del producto {Producto}{Reset}")
                    
                    nueva_cantidad = input(f"\n{Cian}Ingresa la nueva cantidad: {Reset}").strip()
                    
                    if not nueva_cantidad.isdigit() or int(nueva_cantidad) <= 0:
                        print(f"{Rojo}Error: La cantidad debe ser un número positivo.{Reset}")
                        continue
                    
                    Producto["cantidad"] = int(nueva_cantidad)
                    limpiar_pantalla()

                    lineaCa = f"Cantidad de '{Producto['nombre']}' actualizada a {nueva_cantidad} unidades"
                    print(f"{Verde}┌{bordeP}┐")
                    print(f"│{Blanco}{lineaCa:^{AnchoP}}{Reset}{Verde}│")
                    print(f"└{bordeP}┘{Reset}")
                    Exit = 1


            elif opcion_Actualizar == "2":
                Cancelar = ""
                while Cancelar != 1 :
                    print(f"\n{Magenta}Estas actualizando el precio del producto {Producto}{Reset}")

                    try:
                        nueva_precio = float (input(f"\n{Cian}Ingresa la nueva cantidad: {Reset}"))
                        
                    except ValueError:
                        print(f"{Rojo}Error: La cantidad debe ser un número positivo.{Reset}")
                        continue
                        
                    if nueva_precio <=0:
                        print(f"{Rojo}La cantidad debe ser un número positivo.{Reset}")
                        continue

                    Producto["precio"] = (nueva_precio)
                    limpiar_pantalla()

                    lineaPr = f"El precio del '{Producto['nombre']}' actualizado a ${nueva_precio}"
                    print(f"{Verde}┌{bordeP}┐")
                    print(f"│{Blanco}{lineaPr:^{AnchoP}}{Reset}{Verde}│")
                    print(f"└{bordeP}┘{Reset}")
                    Cancelar = 1                

            elif opcion_Actualizar == "3":
                print(f"\n{Amarillo}Actualización Terminada{Reset}")
                Salir = 1
            else:
                print(f"{Rojo}Error: opción no valida, intenta de nuevo{Reset}")
                continue