#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

distancia = int(input("Digite a distância em km da viagem: "))

if distancia <= 200:
    print("O preço da passagem é R${}".format(distancia*0.5))
else:
    print("O preço da passagem é R${}".format(distancia*0.45))