from aspectos_visuales import *

def Calcular_estadísticas(inventario):
    limpiar_pantalla()
    print(f"{Magenta}\nMostrando estadísticas{Reset}")
    
    '''en esta función los contadores inician en cero, si el usuario consulta sin tener articulos agregados se mostrara en cero'''

    Total_unidadesI = 0 
    valor_totalI = 0

    for p in inventario: #esta parte recorre el inventario realizando la busqueda de la información solicitada
        Total_unidadesI += p["cantidad"] #Esta parte suma todas las unidades agregadas al contador arrojando el total 
        valor_totalI += (p["cantidad"] * p["precio"]) 
    #Esta parte busca las unidades y su valor realizando la multiplicación para saber el valor total de todo el inventario
    print(f"\n{Blanco}La cantidad de unidades ingresadas es: {Total_unidadesI}{Reset}")
    print(f"\n{Blanco}El valor total del inventario es: ${valor_totalI}{Reset}")
    return Total_unidadesI, valor_totalI