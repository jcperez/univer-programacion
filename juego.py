import random
tablero = [0] * 9
i = 0
while i < 3:
    print(tablero[0], tablero[1], tablero[2])
    print(tablero[3], tablero[4], tablero[5])
    print(tablero[6], tablero[7], tablero[8])
    print("=======")
    lugar = int(input("Jugador 1 - Que lugar?"))
    tablero[lugar] = 1
    lugar = int(input("Jugador 2 - Que lugar?"))
    tablero[lugar] = 2
    i = i + 1
