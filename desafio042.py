r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo')
    if r1 == r2 == r3:
        print('Triangulo Equilátero')
    elif r1 != r2 != r3:
        print('Triângulo Escaleno')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Triângulo Isóceles')
else:
    print('Não pode formar um triângulo')
