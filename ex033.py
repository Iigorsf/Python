#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
menor = n1
maior = n1
if n2 > n1:
    maior= n2
if n3 > n2 and n3 > n1:
    maior= n3

if n2 < n1:
    menor= n2
if n3 < n2 and n3 < n1:
    menor= n3

print("O menor número é {} e o maior é {}".format(menor,maior))