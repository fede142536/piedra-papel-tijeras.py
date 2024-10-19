nombre1 = input("Ingresa tu nombre jugador1: ")
nombre2 = input("Ingresa tu nombre jugador2: ")

jugador1 = input("Jugador1 elige entre piedra, papel o tijeras: ")
jugador2 = input("Jugador2 elige entre piedra, papel o tijeras: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

intentos = 0
cant_maxima = 5
intentos +=1
while intentos < cant_maxima and not condicion1 or condicion2 or condicion3:
    if jugador1 == jugador2:
        print("Ha sido un empate")
    elif (condicion1) or (condicion2) or (condicion3):
        print("Ganaste", nombre1)
    else:
        print("Ganaste", nombre2)

print("Superaron los 5 intentos")


