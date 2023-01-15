'''Escreva um único algoritmo que calcule as seguintes sequências, fornecendo como saída o resultado de H, S e P,
dadas as respectivas entradas do usuário (sem utilizar vetor):
1. H = 1/1 + 3/2 - 5/3 + 7/4 - ... (+/-) (n*2-1)/n, sendo n um número inteiro e positivo >= 50 informado pelo usuário;
2. S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... (+/-)n/(n*n), sendo n um número inteiro e positivo >= 50 informado pelo usuário; e
3. P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ..., onde n corresponde ao número de termos da sequência,
sendo um número inteiro e positivo >= 50 informado pelo usuário (pot equivale a potenciação)'''

# Ler o número informado pelo usuário para a sequência H
print('1) H = 1/1 + 3/2 - 5/3 + 7/4 - ... (+/-) (N*2-1)/N')
sequencia = 0
n = int(input('Insira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
if n >= 5:  # Condição para N (número inteiro e positivo >= 50)
    for numero in range(1, n+1):  # Para cada número na sequência de 1 até o número informado pelo usuário
        calculo = (numero*2-1)/numero
        if numero % 2 == 0 or numero == 1:  # Se o número for par, somar na sequência. O primeiro termo é impar (1), mas não é negativo.
            sequencia += calculo
        else:  # Se o número for ímpar, subtrair na sequência
            sequencia -= calculo
    print(f'O resultado de H, sendo N = {n}, é {sequencia}')
else:
    print(f'O número {n} não é compatível com N')  # Se o número informado for < 50

# Ler o número informado pelo usuário para a sequência S
print('\n2) S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... (+/-)N/(N*N)')
sequencia = 0
n = int(input('Insira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
if n >= 5:  # Condição para N (número inteiro e positivo >= 50)
    for numero in range(1, n+1):
        calculo = numero/(numero*numero)
        if numero % 2 == 0: # Se o número for par, subtrair na sequência
            sequencia -= calculo
        else:  # Se o número for ímpar, somar na sequência
            sequencia += calculo
    print(f'O resultado de S, sendo N = {n}, é {sequencia}')
else:
    print(f'O número {n} não é compatível com N')  # Se o número informado for < 50

# Ler o número informado pelo usuário para a sequência P
print('\n3) P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ...')
soma = 0
primo = 1
impar = 1
n = int(input('Insira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
if n >= 5:  # Condição para N (número inteiro e positivo >= 50)
    for i in range(n): # Sequência de 0 até o número que o usuário escolheu -1 (n termos)
        verificador = 0  # Verificador de permanência do while (identificou um número primo)
        while verificador == 0:
            divisores = 0
            primo = primo + 1
            for divisor in range(1, primo + 1):
                if primo % divisor == 0:
                    divisores = divisores + 1
            if divisores == 2:  # Todo número primo é divisível por 1 e por ele mesmo. Portando, 2 divisores = primo. (exceto 1)
                verificador = 1  # Encerra o while
        soma += (primo/(impar**3)) 
        impar = impar + 2
    print(f'O resultado de P, sendo N = {n}, é {soma}')
else:
    print(f'O número {n} não é compatível com N')  # Se o número informado for < 50