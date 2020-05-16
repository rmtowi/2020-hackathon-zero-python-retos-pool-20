from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    global options
    
    player = player.lower()
    ai = ai.lower()

    if player == "piedra" and ai == "piedra":
        return "Empate!"
    elif player == "piedra" and ai == "papel":
        return "Perdiste!"
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"
    elif player == "papel" and ai == "papel":
        return "Empate!"
    elif player == "papel" and ai == "tijeras":
        return "Perdiste!"
    elif player == "tijeras" and ai == "piedra":
        return "Perdiste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"
    elif player == "tijeras" and ai == "tijeras":
        return "Empate!"
    else:
        return "Error en escritura"


# Entry Point
def Game():
    #
    #
    
    #
    #
    global options
    player = input("Selecciona piedra, papel o tijeras: ")
    numero_random=randint(0,2)
    ai=options[numero_random]
    #print("AI escogió: " + ai)
   
    winner = quienGana(player, ai)

    print(winner)

#Game()