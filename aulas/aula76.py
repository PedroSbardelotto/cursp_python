# Dicionários em Python (tipo dict)
# Dicionarios são estruturas de dados tipo 
# par de "chav" e "valor".
# chaves podem ser consideradas como indice 
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# o valor de ser de qualquer tipo, incluindo outro 
# dicionário 

# Usamos as chaves - {} - ou a classe dict para criar 
# dicionarios.

# imutaveis: str, int ,float, bool, tuple
# mutavel: dict, list


# usando a class dict a baixo
# pessoa = dict(nome= 'Luiz Otávio', sobrenome='miranda')

# key and value 


pessoa = {
    'nome': 'Pedro Henrique',
    'sobrenome': 'Sbardelotto',
    'idade': 26,
    'altura': 1.8,
    'endereços': [ # uma lista com dicionarios dentro
        {'rua': 'tal tal','número': 123},
        {'rua': 'outra_rua','número':321},
    ],
}

print(f'Me chamo, {pessoa['nome']}. Meu sobrenome é {pessoa["sobrenome"]}')
print()
for chave in pessoa:
    print(chave, pessoa[chave])





