n = 0
while True:
    print('=' * 20)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('=' * 20)
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
print('Fim!')
