#Escreva um programa que converta uma temperatura digita em °C e converta para ° F

celsius = int(input('What is the temperature in degrees: '))

fahrenheit = (celsius*(9/5))+32

print('The temperature of {}°Celsius in Fahrenheit is {}°'.format(celsius, fahrenheit))