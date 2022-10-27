# Estruturas aninhadas
# Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$0,20 por minuto;
# Entre 200 e 400 minutos, o preço é R$0,18;
# Acima de 400 minutos, o preço por minuto é R$0,15;
# Mais que 800 minutos, R$ 0,08.
# Calcule sua conta de telefone.

minutos=int(input("Insira a quantidade de minutos: "))
if minutos < 200:
    menos200 = minutos*0.20
    print(f"Sua fatura é de: R${menos200}")
elif minutos >= 200 and minutos <= 400:
    entre = minutos*0.18
    print(f"Sua fatura é de: R${entre}")
elif minutos <= 800:
    ate800 = minutos*0.15
    print(f"Sua fatura é de: R${ate800}")
else:
    mais800 = minutos*0.08
    print(f"Sua fatura é de: R${mais800}")