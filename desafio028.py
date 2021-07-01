import random
from time import sleep
num = random.randint(0, 5)
sorteio = int(input('Adivinhe o número de 0 a 5: '))
print('Processando...')
sleep(2)
if num == sorteio:
    print('Parabéns, você venceu!')
else:
    print('O número sorteado foi {}, você perdeu.'.format(num))
