#En este archivo se definen funciones que ayudan con el aspecto visual para el programa

#Los colores se definen aquí para no agregarlos en cada archivo de manera individual

#colores
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"

'''Esta parte es para determinar valores para agregar cuadros a la parte visual del usuario
sin tener que agregar esa información en cada archivo de manera individual'''


#Dimensiones
AnchoC = 35    #recuadros cortos
bordeC = "─" * AnchoC
AnchoM = 55    #recuadros medianos
bordeM = "─" * AnchoM
AnchoL = 80   #recuadros largos
bordeL = "─" * AnchoL
AnchoP = 100  #Recuadros para la lista de coders
bordeP = "─" * AnchoP

import os

#Esta función nos ayuda a que el sitema no se vea demasiado cargado para el usuario
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


#Estas funciones un toque visual para el usuario

def Volviendo():
    input(f"\n{Amarillo}Presiona Enter para volver al menú{Reset}")
    import time
    print("\nVolviendo...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()

def Agregando():
    limpiar_pantalla()
    import time
    print("\nAgregando...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()
    print(f"{Verde}\nInformación agregada con éxito{Reset}")

def Cargando():
    limpiar_pantalla()
    import time
    print("\nCargando...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()

def Saliendo():
    limpiar_pantalla()
    import time
    print("\nSaliendo...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()

def Regresando():
    limpiar_pantalla()
    import time
    print(f"{Azul}Regresando...{Reset}")
    time.sleep(1)  # Pausa de 1 segundo
    limpiar_pantalla()