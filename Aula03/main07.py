Time1=input("Fale o nome do primeiro time")
Time2=input("Fale o nome do segundo time")

Gols1=input("Digite o numero de gols do primeiro time")
Gols2=input("digite o numero de gols do segundo time")

if Gols1>Gols2:
    print(f"Time1 Vencedor, contagem de gols:{Gols1}")
else:
     if Gols2>Gols1:
        print(f"Time2 Vencedor, contagem de gols: {Gols2}")

     else:
            print("Houve um empate entre os times")