anterior = 0  # Armazena o último número para comparação
contador = 0  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior + 1)
contador2 = 0  # Soma armazenada para comparação com a contagem vigente
valor = 0  # Número da contagem vigente, para possível desempate
valor2 = 0  # Número armazenado para comparação com a contagem vigente

for i in range(0, 10):  # Utilizei um valor baixo para teste
    numero = int(input('Insira um número inteiro: '))
    if numero == anterior:
        if contador == 0:  # Sem essa função, a contagem fica com 1 a menos
            contador += 2
            valor = numero
        else:
            contador += 1
            valor = numero
    else:
        if contador > contador2:  # Armazena a maior sequência como forma de comparação 
            contador2 = contador
            contador = 0
            valor2 = valor
            valor = 0
        elif contador == contador2:  # Caso existam duas sequências iguais,
            if valor > valor2:       # o maior valor (numero repetido) precisa ser armazenado até o final do for
                valor2 = valor
                valor = 0
                contador = 0
            else:
                contador = 0
        else:
            contador = 0
            valor = 0
    anterior = numero

# TESTES PARA SABER AS ATUALIZAÇÕES DAS VARIÁVEIS NO FOR
print(f'Teste anterior {anterior}')
print(f'Teste contador {contador}')
print(f'Teste contador2 {contador2}')
print(f'Teste soma {valor}')
print(f'Teste soma2 {valor2}')

# Condições para a resposta
if contador > contador2:
    print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor}')
elif contador2 > contador:
    print(f'A maior sequência consecutiva de números constantes é {contador2}, sendo uma sequência de {valor2}')
elif contador == contador2:
    if valor >= valor2:
        print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor}')
    elif valor < valor2:
        print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor2}')
else:
    print(f'Não houve sequência consecutiva de números constantes, sendo a contagem {contador} e {contador2}')