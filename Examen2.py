def funcionA(frase):
    w = input()
    state = frase.contains("hola")
    if(state):
        print("Hola mundo")
    else:
        print("asd")

frase = input()
funcionA(frase)
