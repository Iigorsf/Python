#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

from math import floor

num = int(input("Digite um número de 0 a 9999: "))

print("unidade: ", (num%10))
print("Dezena: {}".format(floor((num%100 - num%10)/10)))
print("centena: {}".format(floor((num%1000)/100)))
print("milhar: {}".format(floor(num/1000)))