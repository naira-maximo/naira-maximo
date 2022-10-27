# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:   * até 20 livros, desconto de 3% por litro
#           * acima de 20 litros, desconto de 5% por litro
# Gasolina: * até 20 litros, desconto de 4% por litro
#           * acima de 20 litros, desconto de 6% por litro
# Leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30
# e o preço do litro do álcool é R$ 2,90.
# Observação: O desconto é aplicado sobre o valor total

print('\033[1;31mDesconto de combustíveis\033[m')


def combustivel():
    litros = int(input('\nInsira os litros de combustível: '))
    tipo = str(input('Insira o tipo de combustível, sendo A para álcool e G para gasolina: '))

    if tipo == 'A' or tipo == 'a':
        valor = litros * 2.90
        if litros <= 20:
            desconto = (valor * 3) / 100
            valor_pago = valor - desconto
            print('-' * 36)
            print('{:-2} litros de álcool.........R${:.2f}\n'
                  '5% de desconto..............R${:.2f}\n'
                  'Total com desconto..........R${:.2f}'
                  .format(litros, valor, desconto, valor_pago))
            print('-' * 36)
        elif litros > 20:
            desconto = (valor * 5) / 100
            valor_pago = valor - desconto
            print('-'*36)
            print('{:-2} litros de álcool.........R${:.2f}\n'
                  '5% de desconto..............R${:.2f}\n'
                  'Total com desconto..........R${:.2f}'
                  .format(litros, valor, desconto, valor_pago))
            print('-'*36)
        else:
            print('Insira uma quantidade de litros válida')
    elif tipo == 'G' or tipo == 'g':
        valor = litros * 3.30
        if litros <= 20:
            desconto = (valor * 4) / 100
            valor_pago = valor - desconto
            print('-'*36)
            print('{:-2} litros de gasolina.......R${:.2f}\n'
                  '5% de desconto..............R${:.2f}\n'
                  'Total com desconto..........R${:.2f}'
                  .format(litros, valor, desconto, valor_pago))
            print('-'*36)
        elif litros > 20:
            desconto = (valor * 6) / 100
            valor_pago = valor - desconto
            print('-'*36)
            print('{:-2} litros de gasolina.......R${:.2f}\n'
                  '5% de desconto..............R${:.2f}\n'
                  'Total com desconto..........R${:.2f}'
                  .format(litros, valor, desconto, valor_pago))
            print('-'*36)
        else:
            print('Insira uma quantidade de litros válida')
            return combustivel()
    else:
        print('Insira um tipo de combustível válido')
    return combustivel()


combustivel()