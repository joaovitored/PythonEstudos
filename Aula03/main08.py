Combustivel= input("Digite o tipo de combustivel: E or e: Etanol ou G ou g:Gasolina")
Litros =float(input("Digite a quantidade de litros"))

if Combustivel == "E" or "e":

    total = Litros*4.90

elif Combustivel == "G" or "g":


    total = Litros*5.80


print(f"O valor total de litros foi de {Litros} e o valor foi de:{total}")

