# Leia largura e altura em m, calcule a área e a qtidade de tinta para pintar
l = float(input('Qual a largura (em metros): '))
h = float(input('Qual a altura (em metros): '))
a = l * h
t = a / 2
print('A aréa é de {}m²\nSerão necessários {}l de tinta para pintar'.format(a, t))