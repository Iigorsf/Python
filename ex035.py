#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

n1 = float(input("Digite o comprimento da primeira reta: "))
n2 = float(input("Digite o comprimento da segunda reta: "))
n3 = float(input("Digite o comprimento da terceira reta: "))

if n1 < (n2+n3) and n1 > (n2-n3):
    print("As retas de comprimentos {}, {}, {} podem formar uma Triângulo".format(n1, n2, n3))
elif n2 < (n1+n3) and n2 > (n1-n3):
    print("As retas de comprimentos {}, {}, {} podem formar uma Triângulo".format(n1, n2, n3))
elif n3 < (n1+n2) and n3 > (n1-n2):
    print("As retas de comprimentos {}, {}, {} podem formar uma Triângulo".format(n1, n2, n3))
else:
    print("As retas de comprimentos {}, {}, {} NÂO podem formar uma Triângulo".format(n1, n2, n3))