# Ordem do Python:
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

# nome = str(input('Qual é o seu nome? '))
# print('Prazer em te conhecer {:=^20}!'.format(nome))
# arredondar {:2f}

n1=int(input('Um Valor: '))
n2=int(input('Outro valor '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, o produto é {},  a divisão é {:.3f}'.format(s,m,d),end=' >>> ')
print('Divisão Inteira {} e potência {}'.format(di,e))
