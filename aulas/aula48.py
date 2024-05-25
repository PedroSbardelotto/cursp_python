"""
Lista em Python 
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis de qulauqer tipo - indíces e fatiamento 

CREATE READ UPDATE CRUD 
Crias, ler, alterar, apagar = lista[i] (CRUD)

Métodos úteis: 
append - add um item ao final da lista 
insert - add um item no indice escolhido 
pop - Remove do final ou do indice escolhido 
del - apaga um indice 
clear - limpa a lista 
extend - Estende a lista 
+ - concatena listas 

"""


lista = [ 10, 20, 30, 40]
lista[2] = 300 
del lista[2]
print(lista)
lista.append(50)
lista.pop()
print(lista)


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
