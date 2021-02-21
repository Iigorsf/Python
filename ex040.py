#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a media atingida:
#média abaixo de 5: reprovado
#média entre 5e 6.9:recuperação
#média 7 ou superio: aprovado

nota = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota + nota2)/2

if media < 5:
    print("A média final do ano foi {}: REPROVADO".format(media))
elif media < 7 and media >= 5:
    print("A média final do ano foi {}: RECUPERAÇÂO".format(media))
elif media >= 7:
    print("A média final do ano foi {}: APROVADO".format(media))