# Pergunte a qtdade de km percorrido por um carro alugado e a qtdd d dias
# que foi alugado. Calcule o preço a ser pago, sabendo que o carro
# custa R$60 por dia e R$ 0,15 po km
d = float(input('Por quantos dias foi alugado? '))
km = float(input('Quantos Km rodados? '))
v = (d * 60) + (km * 0.15)
print('O total a ser pago é R${:.2f}'.format(v))
