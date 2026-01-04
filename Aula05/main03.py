numeroalunos= int(input("quantos alunos está na sala"))
contagem = 1
soma=0

while contagem <= numeroalunos:
        nota= float(input(f"digite a nota do aluno {contagem}"))
        soma+=nota
        contagem+=1
media= soma/numeroalunos

print("a média será :", media)
      