# formatação de strings com o f-string

nome = 'Pedro sbardelotto'
altura = 1.84
peso = 104
imc = peso / (altura * altura)
imc1 = peso // (altura ** 2)
imc2 = peso % (altura * altura)
print(f'{nome} tem {altura} de altura')
print(f'pesa {peso} quilos e seu IMC é: {imc1}')

print(imc1)
print(imc2)