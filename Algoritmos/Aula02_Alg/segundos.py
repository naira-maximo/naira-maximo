# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Insira a quantidade de dias: '))
horas = int(input('Insira a quantidade de horas: '))
minutos = int(input('Insira a quantidade de minutos: '))
segundos = int(input('Insira a quantidade de segundos: '))

dias_seg = 86400 * dias
horas_seg = 3600 * horas
minutos_seg = 60 * minutos
segundos_totais = dias_seg + horas_seg + minutos_seg + segundos
print(dias_seg, horas_seg, minutos_seg)
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos correspondem a {segundos_totais} segundos no total.')