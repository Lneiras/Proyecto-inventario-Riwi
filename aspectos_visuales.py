#En este archivo se definen funciones auxiliares para el programa

#colores
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"

#Dimensiones
Ancho = 35
borde_h = "─" * Ancho
AnchoP = 70
bordeP = "─" * AnchoP
AnchoL = 50
bordeL = "─" * AnchoL

import os

#esta funcion nos ayuda a que el sitema no se vea demasiado cargado para el usuario
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')



def Volviendo():
    import time
    print("\nVolviendo...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    limpiar_pantalla()