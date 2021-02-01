#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
med = float(input('Uma distância em metros: '))
cm = med * 100
mm = med * 1000
print('A medida de {}m é igual a {:.0f}cm e {:.0f}mm'.format(med, cm, mm))