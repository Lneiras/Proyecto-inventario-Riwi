from Funciones.aspectos_visuales import *
import csv
import os

lista_inventario = [] #esta es la lista donde se guardan a manera de diccionario los articulos

productos_csv = os.path.join('Docs', 'productos.csv')

def guardar_inventario(lista_inventario):
    limpiar_pantalla()
    creado = os.path.isfile(productos_csv)  
    with open(productos_csv, 'w', newline='', encoding='utf-8') as archivo:
        columnas = ["nombre", "cantidad", "precio"]
        Escribe = csv.DictWriter(archivo, fieldnames=columnas)
        
        Escribe.writeheader() # Solo escribe encabezados
        Escribe.writerows(lista_inventario)
        print(f"{Verde}Información guardada con éxito{Reset}")

'''En esta función utilizamos 'os.path.join' para definir dónde va a estar el archivo; se utiliza 'os' para que funcione sin importar el sistema operativo.
Utilizamos 'with' para que el archivo se cierre una vez que dejemos de usarlo, 'W' para guardarlo como un archivo nuevo y 'utf-8' para que soporte 
Caracteres especiales. Con 'creado = os.path.isfile(Inventario_csv)' verificamos si el archivo ya existe; si no existe, se creará y se agregarán las 'columnas' 
con los encabezados'''

def cargar_inventario(lista_inventario):
    limpiar_pantalla()
    try:
        with open(productos_csv, "r", encoding="utf-8") as archivo: 
            lector = csv.DictReader(archivo)
            for fila in lector:
                nombre = fila['nombre']
                precio= float(fila["precio"])
                cantidad= int(fila["cantidad"])
                existe = False
                for i in lista_inventario:
                    if i['nombre'].lower() == nombre.lower():
                        existe = True
                        break
                if not existe:
                    print(f"{Verde}Información agregada con éxito{Reset}")
                    lista_inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                
    except FileNotFoundError: #Con esto si el archivo no existe el programa no se rompe
        print(f"{Azul}No hay un archivo para cargar{Reset}")
        pass #Si el archivo no existe aún, no hace nada

'''En esta función utilizamos 'r' para leer el archivo que vamos a cargar, que en este caso agregara la información que contenga a la lista propia del sistema
para que podamos trabajar en los productos, esta función tiene un 'for' para validar si ya existe el producto y de esta manera no agregar varias veces el mismo
producto. '''