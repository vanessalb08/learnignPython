v1 = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(v1))
print('Só tem espaços? ',v1.isspace())
print('É um numero? ',v1.isnumeric())
print('É alfabetico? ',v1.isalpha())
print('É alfanumerico? ',v1.isalnum())
print('Está em minusculo? ',v1.islower())
print('Está em maiuscula? ',v1.isupper())
print('Está capitalizada? {}'.format(v1.istitle()))


