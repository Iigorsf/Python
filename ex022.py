# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo(sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
nome.split()

print('O nome com todas as letras maiúsculas: ', nome.upper())
print('O nome com todas as letras minúsculas: ', nome.lower())
print('Quantas letras ao todo(sem considerar espaços):',(len(nome) - nome.count(' ')))
print('Quantas letras tem o primeiro nome.', nome.find(' '))
