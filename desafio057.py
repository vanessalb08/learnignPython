sexo = str(input('Informe seu sexo: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, digite novamente:')).upper()
print('Sexo {} registrado'.format(sexo))
