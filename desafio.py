# https://www.youtube.com/watch?v=fA3CTGpPVvA
import random as rd #biblioteca para gerar números aleatorios

n_prisioneiros = int(input("Digite o numero de prisioneiros: "))
lmp_estado = False # false, ela esta apagada (lampada)
prisioneiros_escolhidos = []
dias = 0
pr_contador = rd.randint(0,n_prisioneiros)
print("Prisioneiro contador", pr_contador)
tentativas = 0
while True:
    print()

    escolhido = rd.randint(1, n_prisioneiros)
    dias += 1
    print("Escolhido: ", escolhido)

    if pr_contador == escolhido:
        if len(prisioneiros_escolhidos) == n_prisioneiros - 1:
            print("Contador! Todos ja passaram pela sala!")
            break
        print("Contador escolhido")
        if lmp_estado:
            lmp_estado = False
            print("lâmpada apagada")
        continue

    if escolhido not in prisioneiros_escolhidos:
        if lmp_estado:
            print("Lâmpada ja estava acesa")
        else:
            print("Prisioneiro", escolhido," acendeu a lâmpada")
            lmp_estado = True
            prisioneiros_escolhidos.append(escolhido)
    else:
        print(escolhido, "Ja acendeu a lampada")


######################################
print("Dias",dias)
prisioneiros_escolhidos.sort()
print(prisioneiros_escolhidos)
