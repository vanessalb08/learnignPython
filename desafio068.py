import random
pc = random.randint(1, 10)
cont = 0
while True:
    print('=' * 25)
    num = int(input('Digite um número: '))
    opcao = str(input('Par ou ímpar? [P/I]: '))

    par = (num + pc) % 2

    if opcao not in 'PpIi':
        print('Opção inválida!')
    elif (opcao == 'p' and par == 0) or (opcao == 'i' and par != 0):
        print('Você ganhou')
        print(f'O computador escolheu {pc} e você {num} e a soma é {pc + num}')
        print('=' * 25)
        print('Vamos jogar de novo?')
        cont += 1
    else:
        print('Você perdeu')
        print(f'O computador escolheu {pc} e você {num} e a soma é {pc + num}')
        print(f'Você ganhou {cont} vezes')
        break
