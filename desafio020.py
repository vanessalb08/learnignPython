# Sorteie ordem de apresentação
import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome'))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
n5 = str(input('Quinto nome: '))
lista = [n1, n2, n3, n4, n5]
# ordem = random.sample(lista, 5)
random.shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))
