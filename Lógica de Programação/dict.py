# Objetivo
# Escrever um programa que nos retorne uma estrutura contendo
# as palavras existentes no arquivo e a quantidade de vezes
# que as mesmas aparecem no documento

input_lorem_file = open("lorem.txt", "r", encoding="utf-8")
output_lorem_file = open("lorem.out", "w", encoding="utf-8")



def prepare_data(pline: str):
    prepared_line = pline.strip()
    prepared_line = prepared_line.replace(".", " ")
    prepared_line = prepared_line.replace(",", " ")
    prepared_line = prepared_line.replace("!", " ")
    prepared_line = prepared_line.replace("?", " ")
    return prepared_line


def process_qty_words(pwords: list, pdict_qty_words: dict):
    for word in pwords:
        if len(word) == 0:
            continue
        if word in pdict_qty_words:
            qty = pdict_qty_words[word]
            qty += 1
            pdict_qty_words[word] = qty
        else:
            pdict_qty_words[word] = 1


dict_qty_words = {}
for line in input_lorem_file.readlines():
    line = prepare_data(line)
    if len(line) > 0:
        words = line.split()
        process_qty_words(words, dict_qty_words)

for word in sorted(dict_qty_words.keys()):
    output_lorem_file.write(f'{word}:{dict_qty_words[word]}\n')

output_lorem_file.close()
input_lorem_file.close()

print(dict_qty_words)