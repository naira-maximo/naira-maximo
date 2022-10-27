# Podemos adicionar uma lista em uma lista [], ou um dicionário. 
# Sempre contabilizar o último item com a quantidade de elementos menos 1
# quando a variável está como tipo string, não conseguimos manipular, como mudar um índice. Mas a lista permite.

var = 'ovo'
print(var[0:2])  # Printa apenas a posição 0 e 1.

#lista.append(elemento) adiciona um elemento no final da lista. 
#lista.insert(indice, elemento) adiciona um elemento no índice escolhido. 

listaA = [1, 2]
listaB = [3, 4]

# lista = listaA.extend(listaB)
# print(listaA.extend(listaB))

# lista2 = listaA.append(listaB)
print(listaA.append(listaB))

# input_str = '34|56.7|89.4'
# lista_valores = input_str.split('|')

# srt_gerada_join = lista_valores.join()