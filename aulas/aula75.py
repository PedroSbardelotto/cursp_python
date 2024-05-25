""""
Exercicios 
Crie uma função que duplicam, triplicam e quadruplicam 
o numero recebido como parametro 
"""

def criar_multiplicador(num):
    def duplica(num):    
        return num * 2    
    def triplica(num):
        return num * 3 
    def quadruplica(num):     
        return num * 4
    return f'Num duplicado: {duplica(num)} - Num triplicado: {triplica(num)} - Num quadruplicado: {quadruplica(num)}'  
 


print(criar_multiplicador(7))



def criar_multiplicador2(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador2(2)
triplicar = criar_multiplicador2(3)
quadruplicar = criar_multiplicador2(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))

