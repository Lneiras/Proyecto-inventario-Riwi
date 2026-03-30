# Inventario

Este proyecto es un programa simple de gestión de inventario desarrollado en Python.
La aplicación permite registrar productos ingresando el nombre del producto, la cantidad y el precio.

El sistema guarda los productos registrados y permite visualizar la lista de productos agregados. También incluye una opción para salir del programa.

## Diagrama de flujo

![This is an alt text.](https://raw.githubusercontent.com/Lneiras/Inventario/refs/heads/main/Diagrama%20de%20flujo.png.png)

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
|1. Agregar producto|_Se agregan los productos_|
|2. Mostrar inventario|_Se listan los productos agregados_|
|3. Buscar producto|_Se realiza la búsqueda de un producto especifico_|
|4. Actualizar producto|_Se actualizan productos_|
|5. Eliminar producto|_Se eliminan productos_|
|6. Calcular estadísticas|_Se calculan estadísticas del inventario_|
|7. Guardar CSV|_Se guarda el archivo del inventario_|
|8. Cargar CSV|_Se carga el archivo del inventario_|
|9. Salir|_Cierra el programa_|

> _El programa cuenta con la información del **costo total** que multiplica la cantidad del producto por el precio unitario y se muestra en la función de **Mostrar inventario**_

## Requerimiento para desplegar el programa

- Tener python instalado
- Tener Git instalado
- Tener acceso a github
- Tener Visual studio code instalado (opcional)

## Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado en tu computador.
   
 > Para esto abre la terminal **(Ctrl + Alt + T)** y escribe *python --version* o *python3 --version.*
 >
 >>Si está instalado, aparecerá el número de versión (ej. Python 3.x.x).

2. Descarga o clona el repositorio del proyecto.
 - Ingresa a una terminal en tu escritorio.
 - Escribe git clone y pega este enlace del repositorio:
   
   > git clone https://github.com/Lneiras/Inventario.git
   
3. Ve a la carpeta donde se clonó el repositorio y abre una terminal desde la carpeta.
4. Para abrir el programa:
   - Escribe **code .** para abrir el proyecto en VS Code
      - Ve al archivo inventario.py y corre el archivo
   - Escribe python3 inventario.py o python inventario.py si lo quieres correr directamente en la terminal

## Cómo funciona el programa

Una vez clones el repositorio y lo abras en VSCode, ve al archivo llamado `inventario.py` para que puedas correr el programa.

Al iniciar el programa, se mostrará un menú para que veas las opciones disponibles.

![This is an alt text.](linck menú)

1. Agregar productos

 - En esta función podrás agregar el nombre del producto (solo letras).
 - La cantidad del producto (solo números mayores a cero).
 - El precio del producto (solo números mayores a cero).

2. Mostrar inventario

 - En esta opción se listarán todos los artículos que se encuentren en el inventario y la información de cantidad y precio unitario, además se mostrará el valor total, que corresponde a la multiplicación de la cantidad por el precio unitario.

3. Buscar producto

 - En esta opción realizamos la búsqueda de un producto especifico, si el producto es encontrado mostrara nombre, cantidad y precio unitario.

4. Actualizar producto

 - En esta opción realizamos la búsqueda de un producto especifico y procedemos a realizarle una _actualización_
    - Actualizar la cantidad
    - Actualizar el precio
   Si deseamos cancelar la actualización podemos tomar la opción *salir* para volver al menú

5. Eliminar producto

 - En esta opción realizamos la búsqueda de un producto especifico para eliminarlo
   Si deseamos cancelar la eliminación podemos escribir *No* en la confirmación para cancelar la eliminación y volver al menú

6. Calcular estadísticas

 - En esta función se generan las estadisticas que nos inidican lo siguiente:
    - Unidades totales dentro del inventario
    - Valor total del inventario
    - Producto mas caro 
    - Producto con mayor stock del inventario

7. Guardar CSV

 - En esta función se guarda el archivo CSV una vez que se finalice la realización de cambios o actualizaciones a los productos.

8. Cargar CSV

 - En esta función se carga el archivo CSV con el que trabajaremos utilizando las otras funciones del programa.

9. Salir

 - Esta opción cierra el programa.


## Estructura del proyecto

```
Inventario/
- inventario.py        #El motor principal del programa que gestiona el flujo del menú.
- Funciones/                #Directorio que contiene la lógica modularizada:
   - FAgregar.py               #Validación y registro de nuevos productos.
   - Mostrar.py                #Visualización formateada del inventario actual.
   - Buscar.py                 #Lógica de localización de productos con reintentos.
   - Actualizar.p              #Modificación de precios y stock.
   - Eliminar.py               #Borrado seguro de productos.
   - Estadísticas.py           #Cálculos de totales y máximos con Lambdas.
   - Aspectos_visuales.py      #Configuración de colores ANSI y diseño de cuadros.
   - Data.py  
- Docs/                    #Documentos del programa
   - Diagrama de flujo    
   - Imagen del menú principal del programa
   - Archivo csv              
```
