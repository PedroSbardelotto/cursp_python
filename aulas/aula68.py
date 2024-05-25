"""
Escopo de funções em python 

Escopo significa local onde aquele código pode atingir 
Existe o escopo global e loccal.
O escopo global é o escopo onde todo o código é alcançavel 
O Escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados

podemos usar o global para poder mexer em variaveis que estão no escopo externo
"""



x= 1 # esse X está npo escopo global

def escopo():
    x = 10 # esse x está no escopo da função "escopo", é acessado pela função "outra função"
    def outra_funcao():
        y = 2 
        print(x,y)
  
    outra_funcao()  
    print(x)


escopo()

