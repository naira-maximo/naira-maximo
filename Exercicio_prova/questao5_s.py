'''Escreva um algoritmo que calcule a seguinte sequência, fornecendo como saída o resultado de S,
dada a respectiva entrada do usuário (sem utilizar vetor):
2. S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... (+/-)n/(n*n), sendo n um número inteiro e positivo >= 50 informado pelo usuário,'''

# Ler o número informado pelo usuário para a sequência S
print('\n2) S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... (+/-)N/(N*N)')
sequencia = 0
n = int(input('Insira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
if n >= 5:  # Condição para N (número inteiro e positivo >= 50)
    for numero in range(1, n+1):
        calculo = numero/(numero*numero)
        print(f'Resultado do {numero}º cálculo da sequência: {calculo}')
        if numero % 2 == 0: # Se o número for par, subtrair na sequência
            sequencia -= calculo
        else:  # Se o número for ímpar, somar na sequência
            sequencia += calculo
    print(f'O resultado de S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... (+/-)N/(N*N), sendo N = {n}, é {sequencia}')
else:
    print(f'O número {n} não é compatível com N')  # Se o número informado for < 50