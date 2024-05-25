"""
Faça um lista de compras com listas 
O úsuario deve ter a possibilidade de inserir,
 apagar e listar valores de sua lista
não permita que o programa quebre com erros 
"""
import os

def add_item(lista_compras):
    global var
    var = input('Digite o nome do item: ')
    lista_compras.append(var)
def remove_item(var,lista_compras):
    global indice
    var = input('Digite o indice do item que quer remover: ')   
    try:
        indice = int(var) 
        del lista_compras[indice]
    except ValueError:
        print('Por favor digite número int.')
    except IndexError:
        print('indice não exixte na lista')
def imprimir_item(lista_compras):
    global i, item
    if len(lista_compras) == 0:
        print('Sua lista de compras está vazia')
    else:
        for i, item in enumerate(lista_compras):
            print(f'[{i}] - {item}')


var=""
lista_compras = ['Arroz','Carne','Feijão','Pão']

menu = """
1- ADD item
2- REMOVE item
3- PRINT lista
"""


while True: 
    print(menu)
    entrada = input('Digite a opção: ')

    if entrada == "1":
        os.system('cls')
        add_item(lista_compras)
    if entrada == "2":  
        os.system('cls')  
        remove_item(var,lista_compras)
    if entrada == "3":
        os.system('cls')
        imprimir_item(lista_compras)
        