soma = cont = 0
while True:
    num = int(input('Dugite um valor (999 para parar): '))
    if num == 999: #Antes de somar, verifica se o número é o flag
        break
    cont += 1 #só será contabilizado se não for o flag
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
