# Programa el cual genere un numero al azar y este sea adivinado por el ususario
import random


def usuario_adivina(x):
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

def computador_adivina(x):
    num_bajo = 1
    num_alto = x
    respuesta = ''
    contador = 0
    
    while respuesta != 'c':
        if num_bajo != num_alto:
            numero_azar = random.randint(num_bajo, num_alto)
            
        respuesta = input(f"> Es {numero_azar} muy alto [A], muy bajo [B] o correcto [C]: ")
        
        if respuesta == 'c' or 'C':
            print(f"Excelente! Adivinaste en un total de {contador} intentos")
        elif respuesta == 'a' or 'A':
            num_alto = respuesta + 1
            contador += 1
            return num_alto
        elif respuesta == 'b' or 'B':
            num_bajo = respuesta - 1
            contador += 1
            return num_bajo

if __name__ == "__main__":
    x = int(input("> Ingrese el numero limite para adivinar (Este debe ser mayor que 1): "))
    computador_adivina(x)
            
            
    
