#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

town = str(input("Digite o nome da cidade: ")).strip()

if 'SANTO' == town[:5].upper():
    print("A cidade {} começa com Santo.".format(town))
else:
    print("A cidade {} NÃO começa com Santos.".format(town))