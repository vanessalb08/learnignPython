dist = float(input('Qual a distância da viagem? '))
if dist<=200:
    print('Sua passagem custará R${:.2f}'.format(dist*0.5))
else:
    print('Sua passagem custará R${:.2f}'.format(dist*0.45))
