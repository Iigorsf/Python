#Faça um progrmama que leia a largura e a altura de uma parede em metros, calucele a sua área e aquantidade de tinta necessãria para pintá-la, sabendo que casa litro de tinta pinta uma área de 2m².
import math

width = float(input('Type the wall width: '))
height = float(input('Type the wall height: '))

size = width*height

print('Para pintar {} é necessário {} litros de tinta'.format(size, math.ceil(size/2)))