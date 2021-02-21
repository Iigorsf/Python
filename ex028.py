#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelao computador

from random import randint

num = int(input("Tente descobrir um número de 0 a 5 que o computador está pensando: "))
escolha = randint(0,5)
print("\033[1;31;43mPROCESSANDO...\033[m")
if escolha == num:
    print("Ele pensou no número {} você VENCEU".format(escolha))
else:
    print("Ele pensou no número {} você PERDEU".format(escolha))