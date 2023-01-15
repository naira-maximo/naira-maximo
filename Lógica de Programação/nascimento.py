# Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também,
# verifique e mostre se ela já tem idade para votar (16 anos ou mais) e para conseguir a Carteira de Habilitação (18 anos ou mais).

ano = int(input('Insira o ano em que você nasceu: '))
idade = 2022 - ano
if idade >= 16:
    print(f'Você tem {idade} anos e já tem idade para votar', end= '')
    if idade >= 18:
        print(f' e já pode tirar a Carteira de Habilitação')
    else:
        print(f', mas ainda não pode tirar a Carteira de Habilitação, apenas quando completar 18 anos')
else:
    print(f'Você tem {idade} anos, ainda não tem idade para votar e não pode tirar a Carteira de Habilitação')