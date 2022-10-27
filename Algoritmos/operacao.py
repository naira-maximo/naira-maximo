# Elaborar um algoritmo que efetue o cálculo de juros simples, tendo como entrada:
# c = capital
# i = taxa de empréstimo
# n = períodos

print("Calculadora de juros simples")

c = float(input("Insira seu capital: "))
i = int(input("Insira a porcentagem da taxa de juros: "))
n = float(input("Insira o período em meses: "))

juros = c * (i/100) * n
print(f'Juros: {juros}')
capital_com_juros = c + juros
print(f'Capital com juros: {capital_com_juros}')

resposta = input("Deseja continuar? (S) SIM (N) NÃO: ")
if resposta == "S":
    print("Próximo exercício")
elif resposta == "s":
    print("Próximo exercício")
else:
    print("Teste finalizado")


# Criar um algoritmo que permita fazer a conexão cambial entre Reais e Dólares.
# Considerar como taxa de câmbio US$1,0 = R$2,40.
# Ler um valor em Reais pelo teclado e mostrar o correspondente em Dólares.

# Exercícios de Fixação em sala 5/9/2022



# Calcular e imprimir o valor a ser pago pelo cliente.
# Álcool: até 20 litros, desconto de 3% por litro; acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro; acima de 20 litros, desconto de 6% por litro
