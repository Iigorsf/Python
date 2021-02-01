#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#dolar a R$5,46
n = float(input('Quanto você tem na carteira: '))
print('Você pode comprar {:.2f} dólares'.format(n/5.46))