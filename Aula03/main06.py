N1=float(input(f"Digite a primeira nota"))
N2=float(input(f"digite a segunda nota"))
N3=float(input(f"digite a terceira nota"))

media=(N1+N2+N3)/3

if media>=7.0:
    print(f"aprovado. a média sera: {media:2f}")
else:
    if media < 4.0:
        print(f"nao aprovado. Aluno em recuperaçao, media: {media:2f}")

    print(f"reprovado. sua media foi: {media:2f}")

