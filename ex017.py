#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calculete e mostr o comprimento da hipotenusa

catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))

hipot = ((catop**2)+(catad**2))**(1/2)

print("A hipotenusa de um triângulo retângulo com o cateto oposto igual a {} e o cateto adjacente igual a {} é {}".format(catop, catad, hipot))