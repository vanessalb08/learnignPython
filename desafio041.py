#Leia o ano e mostre a categoria da idade
from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano

if idade <= 9:
    print('Mirim')
elif 9 < idade <= 19:
    print('Infantil')
elif 19 < idade <= 20:
    print('Sênior')
else:
    print('Master')