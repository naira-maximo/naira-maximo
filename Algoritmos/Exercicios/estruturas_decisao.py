# Estrutura de Decisão

# Fazer um programa que leia do teclado o nome, o grupo e
# o preço de fábrica de um produto do estoque. Calcular o
# preço de venda do produto sabendo que a margem de
# lucro é de 20% para os produtos do grupo "A", 30% para
# os do grupo "B" e 10% para os demais grupos. Imprimir o
# nome do produto, seu grupo o preço de fábrica e o preço
# de venda.

# Operador Ternário - <valor> if <condicao> else <valor>

nome = input("Informe o nome do produto: ")
grupo = input("Informe o grupo do produto (A|B|C): ") # str - class -> methods
preco_custo = float(input("Informe o preço de custo do produto: R$ "))
margem = 0.0

if grupo.upper().strip() == "A": # ' a ' -> ' A ' -> 'A'
    margem = 1.2
elif grupo.upper().strip() == "B":
    margem = 1.3
else:
    margem = 1.1
# ' - " - '''
print(f'''
    Nome do produto - {nome}
    Grupo do produto - {grupo.strip().upper()}
    Preço de custo - R${preco_custo:.2f}
    Preço de venda (final) - R${(preco_custo * margem):.2f}
''')