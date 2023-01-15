# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
from math import trunc


print('Olá, viajante!')
km = float(input('Insira a distância que irá percorrer (em km): '))
km_h = float(input('Insira a velocidade média esperada para a sua viagem (km/h): '))
h = km/km_h
print(f'O tempo esperado para a sua viagem de {km:.0f}km, com uma velocidade média esperada de {km_h:.0f}km/h, é de {h:.2f} horas.')
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.