'''Elabore um algoritmo que leia 150 números inteiros e imprima:
* A) Qual o tamanho da maior sequência consecutiva de números em ordem crescente, assumindo como critério de desempate a soma dos números;
* B) Qual o tamanho da maior sequência consecutiva de números constantes, assumindo como critério de desempate o valor_b do número envolvido na sequência.'''

# Variáveis de A
anterior_a = 1  # Armazena o último número para comparação
contador_a = 1  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior_a + 1)
contador2_a = 0  # Soma armazenada para comparação com a contagem vigente
soma_a = 0  # Soma da contagem vigente, para possível desempate
soma2_a = 0  # Soma armazenada para comparação com a contagem vigente
# Variáveis de B
anterior_b = 0  # Armazena o último número para comparação
contador_b = 0  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior_b + 1)
contador2_b = 0  # Soma armazenada para comparação com a contagem vigente
valor_b = 0  # Número da contagem vigente, para possível desempate
valor2_b = 0  # Número armazenado para comparação com a contagem vigente

for i in range(0, 10):
    numero = int(input('Insira um número inteiro: '))
    # Resolução de A
    if numero == anterior_a + 1 and numero != 1:
        contador_a += 1
        if soma_a == 0:  # Sem essa função, o primeiro número da sequência consecutiva é desprezado 
            soma_a += (numero + anterior_a)
        else:
            soma_a += numero
    else:
        if contador_a > contador2_a:  # Armazena a maior sequência como forma de comparação 
            contador2_a = contador_a
            contador_a = 1
            soma2_a = soma_a
            soma_a = 0
        elif contador_a == contador2_a:  # Caso existam duas sequências iguais,
            if soma_a > soma2_a:         # a maior soma_a precisa ser armazenada até o final do for
                soma2_a = soma_a
                soma_a = 0
                contador2_a = contador_a
                contador_a = 1
            else:
                contador_a = 1
                soma_a = 0
        else:
            contador_a = 1
            soma_a = 0
    anterior_a = numero
    # Resolução de B
    if numero == anterior_b:
        if contador_b == 0:  # Sem essa função, a contagem fica com 1 a menos
            contador_b += 2
            valor_b = numero
        else:
            contador_b += 1
            valor_b = numero
    else:
        if contador_b > contador2_b:  # Armazena a maior sequência como forma de comparação 
            contador2_b = contador_b
            contador_b = 0
            valor2_b = valor_b
            valor_b = 0
        elif contador_b == contador2_b:  # Caso existam duas sequências iguais,
            if valor_b > valor2_b:       # o maior valor_b (numero repetido) precisa ser armazenado até o final do for
                valor2_b = valor_b
                valor_b = 0
                contador_b = 0
            else:
                contador_b = 0
        else:
            contador_b = 0
            valor_b = 0
    anterior_b = numero

# Condições para a resposta
if contador_a >= contador2_a:
    if soma_a >= soma2_a:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador_a}, tendo {soma_a} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador_a}, tendo {soma2_a} como a soma dos termos')
elif contador2_a > contador_a:
    if soma_a >= soma2_a:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2_a}, tendo {soma_a} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2_a}, tendo {soma2_a} como a soma dos termos')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador_a} e {contador2_a}')

# Condições para a resposta
if contador_b > contador2_b:
    print(f'A maior sequência consecutiva de números constantes é {contador_b}, sendo uma sequência de número {valor_b}')
elif contador2_b > contador_b:
    print(f'A maior sequência consecutiva de números constantes é {contador2_b}, sendo uma sequência de número {valor2_b}')
elif contador_b == contador2_b:
    if valor_b >= valor2_b:
        print(f'A maior sequência consecutiva de números constantes é {contador_b}, sendo uma sequência de número {valor_b}')
    elif valor_b < valor2_b:
        print(f'A maior sequência consecutiva de números constantes é {contador_b}, sendo uma sequência de número {valor2_b}')
else:
    print(f'Não houve sequência consecutiva de números constantes, sendo a contagem {contador_b} e {contador2_b}')

