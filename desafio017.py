import math
cop = float(input('Cateto oposto: '))
cadj = float(input('Cateto adjacente: '))
# hip = pow(cop, 2) + pow(cadj, 2)
hip = math.hypot(cop, cadj)
print('A hipotenusa é {:.2f}'.format(hip))



