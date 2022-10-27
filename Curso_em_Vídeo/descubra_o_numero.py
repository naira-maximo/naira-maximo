from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador sortear um nº e salvar na memória
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)  # Pausa a execução em 3 segundos 
if jogador == computador:
    print(f'\nPARABÉNS! Você conseguiu me vencer! Eu também pensei no número {jogador}\n')
else:
    print(f'\nGANHEI! Eu pensei no número {computador} e não no {jogador}\n')