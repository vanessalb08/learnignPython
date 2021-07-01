#Dizer se o número é primo
total = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        total += 1
print('O número {} foi dividido {} vezes.'.format(num, total))
if total == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))
