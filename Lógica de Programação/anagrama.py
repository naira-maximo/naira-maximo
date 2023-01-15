def anagrama(string1, string2):
    stringa = sorted(string1)
    stringb = sorted(string2)
    return stringa == stringb

print(anagrama('amor', 'roma'))
print(anagrama('geleia', 'aieleg'))
print(anagrama('pato', 'rato'))
print(anagrama('hotel', 'motel'))