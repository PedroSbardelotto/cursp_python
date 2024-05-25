"""
Lista de listas e seus indices 
"""
salas = [
    # 0          1
    ['Maria', 'Helena',], #0
    #0
    ['Eliane',], #1
    #0    1       2
     ['Luiz','joao','Eduarda',], #2

]
# acessando um lista dentro de outra lista
# PRIMEIRO A POSIÇÃO DA LISTA DENTRO DA LISTA 
# print(salas[1][0])#ELIANE
# print(salas[0][1])#HELENA
# print(salas[2][2])#EDUARDA
# print(salas[2][3][2]) #numero 20 dentro da tupla (é o indice 3 ) 


for sala in salas:
    print(f'A sala é {sala}')
 
    for aluno in sala:
        print(aluno)
