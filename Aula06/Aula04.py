
Peso = float(input("Digite o seu peso"))
Altura = float(input("Digite sua altura"))

Imc = Peso/(Altura*Altura)

if Imc < 18.6:
        print("Abaixo do peso")

elif Imc >= 18.6 < 24.9:
        print("Peso ideal, parabéns!")

elif Imc >= 25.0 < 29.9:
        print("Levemente acima do peso")

elif Imc >= 30.0 < 34.9:
        print("Obesidade Grau 1")

elif Imc >= 35.0 < 39.9:
        print("Obesidade Grau 2 (severa)")

else:
    print("Obesidade grau 3 (mórbida)")

print(f"O seu Imc será : {Imc}")
