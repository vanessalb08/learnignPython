nome = ''
valor = maisdemil = total = barato = 0
opcao = nomebarato = ''
while True:
    barato = valor
    nomebarato = nome
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? R$ '))
    opcao = str(input('Deseja continuar [S/n]? '))
    total += valor
    if valor > 1000:
        maisdemil += 1
    if valor <= barato:
        barato = valor
        nomebarato = nome
    while opcao not in 'SsNn':
        opcao = str(input('Opção inválida! Deseja continuar? [S/N] '))
    if opcao in 'nN':
        break
print(f'Total gasto {total}\n{maisdemil} produtos custam mais de R$ 1000,00')
print(f'O produto mais barato é {nomebarato} e custa R$ {barato:.2f}')
