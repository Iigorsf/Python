#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input("Escolha um número inteiro: "))
print('''Escolha a base de conversão:
 [ 1 ] para BINÁRIO
 [ 2 ] para OCTAL
 [ 3 ] para HEXADECIMAL''')
escolha = int(input("Escolha: "))
if escolha == 1:
    print("{} convertendo para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertendo para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("{} convertendo para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Você selecionou uma base de conversão não existente")