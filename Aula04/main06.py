quantidade=0
quantidadeinvalida= 0
for x in range (11):
    num=int(input(f"11Digite o valor:"))

    if num >=10 and num <=20:
        quantidade =  quantidade+1

    else:
        quantidadeinvalida= quantidadeinvalida+1


print(f"Valores dentro {quantidade}, valores fora {quantidadeinvalida}")





