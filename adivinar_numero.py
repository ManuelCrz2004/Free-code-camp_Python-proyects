# Programa el cual genere un numero al azar y este sea adivinado por el ususario
import random


def programa_azar(x):
    numero_azar = random.randint(1, x)
    numero_elegido = 0
    contador = 0
    
    comprobacion = False

    while comprobacion == False:
        numero_elegido = int(input(" > Ingrese su opción a elegir: "))
        
        if numero_azar == numero_elegido:
            print(f"Correcto! Adivinaste el numero en un total de {contador} intentos.")
            comprobacion = True
            break
        elif numero_azar > numero_elegido:
            print("Incorrecto! El numero es mayor")
            contador += 1
        elif numero_azar < numero_elegido:
            print("Incorrecto! El numero es menor")
            contador += 1
            
if __name__ == "__main__":
    x = int(input("> Ingrese el numero limite para adivinar (Este debe ser mayor que 1): "))
    programa_azar(x)
            
            
    
