num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [Para sair digite 999]: '))
    if num == 999:
        soma = soma - num
        cont = cont - 1
    cont += 1
    soma = soma + num
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
