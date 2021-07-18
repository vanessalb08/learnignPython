num = 0
opcao = ''
media = 0
cont = 1
soma = 0
maior = 0
menor = 999
while opcao in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    media = soma / cont
    cont += 1
    opcao = str(input('Deseja continuar [S/N]? '))
    if num > maior:
        maior = num
    if num <= menor:
        menor = num
print('A média é {}, o maior é {} e o menor é {}'.format(media, maior, menor))
