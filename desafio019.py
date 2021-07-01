import random
# ou for random import choice
a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quarto nome: '))
lista = [a1, a2, a3, a4]
nome = random.choice(lista)
print('O aluno esolhido foi {}'.format(nome))
