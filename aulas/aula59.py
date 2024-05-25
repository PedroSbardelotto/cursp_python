#desempacotamento em chamadas 
# de metodos e funções 


string = 'ABCD'
lista = ['Maria',"helena",1,2,3, "eduarda"]
tupla = 'Python', 'é', 'legal'

# *_ resto de uma lista, tupla 
# a, b, c, *_ = lista


# for nome in lista: 
#     print(nome,end=' ', sep='')

print(*lista) #forma de desempacotar a chamada da função 
print(*lista, sep ='\n')