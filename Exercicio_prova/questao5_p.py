'''Escreva um algoritmo que calcule a seguinte sequência, fornecendo como saída o resultado de P,
dadas a respectiva entrada do usuário (sem utilizar vetor):
3. P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ..., onde n corresponde ao número de termos da sequência,
sendo um número inteiro e positivo >= 50 informado pelo usuário (pot equivale a potenciação)'''

# Ler o número informado pelo usuário para a sequência P
soma = 0
primo = 1
impar = 1
n = int(input('\nInsira o valor de N, sendo um número inteiro e positivo maior ou igual a 50: '))
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
print(f'Resultado da {n}ª soma da sequência é: {soma}')