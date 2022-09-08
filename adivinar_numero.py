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
    limite_menor = 1
    limite_mayor = x
    respuesta = ''
    resultado = False
    intentos = 0

    while resultado == False:

        numero_azar = random.randint(limite_menor, limite_mayor)

        respuesta = int(input(f"> ¿Es {numero_azar} mayor (1), menor (2) o igual (0) al numero que tiene en mente?\t> "))

        if respuesta == 1:
            limite_mayor = numero_azar - 1
            intentos += 1
        elif respuesta == 2:
            limite_menor = numero_azar + 1
            intentos +=1
        elif respuesta == 0:
            print(f"Felicidades! La computadora lo resolvio en un total de {intentos} intentos")
            resultado = True
        else:
            print("No se entendio tu petición")
            pass



    # Esta respuesta no fue usada, ya que el codigo no tiene un correcto funcionamiento

    # while respuesta != 'c':

    #     new_numero_azar = numero_azar
            
    #     respuesta = input(f"> Es {new_numero_azar} mayor [A], menor [B] o correcto [C]: ")
        
    #     if respuesta == 'c' or 'C':
    #         print(f"Excelente! Adivinaste en un total de {contador} intentos")
    #     elif respuesta == 'a' or 'A':
    #         num_alto = respuesta - 1
    #         numero_azar = random.randint(num_bajo, num_alto)
    #         contador += 1

    #         return numero_azar
    #     elif respuesta == 'b' or 'B':
    #         num_bajo = respuesta + 1
    #         numero_azar = random.randint(num_bajo, num_alto)
    #         contador += 1

    #         return numero_azar

    # Esta respuesta no fue usada, ya que el codigo no tiene un correcto funcionamiento

if __name__ == "__main__":
    x = int(input("> Ingrese el numero limite para adivinar (Este debe ser mayor que 1): "))
    computador_adivina(x)
            
            
    
