##Ler numero interio e mostrar antecessor e sucessor
n1 = int(input('Diga um número: '))
a = n1 - 1
s = n1 + 1
print('O antecessor de {} é {}\nO Sucessor de {} é {}'.format(n1, a, n1, s))
# podia tirar as variáveis a e s e colocar .format(n1, (n1-1), (n1+1))