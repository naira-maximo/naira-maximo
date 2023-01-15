# Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. Utilize a seguinte tabela como referência:
'''Código                      Classificação
    1                          Alimento não-perecível
    2, 3 ou 4                  Alimento perecível
    5 ou 6                     Vestuário
    7                          Higiene pessoal
    8 até 15                   Limpeza e utensílios domésticos
    Qualquer outro código      Inválido'''

def código():
    codigo = int(input('Insira o código do produto (de 1 a 15): '))
    if codigo == 1:
        print(f'Produtos com o código {codigo} são alimentos não-perecíveis')
    elif codigo > 1 and codigo <= 4:
        print(f'Produtos com o código {codigo} são alimentos perecíveis')
    elif codigo == 5 or codigo == 6:
        print(f'Produtos com o código {codigo} são vestuários')
    elif codigo == 7:
        print(f'Produtos com o código {codigo} são de higiene pessoal')
    elif codigo >= 8 and codigo <= 15:
        print(f'Produtos com o código {codigo} são de limpeza e utensílios domésticos')
    else:
        print('Código inválido')
    código()
código()
