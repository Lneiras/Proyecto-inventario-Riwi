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
|2. Listar productos|_Se listan los productos agregados_|
|3. Salir|_Cierra el programa_|

> _El programa cuenta con la información del **costo total** que multiplica la cantidad del producto por el precio unitario_

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

1. Agregar productos

 - En esta función podrás agregar el nombre del producto (solo letras).
 - La cantidad del producto (solo números mayores a cero).
 - El precio del producto (solo números mayores a cero).

2. Listar productos

 - En esta opción se listarán todos los artículos que agregaste en la opción anterior y se mostrará el valor total, que corresponde a la multiplicación de la cantidad por el precio unitario.

3. Salir

 - Esta opción cierra el programa.


## Estructura del proyecto

```
Inventario/
- inventario.py             # Punto de entrada, menú principal
- FAgregar.py               # Función agregar
- Funciones.py              # Otras funciones 
- aspectos_visuales.py      # funciones y detalles para la visualización del usuario
- README.md
```

