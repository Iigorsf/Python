#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input("Escreva a velocidade do carro: "))

if velocidade > 80:
    multa= (velocidade-80)*7
    print("O carro está acima da velocidade permite da 80km/h e foi multado em R${}".format(multa))
else:
    print("O carro está dentro da velocidade permitida. Siga com segurança")