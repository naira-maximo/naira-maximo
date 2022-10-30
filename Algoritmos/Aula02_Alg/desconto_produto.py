# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
preço = float(input('Qual o preço da mercadoria? R$'))
percentual = float(input('Qual o percentual de desconto? (sem o símbolo %) '))
desconto = (preço*percentual)/100
preço_atual = preço - desconto
print(f'O valor do desconto é de R${desconto:.2f} e o preço a pagar é de R${preço_atual:.2f}')
