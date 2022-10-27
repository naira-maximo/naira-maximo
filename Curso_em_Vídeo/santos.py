# Crie um programa que reconheça se a cidade em que o usuário nasceu começa com "Santo".
cidade = str(input('Em que cidade você nasceu? ')).strip()  #.strip() retira possíveis espaços colocados indevidamente pelo usuário
print(cidade[:5].upper() == 'SANTO')