casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f} '.format(casa, anos, prestacao))

if prestacao <= minimo:
    print('Empréstimo Concedido!')
else:
    print('Empréstimo negado! O valor da prestação é R$ {:.2f}, maior que 30% do seu salário'.format(prestacao))