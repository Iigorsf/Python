#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprèstimo será negado.

precoCasa = int(input("Digite o preço da casa: "))
salario = int(input("Digite o salário do comprador: "))
anos = int(input("Em quantos anos vai pagar: "))

mensal = precoCasa/(anos*12)
if mensal > (salario*0.3):
    print("O empréstimo bancário foi NEGADO, a mensalidade de R${:.2f} excede 30% do seu salário que é equivalente a R${:.2f}".format(mensal,(salario*0.3)))
else:
    print("O empréstimo foi APROVADO e a mensalidade é de R${:.2f}".format(mensal))