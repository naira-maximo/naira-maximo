# Crie um algoritmo que leia um vetor de 30 números inteiros e gere um segundo vetor cujas posições pares são o dobro do vetor original e as ímpares o triplo.

# Desenvolva um algoritmo que permita a leitura de um vetor de 30 números inteiros e gere um segundo vetor com os mesmos dados, so que de maneira invertida, 
# ou seja, o primeiro elemento ficará na última posição, o segundo na penúltima e assim por diante.

números = []

for i in range(30):
    números.append(int(input(f'Insira o {i+1}º número inteiro: ')))
print(números)
print(str(números.sort()))