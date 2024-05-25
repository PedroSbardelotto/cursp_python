# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1, type(s1))
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = {1, 2, 3, 3, 3, 3, 3, 3, 3}
# print(s1, type(s1))



# Métodos úteis:
# add, update, clear, discard

# s2 = set()
# s2.add('pedro')
# s2.add('antonia')
# s2.update(('Ola mundo', 1, 2, 3, 4))
# # s2.clear()
# s2.discard('Ola mundo')
# print(s2)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2 # unindo sets
# print(s3)
# s3 = s1 & s2 # intersecção entre dois sets  
# print(s3)
# s3 = s1 - s2 # Itens presentes apenas no set da esquerda
# print(s3)
# s3 = s1 ^ s2

# Exemplo de uso dos stes 
letras =  set()
while True: 
    letra = input('Digite: ')
    letras.add(letra)