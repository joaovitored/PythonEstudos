Nome = input("Seu nome")
Idade = input("Sua idade")
Salario = float(input("digite seu salario"))
PorcentagemAumento = float(input("Informe o acrescimo"))
cash = (Salario * PorcentagemAumento) / 100
SalarioAtualizado = Salario+cash
print(f"Seu nome é {Nome}, sua idade é {Idade} e o seu salário é {Salario}")
print(f"E seu aumento será {SalarioAtualizado}")