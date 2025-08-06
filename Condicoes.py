tempo=int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('-- Fim -- ')
print('x'*25)
 # Ou
t=int(input('(Modelo 2) Quantos anos tem o seu carro? '))
print('Carro novo'if t<=3 else 'Carro Velho')
print('-- Fim -- ')
print('x'*25)

print('Exemplos')
nome=str(input('Qual é o seu nome? '))
if nome == 'Gilbert':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia {}'.format(nome))

n1=float(input('Digite a primeira Nota '))
n2=float(input('Digite a segunda Nota '))
n=(n1+n2)/2
print('A sua media foi {:.1f}'.format(n))
if n>=6.0:
    print('Sua média foi boa! Parabéns! ')
else:
    print('Sua média foi ruim! Estude mais')

