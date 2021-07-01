a1 = int(input('Qual o primeiro termo: '))
r = int(input('Qual a razã]o: '))
n = 1
while n <= 10:
    an = a1 + (n - 1) * r
    n += 1
    print('{} '.format(an), end='➔ ')
print('Fim')
