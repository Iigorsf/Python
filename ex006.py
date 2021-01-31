#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz
num = int(input('Digite um número: '))
print("O dobro do número {0} é {1}, o triplo é {2} e a raiz é {3}".format(num, (num * 2), (num * 3), (num ** (1 / 2))))