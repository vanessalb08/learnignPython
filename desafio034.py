sal = float(input('Qual o valor do seu salário? R$'))
if sal <= 1250:
    print('Seu novo salário será R${:.2f}, com aumento de 15%.'.format(sal*1.15))
else:
    print('Seu novo salário será R${:.2f}, com aumento de 10%.'.format(sal*1.10))
