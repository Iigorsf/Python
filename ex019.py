#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

var1 = input("Nome do primeiro alunos: ")
var2 = input("Nome do segundo alunos: ")
var3 = input("Nome do terceiro alunos: ")
var4 = input("Nome do quarto alunos: ")

lista = [var1, var2, var3, var4]
sorteado = choice(lista)

print("O nome do escolhido é ", sorteado)