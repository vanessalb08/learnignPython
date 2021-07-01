vel = float(input('Qual a velocidade do carro? '))
multa = vel - 80
if vel>80:
    print('Você está acima do limite. A multa é de R${:.2f}'.format(multa*7))
print('Você está dentro do limite de velociade, parabéns!')
