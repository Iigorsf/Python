#A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: Sênior
#Acima: Master

from datetime import date

nascimento = int(input("Digite o ano de nascimento do atleta: "))

data_atual = date.today()
ano = data_atual.year

categoria = ano - nascimento

if categoria < 10 :
    print("O atleta com {} anos é da categoria MIRIM".format(categoria))
elif categoria < 15:
    print("O atleta com {} anos é da categoria INFANTIL".format(categoria))
elif categoria < 20:
    print("O atleta com {} anos é da categoria JUNIOR".format(categoria))
elif categoria < 26:
    print("O atleta com {} anos é da categoria SÊNIOR".format(categoria))
else:
    print("O atleta com {} anos é da categoria MASTER".format(categoria))