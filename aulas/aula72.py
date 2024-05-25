# Exercicios cp, funções

"""
Crie uma função que multiplica todos os argumentos 
não nomeados recebidos 
Retorne o total para uma variavel e mostre o valor da variavel.

Crie uma função fala se um número é par ou impar
Retorne se o numero é par ou impar



"""

def multiplica(*args):
    total= 1 
    for numeros in args:
        total *= numeros
    return total

multiplication = multiplica(1,2,3,4,5,6,7)
print(multiplication)



def parouimpar(numero):
    # if numero % 2 == 0:
    #     par = 'par'
    #     return par
    # else:
    #     impar = 'impar'
    #     return impar
    multiplo_de_dois = numero % 2==0 
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    


print(parouimpar(2))
print(parouimpar(15))
print(parouimpar(23))
print(parouimpar(4))
print(parouimpar(13))
            
