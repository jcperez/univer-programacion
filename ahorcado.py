palabra = "UNIVER"
juego   = ['*'] * len(palabra) 
while True:
    letra = input("Ingresa una letra: ")
    i = 0
    while i < len(palabra):
        if palabra[i] == letra:
            juego[i] = letra
        i = i + 1
    print(juego)