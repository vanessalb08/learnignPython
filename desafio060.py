num = int(input('Digite um número: '))
soma = 1
fat = 1
while soma <= num:
    fat = fat * soma
    soma += 1
print('O fatorial de {} é {}'.format(num, fat))
