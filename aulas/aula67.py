"""
Valores padrão para parâmetros! 
A odefinir uma função, os parametros podem ter valores padrão. Caso o valor não 
não seja enviado para o parametro, o valor padrão será usado. 
 
REFATORAR: editar o seu código.

"""


def soma(x,y, z=None):  # zero ao ser confrontado com um boleano retorna falsy e pode criar problemas para o futuro
    
    if z  is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else: 
        print(f'{x=} {y=}', x + y)
soma(1,2)
soma(2,40)
soma(100,100)
soma(7, 9, 0)