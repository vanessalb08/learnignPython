maior18 = 0
menor20 = 0
homem = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [F/M] '))
    if idade >= 18:
        maior18 += 1
    if sexo in 'mM':
        homem += 1
    if idade < 20 and sexo in 'fF':
        menor20 += 1
    continuar = str(input('Deseja continuar? '))
    print('=' * 25)
    if continuar not in 'SsNn':
        print('Opção inválida!')
    if continuar in 'nN':
        break
print(f'São {maior18} maiores de 18 anos, {homem} homens e {menor20} mulheres menores de 20')

