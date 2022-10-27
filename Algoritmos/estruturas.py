# ESTRUTURAS DE SELEÇÃO
# Escreva um algoritmo que, a partir de um mês fornecido (número inteiro de 1 a 12), apresente o nome dele por extenso ou uma mensagem de mês inválido

meses = ['Mês inválido','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = int(input('Insira um número equivalente a um mês (de 1 a 12): '))
if mes <= 12:
    print(meses[mes])
else:
    print('Número inválido')

# Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles compõem uma data válida.
# Não deixe de considerar os meses com 30 ou 31 dias, e o tratamento de ano bissexto.
ano = int(input('Insira um ano:'))
mês = int(input('Insira um mês:'))
dia = int(input('Insira um dia:'))
if ano <= 2022:
    if ano % 4 == 0:
        print('Ano bissexto, com 366')
        if mês > 0 and mês <=12:
            if mês == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                if dia > 0 and dia <=31:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 30 dias')
            elif mês == 2:
                if dia > 0 and dia <= 29:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 29 dias')
            elif mês == 4 or 6 or 9 or 11:
                if dia > 0 and dia <= 30:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 30 dias')
    else:
        print('Ano com 365 dias')
        if mês > 0 and mês <=12:
            if mês in [1, 3, 5, 7, 8, 10, 12]:
                if dia > 0 and dia <=31:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 30 dias')
            elif mês == 2:
                if dia > 0 and dia <= 28:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 28 dias')
            elif mês == 4 or 6 or 9 or 11:
                if dia > 0 and dia <= 30:
                    print(f'Data válida: {dia}/{mês}/{ano}')
                else:
                    print(f'O mês {mês} tem de 1 a 30 dias')
        else:
            print('Mês inválido')
else:
    print (f'O ano {ano} não é válido')




# 31 Janeiro, março, maio, julho, agosto, outubro, dezembro

# 29 ou 28 Fevereiro

# 30 abril, junho, setembro, novembro

# Escreva o signo do zodíaco correspondente ao dia e mês informado.



