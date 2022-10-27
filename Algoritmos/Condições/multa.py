# Pergunte a velocidade de um carro, supondo um valor inteiro. 
# Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110.

v = int(input("Velocidade: "))
if v > 110:
    print("Você ultrapassou o limite de velocidade de 110km/h e foi multado!")
    multa = (v-100)*5
    print(f"Valor da multa a ser paga é: R${multa:.2f}") 