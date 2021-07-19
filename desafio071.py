valor = int(input('Qual o valor a ser sacado? R$ '))
total = valor #total a ser pago
ced = 50 #maior cedula no caixa
totced = 0
while True:
    if total >= ced:
        total -= ced #quantas vezes consegue tirar 50 do total
        totced += 1 #conta quantas cedulas foram retiradas
    else: #se não der pra tirar de 50, verificar quala cedula atual
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}')
        if ced == 50: #se não der pra tirar de 50, passa pra cedula de 20
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
