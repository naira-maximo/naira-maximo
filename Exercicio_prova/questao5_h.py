'''Escreva um algoritmo que calcule a seguinte sequência, fornecendo como saída o resultado de H,
dada a respectiva entrada do usuário (sem utilizar vetor):
1. H = 1/1 + 3/2 - 5/3 + 7/4 - ... (+/-) (n*2-1)/n, sendo n um número inteiro e positivo >= 50 informado pelo usuário;'''

# Ler o número informado pelo usuário para a sequência H
print('1) H = 1/1 + 3/2 - 5/3 + 7/4 - ... (+/-) (N*2-1)/N')
sequencia = 0
n = int(input('Insira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
if n >= 5:  # Condição para N (número inteiro e positivo >= 50)
    for numero in range(1, n+1):  # Para cada número na sequência de 1 até o número informado pelo usuário
        calculo = (numero*2-1)/numero
        print(f'Resultado do {numero}º cálculo da sequência: {calculo}')
        if numero % 2 == 0:  # Se o número for par, somar na sequência
            sequencia += calculo
        else:  # Se o número for ímpar, subtrair na sequência
            sequencia -= calculo
    print(f'O resultado de H = 1/1 + 3/2 - 5/3 + 7/4 - ... (+/-) (N*2-1)/N, sendo N = {n}, é {sequencia}')
else:
    print(f'O número {n} não é compatível com N')  # Se o número informado for < 50