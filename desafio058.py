#Computador pensa em um número de 0 a 10 e o jogador só sai quando conseguir adivinhar, mostrar quantos palpites foram necessários
import random
tentativas = 0
pc = random.randint(0, 10)
usuario = int(input('Escolha um número entre 1 e 10: '))
while pc != usuario:
    usuario = int(input('Você errou! Tente novamente: '))
    tentativas += 1
print('Você acertou! E só precisou de {} tentativas'.format(tentativas + 1))
