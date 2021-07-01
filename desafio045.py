#Computador jogar JOKENPÔ com usuário
import random
from time import sleep
num = random.randint(0,2)
opcao = int(input('Escolha uma opção:\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura\n'))

if opcao == 0: #pedra
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('Escolhi {} e você {}'.format(num, opcao))
    if num == 1:
        print('Você perdeu! Papel enrola pedra.')
    elif num == 2:
        print('Você ganhou! Pedra quebra tesoura.')
    else:
        print('Empatou, tente de novo!')
elif opcao == 1: #papel
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('Escolhi {} e você {}'.format(num, opcao))
    if num == 0:
        print('Você ganhou! Papel enrola pedra!')
    elif num == 2:
        print('Você perdeu! Tesoura corta papel.')
    else:
        print('Empatou, tente de novo!')
elif opcao == 2: #tesoura
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('Escolhi {} e você {}'.format(num, opcao))
    if num == 1:
        print('Você perdeu! Tesoura corta papel.')
    elif num == 0:
        print('Você ganhou! Pedra quebra tesoura.')
    else:
        print('Empatou, tente de novo!')
else:
    print('Opção inválida, tente novamente')
