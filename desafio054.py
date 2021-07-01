#Ler ano de nascimento de 7 pessoas e mostrar quantas não são de maior
from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Existem:\n{} pessoas que são maiores de idade\n{} pessoas menores de idade.'.format(maior, menor))
