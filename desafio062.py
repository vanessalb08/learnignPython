a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while n <= total:
        an = a1 + (n - 1) * r
        n += 1
        print('{} '.format(an), end='➔ ')
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos termos? '))
print('Fim da PA. Você visualizou {} termos'.format(total))
