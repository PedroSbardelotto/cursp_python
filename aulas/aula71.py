"""
args - Argumentos não nomeados 
* - *args (empacotamentos e desnpacotamento)

"""

#Lembre-se de desmpacotamento 
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x+y

def soma(*args):
    total = 0
    for numero in args:
        
        total = total + numero 
       
    return total

 
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)
soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

outra_soma = soma(1,2,3,4,5,6,7,8,100)

print(outra_soma)