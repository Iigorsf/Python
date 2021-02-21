#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input("Escreva o salário do funcionário: R$"))

if salario > 1250:
    print("O aumento do funcionário com o salario de R${} será de R${:.2f}".format(salario, (salario*0.10)))
else:
    print("O aumento do funcionário com o salario de R${} será de R${:.2f}".format(salario,(salario*0.15)))