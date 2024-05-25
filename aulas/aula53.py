"""
enumerate - enumera iteraves (indices)

"""

nomes = ['maria', 'pedro', 'luiz']

lista_enumerate = enumerate(nomes)

for item in lista_enumerate:
    print(item)

for item in enumerate(nomes):
    print(item)

for item in enumerate(nomes):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(nomes):
    pass