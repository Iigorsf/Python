#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome separadamente.

#nome = str(input("Digite um nome: "))

#print("Primeiro nome= {}".format(nome[:(nome.find(' '))]))
#print("Último nome= {}".format(nome[(nome.rfind(' ')):]))

n = str(input("Digite um nome: "))
nome = n.split()

print("Primeiro nome= {}".format(nome[0]))
print("Último nome= {}".format(nome[len(nome)-1]))