peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / altura ** 2

print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.2:
    print('Você está abaixo do peso')
elif 18.2 < imc < 25:
    print('Você éstá no peso ideal')
elif 25 < imc < 30:
    print('Você está com sobrepeso')
elif 30 < imc < 40:
    print('Você está com obesidade')
else:
    print('Obesidade mórbida')
