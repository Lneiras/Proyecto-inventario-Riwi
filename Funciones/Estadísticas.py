from Funciones.aspectos_visuales import *

def Calcular_estadísticas(inventario):
    limpiar_pantalla()

    if not inventario: #Si el usuario consulta esta opción sin tener productos en el inventario se mostrara ese mensaje
        print(f"{Azul}\nEl inventario está vacío.{Reset}")
        return

    LineaE = "Mostrando Estadísticas"
    print(f"{bordeM}")
    print(f"{Verde}{LineaE:^{AnchoM}}{Reset}")
    print(f"{bordeM}")
    
    '''En esta parte se agregan contadores que inician en cero y dos puntos de referencia para poder comparar y buscar los valores máximos.
    Los contadores inician en cero y se le suman todas las unidades registradas y el valor total de los productos registrados hasta el momento de consulta.
    Los puntos de referencia inician con el primer valor de la lista para poder comparar, si el siguiente valor es mayor será reemplazado y así hasta llegar al mayor.'''

    Total_unidades_I = 0 
    valor_total_I = 0
    Producto_mas_caro_I = inventario[0]
    Producto_con_mas_stock_I = inventario[0]

    for p in inventario: #Esta parte recorre el inventario realizando la búsqueda de la información solicitada
        Total_unidades_I += p["cantidad"]  
        valor_total_I += (p["cantidad"] * p["precio"]) 
        
        if p["precio"] > Producto_mas_caro_I["precio"]:
            Producto_mas_caro_I = p

        if p["cantidad"] > Producto_con_mas_stock_I["cantidad"]:
            Producto_con_mas_stock_I = p

    #Esta parte busca las unidades y su valor realizando la multiplicación para saber el valor total de todo el inventario
    print(f"\n{Blanco}La cantidad de unidades ingresadas es: {Total_unidades_I}{Reset}")
    print(f"\n{Blanco}El valor total del inventario es: ${valor_total_I}{Reset}")
    print(f"\n{Blanco}El producto mas caro del inventario es {Producto_mas_caro_I['nombre']} con un precio de ${Producto_mas_caro_I['precio']:,}{Reset}")
    print(f"\n{Blanco}El producto con mas stock del inventario es {Producto_con_mas_stock_I['nombre']} con {Producto_con_mas_stock_I['cantidad']:,} unidades{Reset}")
    return Total_unidades_I, valor_total_I, Producto_con_mas_stock_I, Producto_mas_caro_I