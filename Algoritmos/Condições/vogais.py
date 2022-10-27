# • Faça um programa que leia uma palavra e troque as vogais por “*” usando for
palavra = input('Palavra: ')
troca = ''
for letra in palavra:
    if letra in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + letra
print(f'Nova palavra: {troca}')