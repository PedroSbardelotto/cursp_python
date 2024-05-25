"""while/else"""

string = 'Valor Qaulquer'

i = 0 
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1 

    if letra == ' ':
        break
    print(letra)
    i += 1
else: 
    print('O else foi executado.')
print('Fora do While')