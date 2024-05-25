"""
Faça um jogo para o úsuario advinhar qual a palavra secreta. 
- você vai propor uma palavra secretra qualquer e vai dar a possibilidade 
para o usuario digitar apenas uma letra. 
- Quando o usuario digitar uma letra, você vai conferir se a letra digitada está 
na palavra secretra 
   -se a letra digitada estiver na palavra secreta; exiba a letra; 
   -se a letra digitada não estiver na palavra secreta; exiba *. 
Fça a contagem de tentativas do seu úsuario. 
"""

# secret_word = 'Pyhton'
# letter = ''
# user_word = ''
# count_user = 0 

# while user_word != secret_word:
#         letter = input('Digite uma letra: ')
#         count_user += 1 
#         if letter in secret_word == True:
#                 print(f'A letra ({letter}) digitada existe na palavra secreta!')
#                 user_word = letter
#         else: 
#                 print("A letra diitada não exixte na palavra secreta")

import os



palavras_list = ['java', 'python', 'programacao']

palavra_secreta = ''
letras_acertadas =''
numero_tentativa = 0

for i in range(len(palavras_list)):
    palavra_secreta = palavras_list[i]

    while True:
    
        letra_digitada = input('Digite uma letra: ')
        numero_tentativa += 1
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra!')
            continue

        if letra_digitada in palavra_secreta: 
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas: 
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print('Palavra formada: ',palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls') 
            print('##################')
            print('voce ganhou!')
            print('A palavra era!', palavra_formada)
            print('Tentativas:',numero_tentativa)
            print('##################')
            letras_acertadas =''
            numero_tentativa = 0