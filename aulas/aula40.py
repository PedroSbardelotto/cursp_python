"""Claculadora com o While """


while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0 
    try:
        num_1_float = float(numero_1)
        num_1_float = float(numero_2)
        numeros_validos = True
    except Exception:
        numeros_validos = None
    if numeros_validos == None:
        print('Um ou ambos os numeros são invalidos.')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) >1:
        print('Digite apenas um operador.')
        continue
    print('Realizando sua conta. Confira o resultado abaix!')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador =='-':
        print(num_1_float - num_2_float)
    elif operador =='/':
        print(num_1_float + num_2_float)
    elif operador =='*':
        print(num_1_float / num_2_float)

    sair = input('quer sair? [s]sim: ').lower().startswith('s')

    if sair is True:
        break
    
