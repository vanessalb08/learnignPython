nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
prim = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(prim[0], len(prim[0])))
