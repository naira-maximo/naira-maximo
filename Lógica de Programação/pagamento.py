# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

'''Código           Condição de pagamento
    1       Á vista em dinheiro ou cheque, recebe 10% de desconto
    2       Á vista no cartão de crédito, recebe 5% de desconto
    3       Em duas vezes, preço normal de etiqueta sem juros
    4       Em três vezes, preço normal de etiqueta mais juros de 10%'''
    
def etiqueta():
    preço = float(input('Insira o valor do produto que consta na etiqueta: R$'))
    pagamento = input('Qual será a forma de pagamento (dinheiro, cheque ou cartão de crédito)? ').lower().strip()
    if pagamento == 'dinheiro' or pagamento == 'cheque':
        print(f'O valor a pagar é de {preço - (preço*10)/100:.2f} ou {preço*0.9:.2f}')
    elif pagamento == 'cartão de crédito' or pagamento == 'crédito':
        parcelas = int(input('Quer dividir em quantas parcelas (1, 2 ou 3 vezes)? '))
        if parcelas == 1:
            print(f'O valor a pagar é de R${preço*0.95:.2f}')
        elif parcelas == 2:
            print(f'O valor a pagar é de R${preço:.2f}')
        elif parcelas == 3:
            print(f'O valor a pagar é de R${preço*1.10:.2f}')
        else:
            print('Número de parcelas não permitido')
    else:
        print('Forma de pagamento não permitido')
    etiqueta()
etiqueta()