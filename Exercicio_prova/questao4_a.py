anterior = 1  # Armazena o último número para comparação
contador = 1  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior + 1)
contador2 = 0  # Soma armazenada para comparação com a contagem vigente
soma = 0  # Soma da contagem vigente, para possível desempate
soma2 = 0  # Soma armazenada para comparação com a contagem vigente

for i in range(0, 10):  # Utilizei um valor baixo para teste
    numero = int(input('Insira um número inteiro: '))
    if numero == anterior + 1 and numero != 1:
        contador += 1
        if soma == 0:  # Sem essa função, o primeiro número da sequência consecutiva é desprezado 
            soma += (numero + anterior)
        else:
            soma += numero
    else:
        if contador > contador2:  # Armazena a maior sequência como forma de comparação 
            contador2 = contador
            contador = 1
            soma2 = soma
            soma = 0
        elif contador == contador2:  # Caso existam duas sequências iguais,
            if soma > soma2:         # a maior soma precisa ser armazenada até o final do for
                soma2 = soma
                soma = 0
                contador2 = contador
                contador = 1
            else:
                contador = 1
                soma = 0
        else:
            contador = 1
            soma = 0
    anterior = numero

# TESTES PARA SABER AS ATUALIZAÇÕES DAS VARIÁVEIS NO FOR
print(f'Teste anterior {anterior}')
print(f'Teste contador {contador}')
print(f'Teste contador2 {contador2}')
print(f'Teste soma {soma}')
print(f'Teste soma2 {soma2}')

# Condições para a resposta
if contador >= contador2:
    if soma >= soma2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo {soma} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo {soma2} como a soma dos termos')
elif contador2 > contador:
    if soma >= soma2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo {soma} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo {soma2} como a soma dos termos')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador} e {contador2}')