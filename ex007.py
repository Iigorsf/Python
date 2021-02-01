#Desenvolva um programa que leia as duas notas de um aluno calcule e mostre a sua média
n1= float(input('Primeira nota do aluno: '))
n2= float(input('Segunda nota do Aluno: '))
res= (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2 , res))