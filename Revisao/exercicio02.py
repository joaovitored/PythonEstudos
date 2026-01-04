import random

numerosecret = random.randint(1,100)

variavel= None
while variavel!=numerosecret:

    variavel= int(input("Adivinhe um numero de 0 a 100:"))

    if variavel==numerosecret:
            print("Numero correto")

    elif variavel < numerosecret:
            print(f"O numero é maior que {variavel} ")

    else:
           print(f"o numero é maior que {variavel}")
