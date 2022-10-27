# Receba como entrada 20 notas de alunos
# Selecione e popule

numero_alunos = int(input('Informe o número de alunos da turma: '))
lista_notas = []
soma_notas = 0.0
for indice in range(1, numero_alunos + 1):  # ou colocar 0, numero_alunos
    nota = float(input(f'Informe a nota {indice}: '))  # se a lista começar em 0, colocar indice + 1
    soma_notas += nota
    lista_notas.append(nota)

# media = sum(lista_notas) / len(lista_notas)
media = soma_notas / numero_alunos
print(media)

lista_sup_media = []
for indice in range(0, numero_alunos):
    if lista_notas[indice] >= media:
        lista_sup_media.append(lista_notas[indice])
print(lista_sup_media)

