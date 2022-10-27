# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas;
# * O nome com todas minúsculas;
# * Quantas letras ao todo (sem considerar espaços);
# * Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('-'*22)
print('Analisando seu nome...')
print('-'*22)
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
num = int(input('Insira um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

# Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

