#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

ang = float(input("Digite o ângulo que você deseja: "))

rad = float(radians(ang))
sen = sin(rad)
cos = cos(rad)
tang = tan(rad)

print('O ângulo {:.2f}° tem o radiano de {:.2f}rad, o seno de {:.2f}, o cos de {:.2f} e a tangente de {:.2f}'.format(ang, rad, sen, cos, tang))