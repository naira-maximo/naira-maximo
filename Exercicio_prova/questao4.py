'''Elabore um algoritmo que leia 150 números inteiros e imprima:
* Qual o tamanho da maior sequência consecutiva de números em ordem crescente, assumindo como critério de desempate a soma dos números;
* Qual o tamanho da maior sequência consecutiva de números constantes, assumindo como critério de desempate o valor do número envolvido na sequência.'''

import random

anterior = 0
contador = 0
contador2 = 0

for i in range(0, 10):
    numero = random.randint(1, 10)
    print(numero)
    if numero == anterior + 1:
        contador += 1
        if contador > contador2:
            contador2 = contador 

print(contador)


