print('''Ler o comprimento de 3 retas e informar se podem ou
#não formar um triangulo''')
a=float(input('Informe a medida da primeira Reta '))
b=float(input('Informe a medida da segunda reta '))
c=float(input('Informe a medida da terceira reta '))
if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')

