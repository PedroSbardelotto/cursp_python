# Métodos úteisdos dicionarios em python 
# len - quantas chaves 
# keys - iteravel com chaves 
# values - iteravel com chaves e valores 
# items - iterável com chaves e valores 
# setdefoult- adiciona valor se a chave não existe 
# copy - retorna uma cópia rasa (shallow copy)
# get - obtem uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - apaga o ultimo item adcionado
# update - atualiza um dicionario com outro



# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome':'Sbartdelotto',
#     'idade': 900,
# }
# pessoa.setdefault('idade', None)


# # print(pessoa.__len__()) # existem 2 chaves no dict pessoa
# print(len(pessoa)) # existem 2 chaves no dict pessoa
# print(list(pessoa.keys())) # keys interando com list
# print(pessoa.keys()) # retorna valores de keys e são iteraveis, podem ser tranformados em tupls,listas, etc
# # for values in pessoa: 
# #     print(values)
# print(list(pessoa.values())) # valores dentro do dict,iterando com listas 
# print(pessoa.values()) # valores dos values mostrados como dict  
# # for valor in pessoa.values():
# #     print(valor)
# print(list(pessoa.items())) 

# # for chave, valor in pessoa.items():
# #     print(chave, valor)

# shallow copy VS deeep copy 



d1 = {
     'c1': 1,
     'c2': 2,
     'l1': [0, 1, 2],
 }
d2 = d1.copy() # copia rasa 

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

