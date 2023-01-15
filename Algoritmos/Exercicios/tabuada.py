tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(f'{tabuada} x {valor:2d} = {tabuada*valor:2d}'))