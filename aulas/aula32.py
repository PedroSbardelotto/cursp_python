"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um numero inteiro: ')

# try:
#     if float(entrada) % 2 == 0:
#         text = 'PAR'
#     else:
#         text = 'IMPAR'
# except ValueError:
#     print('Você não digitou um número invalido!')

# print(f'o número digitado ({entrada})  é {text} !')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora: ')
try:
    entrada_int = int(entrada)
    
    try:
        if entrada_int < 0: 
            print('Não existem horas negativas! ')
        elif entrada_int >= 0 and entrada_int <= 11:
            print('Bom Dia!')
        elif entrada_int >= 12 and entrada_int <= 17:
            print("Boa tarde!")
        elif entrada_int >= 18 and entrada_int <= 23:
            print('Boa noite!')
    except:
        print("Você digitou um horário invalido!")
except:
    print("Você não digitou um número inteiro!!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu nome: ')

# if len(nome) <= 4:
#     print('Seu nome é curto!')
# elif len(nome) >= 5 and len(nome) <= 6:
#     print('Seu nome é normal!')
# else: 
#     print('Seu nome é muito grande!')
 