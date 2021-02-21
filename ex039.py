#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa tambpem deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

data_atual = date.today()
ano = data_atual.year

nascimento = int(input("Digite seu ano de nascimento: "))

alistar = ano - nascimento

if alistar < 18:
    print("Quem nasceu no ano de {} deve se alistar em {} anos".format(nascimento, (18-alistar)))
elif alistar == 18:
    print("Quem nasceu no ano de {} está na hora de se alistar ".format(nascimento))
else:
    print("Quem nasceu no ano de {} passou do prazo de se alistar em {} anos".format(nascimento, (alistar-18)))