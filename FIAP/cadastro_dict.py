usuarios={}

def perguntar():
    resposta = input('''O que deseja realizar?
    <I> - Para Inserir um usuário
    <P> - Para Pesquisar um usuário
    <E> - Para Excluir um usuário
    <L> - Para Listar um usuário: ''').upper()
    return resposta

def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                          input('Digite a última data de acesso: '),
                                          input('Qual a última estação acessada: ').upper()]

opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    if opcao == 'L':
        print(usuarios)
    opcao = perguntar()
