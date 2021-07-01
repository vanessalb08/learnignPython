#leia dois valores e mostre um menu na tela
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = int(input('O que deseja fazer? \n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa\n'))
while opcao != 5:
    if opcao == 1:
        soma = num1 + num2
        print('A soma é {}'.format(soma))
    if opcao == 2:
        mult = num1 * num2
        print('A multipliação é {}'.format(mult))
    if opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        else:
            print('{} é maior que {}'.format(num2, num1))
    if opcao == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    opcao = int(input('O que deseja fazer agora? '))
print('Fim!')
