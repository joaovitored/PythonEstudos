Quantidade = 0
for x in range (1,10,1):
    num = int(input("Digite o numero"))
    if num <0:
        print("numero negativo")
        Quantidade+=1

print(f"A quantidade de valores negativos são {Quantidade}")