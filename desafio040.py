nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1 + nota2)/2

if media < 5:
    print('Sua média é {}. REPROVADO!'.format(media))
elif 5 < media < 6.9:
    print('Sua média é {}. RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {}. APROVADO, PARABÉNS!'.format(media))
