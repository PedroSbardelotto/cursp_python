"""
argumentos nomeados e n nomeados em funções Python
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y,z): #<- argumentos posicionais
    #Definição da função 
    
    print(f'{x=} {z=}  y={y}', '|', 'x + y =', x + y )




soma(1,2,3) 
soma(y=2,x=1, z=3)

print(1,2,3, sep='-')