#Crie um Programa que leia o nome de uma pessoa e diga se ela tem "SILVA' no nome

nome = str(input("Digite um nome: ")).upper()

if (nome.find('SILVA')) != -1:
    print("O nome {} tem SILVA".format(nome))
else:
    print("O nome {} NÃO tem SILVA".format(nome))