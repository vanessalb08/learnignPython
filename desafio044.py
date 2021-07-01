valor = float(input('Qual o valor do produto? R$ '))
condicao = int(input(
    'Qual a condição de pagamento? \n1 - A vista/Cheque\n2 - A vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão:\n'))

if condicao == 1:
    print('Você terá 10% de desconto e pagará R$ {}'.format(valor * 0.9))
elif condicao == 2:
    print('Você terá 5% de desconto e pagará {}'.format(valor * 0.95))
elif condicao == 3:
    print('O valor será {}'.format(valor))
elif condicao == 4:
    print('O valor será {}'.format(valor * 1.2))
else:
    print('Opção inválida')
