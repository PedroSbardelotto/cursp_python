"""
Higher Order Functions 
first class functions 

"""
def saudacao(msg):
     return msg


def executa(funcao, msg):
     return funcao(msg)



v = executa(saudacao, 'Bom dia!')
print(v)




# # Funções como ARGUMENTOS 
# def aplicar_funcao(func,valor):
#     return func(valor)
# def quadrado(x):
#     return x * x

# resultado = aplicar_funcao(quadrado, 5)
# print(resultado) # saida 25 


# # Funcções como resultado 
# def multplicador(n):
#     def funcao_interna(x):
#         return x * n
#     return funcao_interna

# dobrador = multplicador(2)
# resultado = dobrador(5)
# print(resultado) # saida 10 

# # Funções de MAP, FILTER e REDUCE 

# # Map - aplica uma função a cada elemento da sequência 
# lista = [1,2,3,4]
# resultado_map = list(map(lambda x: x* 2, lista))
# print(resultado_map) # saida: [2,4,6,8]

# #FILTER Filtra os elementos da sequencia com base em uma função de teste
# resultado_filter = list(filter(lambda X: X% 2 ==0 ,lista))
# print(resultado_filter) # saida [2,4]

# #REDUCE - Reduz a sequencia a um unico valor aplicadno uma função cumulativa
# from functools import reduce
# resultado_reduce = reduce(lambda x, y: x + y, lista) # saida 10

# # funções lambda 
# quadrado = lambda x: x*x 
# resultado = quadrado(5)
# print(resultado) # Saida: 25 

# # DECORADORES 
# def decorador(func):
#     def wrapper(*args, **kwargs):
#         print("antes de função")
#         resultado = func(*args, **kwargs)
#         return resultado
#     return wrapper

# @decorador
# def minha_funcao():
#     print("executanto a função")

# minha_funcao()


def maps(a):
    
   return a * 2 


print(map([1, 2]))