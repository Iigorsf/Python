#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantida de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

traveled = float(input("Enter the distance traveled: "))
rented = int(input("how many days was it rented for? "))

price = (traveled*0.15) + (rented*60)

print("O preço a se pagar por {} km percorridos e o aluguel de {} dias é de R${}".format(traveled, rented, price))