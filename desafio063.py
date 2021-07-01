num = int(input('Quantos elementos quer ver? '))
termo = 0
soma = 1
cont = 1
fib = 0
while cont <= num:
    fib = termo + soma
    print(termo, end='➔ ')
    soma = termo
    termo = fib
    cont += 1
print('Fim')
