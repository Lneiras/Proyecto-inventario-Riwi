from aspectos_visuales import *


def agregar_producto():
    limpiar_pantalla()
    print(f"{Magenta}\nAgregando Productos{Reset}")
    while True:
        producto = input(f"{Azul}Ingresa el producto que deseas agregar: {Reset}").strip() 
        #strip() elimina los espacios vacios al inicio y al final del texto
        #con este if hacemos que el nombre del producto sea valido(no numeros, no simbolos, no espacios vacios)
        if not producto.replace(" ", "").isalpha() or len(producto) == 0:  
        #replace() elimina los espacion mientras se realiza la validación 
        # isalpha() verifica que el texto solo contenga letras y len() verifica que el texto no este vacio
            limpiar_pantalla()
            print(f"{Rojo}Error: El nombre que intentas agregar no es valido.{Reset}")
        else:
            limpiar_pantalla()
            lineaA1 = f"El producto {producto} ha sido agregado exitosamente"
            print(f"{Verde}┌{bordeP}┐")
            print(f"│{Blanco}{lineaA1:^{AnchoP}}{Reset}{Verde}│")
            print(f"{Verde}└{bordeP}┘")
            break
    while True:
        Cantidad = input(f"\n{Cian}Ingresa la cantidad del producto: {Reset}").strip()
        #aquí hacemos que la cantidad sea un numero mayor a cero
        if not Cantidad.isdigit() or int(Cantidad) <= 0:
            limpiar_pantalla()
            print(f"{Rojo}Error: La cantidad debe ser un número positivo.{Reset}")
        else:
            limpiar_pantalla()
            lineaA2 = f"Se ha agregado la cantidad de {Cantidad} del producto {producto}"
            print(f"{Verde}┌{bordeP}┐")
            print(f"│{Blanco}{lineaA2:^{AnchoP}}{Reset}{Verde}│")
            print(f"{Verde}└{bordeP}┘")
            break
    while True:
        try:
            #Utilizamos float para que se puedan agregar numeros que pueden tener decimales
            #el decimal se agrega con .
            Precio = float(input(f"\n{Amarillo}Ingresa el precio del producto: {Reset}").strip())
        except ValueError:
            limpiar_pantalla()
            print(f"{Rojo}Error: El precio debe ser un número.{Reset}")
            continue
        if Precio <= 0:
            limpiar_pantalla()
            print(f"{Rojo}Error: El precio debe ser mayor a cero.{Reset}")
            continue
        #Con el try/excep y el if nos aseguramos que el valor agregado sea un numero mayor a cero
        else:
            limpiar_pantalla()
            lineaA3 = f"Se ha agregado el precio con éxito."
            print(f"{Verde}┌{bordeP}┐")
            print(f"│{Blanco}{lineaA3:^{AnchoP}}{Reset}{Verde}│")
            print(f"{Verde}└{bordeP}┘")
            Agregando()
            lineaA4 = f"El producto {producto} ha sido agregado al inventario."
            print(f"{Verde}┌{bordeP}┐")
            print(f"│{Blanco}{lineaA4:^{AnchoP}}{Reset}{Verde}│")
            print(f"{Verde}└{bordeP}┘")
            break
    return {"nombre": producto, "cantidad": int(Cantidad), "precio": Precio}