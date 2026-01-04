pin=123456
erro=3
while erro>0:
    tentativa = int(input("Digite sua senha"))
    if tentativa == pin:
        print("Senha correta, acesso garantido!")
        break
    else:
        erro-=1
        print("senha incorreta")
        if erro<=0:
            print("Conta bloqueada!")


