media = 0
maior = 0
menor = 0
velho = ''
for p in range(1, 5):
    print('------{}ª Pessoa------'.format(p))
    nome = str(input('Digite o {}° nome: '.format(p))).strip
    idade = int(input('Digite a {}ª idade: '.format(p)))
    sexo = str(input('Qual o {}° Sexo: [M/F]: '.format(p))).upper()
    if p == 1:
        media = idade
        maior = idade
        velho = nome
    else:
            media += idade
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        menor += 1

print('A média de idade é {}'.format(media/p))
print('O mais velho é {} e ele tem {} anos'.format(velho, maior))
print('Existem {} mulheres com menos de 20 anos'.format(menor))
