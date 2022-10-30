'''Sabendo que a população do país A é da ordem de 15000 habitantes com uma taxa de crescimento de 10%,
que a população do país B é de 45000 habitantes com uma taxa de crescimento de 5%,
e que a população do país C é de 65000 habitantes com uma taxa de crescimento de 2,5%, escreva um programa que calcule e imprima:
* Em quantos anos a população A igualará ou ultrapassará a população B; e
* Em quantos anos a população A ultrapassará a população C em 23%'''

# População dos países
a1 = 15000  # Criei duas variáveis 'a' para que acumule os valores simultaneamente, independente do outro cálculo 
a2 = 15000
b = 45000
c = 65000
# Passagem dos anos
anos1 = 0  # Para que não houvesse conflito, coloquei as contagens de anos separadas para cada situação
anos2 = 0
# Calcular o crescimento anual da população dos países A e B
while a1 <= b:
    taxa_a = (a1 * 10)/100  # Taxa de crescimento anual do país A
    taxa_b = (b * 5)/100  # Taxa de crescimento anual do país B
    a1 += taxa_a  # Acréscimo da taxa na variável da população a cada ano contabilizado
    b += taxa_b
    anos1 += 1  # Contador de anos
print(f'A população A igualará ou ultrapassará a população B em {anos1} anos, tendo {a1:.0f} habitantes a população A e {b:.0f} a população B')

# Calcular o crescimento anual da população dos países A e C
while a2 < c*1.23:
    taxa_a = (a2 * 10)/100  # Taxa de crescimento anual do país A
    taxa_c = (c * 2.5)/100  # Taxa de crescimento anual do país C
    a2 += taxa_a  # Acréscimo da taxa na variável da população a cada ano contabilizado
    c += taxa_c
    anos2 += 1  # Contador de anos
print(f'A população A ultrapassará a população C em 23% em {anos2} anos, tendo {a2:.0f} habitantes a população A e {c:.0f} a população C')

