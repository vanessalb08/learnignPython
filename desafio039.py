from datetime import date
ano = int(input('Qual o ano de seu nascimento? '))
idade = date.today().year - ano

if idade == 18:
    print('Está na hora de se alistar')
elif idade <= 18:
    print('Você ainda vai se alistar, faltam {} anos'.format(18 - idade))
else:
    print('Você já passou do tempo de se alistar a {} anos'.format(idade - 18))
