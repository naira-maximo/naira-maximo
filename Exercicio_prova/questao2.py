'''Escreva um algoritmo que receba o valor do salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa,
ambos informados pelo usuário. Sabendo-se que a empresa paga 5% sobre um total de até R$1.500,00,
mais 7% sobre o valor que ultrapassar esse montante (diferença), o programa deve calcular e imprimir o salário total final do vendedor'''

# Receber o valor do salário fixo e o valor de vendas
salario_fixo = float(input('Informe o salário fixo do vendedor: R$'))
valor_de_vendas = float(input('Informe o valor das vendas efetuadas pelo vendedor: R$'))

# Calcular a porcentagem sobre um total de até R$1.500,00 (5%)
if valor_de_vendas <= 1500.00:
    comissao = (valor_de_vendas * 5)/100
# Calcular a porcentagem sobre a diferença, se ultrapassar R$1.500,00 (5% para 1500 mais 7% para o restante)
elif valor_de_vendas > 1500.00:
    comissao = ((1500 * 5)/100) + (((valor_de_vendas - 1500.00)*7)/100)
# Imprimir o salário total final do vendedor
salario_atual = salario_fixo + comissao
print(f'O salário total final do vendedor é de R${salario_atual:.2f}.')