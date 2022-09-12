import random

# Planeacion proyecto:
    
#     Se pide al usuario su opcion. (lista)
#     Se genera la seleccion random (Lista)
#     Se comparan entre si (lista)
#     Se da el resultado (Lista)

# funcion para pedir al ususario seleccionde piedra, papel o tijera
def user_input():
    print(f"Bienvenido a piedra, papel o tijera Usuario")
    
    user = input("> Ingrese su opción:\n(1) Piedra\n(2) Papel\n(3) Tijera\n>>>")
    
    if user == "1":
        user = "Piedra"
        return user
    elif user == "2":
        user = "Papel"
        return user
    elif user == "3":
        user = "Tijera"
        return user
    else:
        print("Su petición no fue reconocida.")
        user_input()    

# funcion para generar un elemento al azar
def random_selection():
    lista = ["Piedra", "Papel", "Tijera"]
    seleccion_maquina = random.choices(lista ,weights = [1, 1, 1], cum_weights = None, k = 1)
    seleccion_maquina = seleccion_maquina[0]
    return seleccion_maquina

# funcion para comparar respuestas
def comparar_inputs(usuario, maquina):
    # Si:
    #     piedra gana a tijera
    #     tijera gana a papel
    #     papel ganaa tijera
    #     Iguales entre si, empatan
    
    resultado = ''
    opciones = ["Piedra", "Papel", "Tijera"]
    contador_u = 0
    contador_m = 0
    c = 0
    
    for i in opciones:
        if (usuario == opciones[c]) and (maquina == opciones[c]):
            print("Hay un empate")
        c += 1
    
    # Victorias de la maquina
    if (usuario == opciones[0]) and (maquina == opciones[1]):
        print("Gana maquina")
        contador_m += 1
    elif (usuario == opciones[1]) and (maquina == opciones[2]):
        print("Gana maquina")
        contador_m += 1
    elif (usuario == opciones[2]) and (maquina == opciones[0]):
        print("Gana maquina")
        contador_m += 1
        
    # Victorias del usuario
    if (usuario == opciones[1]) and (maquina == opciones[0]):
        print("Gana usuario")
        contador_u += 1
    elif (usuario == opciones[2]) and (maquina == opciones[1]):
        print("Gana usuario")
        contador_u += 1
    elif (usuario == opciones[0]) and (maquina == opciones[2]):
        print("Gana usuario")
        contador_u += 1
     
     
    # Devolver el marcador final    
    contador_u = str(contador_u)
    contador_m = str(contador_m)    
    
    print(f"El marcador quedo:\n maquina: {contador_m} vs usuario: {contador_u}")   

def ciclo_rondas():
    n_veces = int(input("> Ingrese el número de rondas que desea jugar: "))
    contador = 0
    
    while n_veces > contador:
        user_inp = user_input()
        random_chs = random_selection()
        
        comparar_inputs(user_inp, random_chs)
        contador += 1

if __name__ == "__main__":  
    ciclo_rondas()