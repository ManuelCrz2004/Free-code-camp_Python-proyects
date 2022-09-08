# # Concatenación de stirngs (poner strings juntos)
# # Queremos crear un string que diga "subscribete a _______"
# youtuber = "X"  # Algun valor de string

# # Maneras para hacer lo anterior
# print("subscribete a " + youtuber)
# print("subscribete a {}".format(youtuber))
# print(f"subscribete a {youtuber}")

#   Para comentar un fragmento de codigo: CTRL + K --- CTRL + C
#   Para descomentar: CTRL + U

adj = input("> Adjetivo: ")
verbo1 = input("> Verbo 1: ")
verbo2 = input("> Verbo 2: ")
persona_famosa = input("> Persona famosa: ")

madlib = f"Programación de computadores es {adj}! Me emociona todo el tiempo por que yo amo \
{verbo1}. Mantente hidratado y {verbo2} como {persona_famosa}"
    
print(madlib)