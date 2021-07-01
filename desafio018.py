import math

num = float(input('Qual o ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tg = math.tan(math.radians(num))
print('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nA tangente de {} é {:.2f}'.format(num, sen, num, cos, num, tg))
