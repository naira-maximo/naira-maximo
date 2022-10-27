# A diferença entre um contador e um acumulador é que os contadores o valor adicionado é constante e, nos acumuladores, variável
# • Cálculo da soma de dez números inteiros
n = 1
soma = 0
while n <= 10:
    x = int(input(f'Digite o {n}º número: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {soma}')

# • Calcule a média de 10 números inteiros
n = 1
soma = 0
while n <= 10:
    x = int(input(f'Digite o {n}º número: '))
    soma = soma + x
    n = n + 1
print(f'Média: {soma/10:.2f}')

# • Calcule o fatorial de dez
i = 1
fat = 1
while i <= 10:
    fat = fat * i
    i = i + 1
print(f'Fat(10) = {fat}')

# Calcule o fatorial de um número inteiro n
i = 1
fat = 1
n = int(input('Digite n: '))
while i <= n:
    fat = fat * i
    i = i + 1
print(f'Fat({n}) = {fat}')