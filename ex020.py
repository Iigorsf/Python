#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

var1 = input("Nome do primeiro alunos: ")
var2 = input("Nome do segundo alunos: ")
var3 = input("Nome do terceiro alunos: ")
var4 = input("Nome do quarto alunos: ")

lista = [var1, var2, var3, var4]
shuffle(lista)

print('A ordem de apresentação será: ', lista)

