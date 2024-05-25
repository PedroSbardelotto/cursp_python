
'''
Introdução ao desenpacotamento

'''


nomes = ['maria', 'pedro', 'luiz']
print(nomes)
nome1, nome2, nome3 = ['maria', 'pedro', 'luiz']
print(nome1, nome2, nome3)
nome1, *resto = ['maria', 'pedro', 'luiz']
print(nome1, resto)
nome1, *_ = ['maria', 'pedro', 'luiz']
