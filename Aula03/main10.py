hora1= int(input("digite a hora 1: "))
minuto1= int(input("digite o minuto 1: "))
hora2= int(input("digite a hora 2: "))
minuto2= int(input("digite o minuto 2: "))


somaHora= hora1+hora2
finalminuto= minuto1+minuto2
resto=0
#setar o horário em 24 horas se ultrapassar as 12
if somaHora > 24:
    fimhora = somaHora - 24
    somaHora = fimhora

elif somaHora > 12:
    fimhora = somaHora - 12
    somaHora = fimhora

#setar ajustar o horário para o formato de 12 horas
else:
        if finalminuto >59:
            fimminuto = finalminuto %60
            finalminuto = fimminuto

#converter minutos adicionais em horas
if finalminuto >= 60:
    finalminuto= finalminuto % 60
    somaHora= somaHora + 1

print(f"Hora {somaHora} , Minuto {finalminuto}")