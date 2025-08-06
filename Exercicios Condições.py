# 1.Programa que faça o computador pensar em
#um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número
#escolhido pelo computador
print('''1.Programa que faça o computador pensar em
um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número
escolhido pelo computador''')
import random
nr=random.randint(0,5)
n=int(input('Qual número estou pensando? '))
if n==nr:
    print('Voce acertou! O número que eu pensei foi {}'.format(nr))
else:
    print('Voce errou! Eu pensei no número {}'.format(nr))
print('x'*25)
#Escreva um programa que leia a velocidade de um
#carro.Se ele ultrapassar 80KM/h.Mostre uma mensagem
#Dizendo que ele foi multado.A multa vai custar R$7,00
#Por cada km acima do limite
print('''2.Escreva um programa que leia a velocidade de um
carro.Se ele ultrapassar 80KM/h.Mostre uma mensagem
Dizendo que ele foi multado.A multa vai custar R$7,00
Por cada km acima do limite''')
v=float(input('Qual a velocidade do carro? '))
if v<=80:
    print('Voce está dentro do limite permitido')
else:
    m=(v-80)*7
    print('Quer bancar o Toretto né amostradinho? Pois bem,'
          'voce ultrapassou o limite de velocidade e terá '
          'que pagar uma multa de R${}'.format(m))
print('x'*25)

#Crie um programa que leia um número inteiro
#e mostre se ele é par ou ímpar
print('''Crie um programa que leia um número inteiro
e mostre se ele é par ou ímpar''')
n=int(input('Qual o número escolhido? '))
if n % 2 ==0:
    print('Esse número é par')
else:
    print('Este número é ímpar')
print('x'*25)

#Desenvolva um programa que pergunte a distância
#de uma viagem em KM.Calcule o preço da passagem.
#Cobrando R$0,50 por KM para viagens de até 200km
#e R$0,45 para viagens mais longas
print('''3.Desenvolva um programa que pergunte a distância
de uma viagem em KM.Calcule o preço da passagem.
Cobrando R$0,50 por KM para viagens de até 200km
e R$0,45 para viagens mais longas''')
d=float(input('Qual será a distância da viagem? '))
if d<=200:
    vd=d*0.50
    print('O Valor que será cobrado pela viagem será de {}'.format(vd))
else:
    vr=d*0.45
    print('O valor que será cobrado pela viagem será de {}'.format(vr))
print('x'*25)

#Mostre um programa que leia um ano qualquer e
#Mostre se ele é Bissexto
print('''4.Mostre um programa que leia um ano qualquer e
Mostre se ele é Bissexto''')
import calendar
ano=int(input('Qual ano deseja consultar? ' ))
if ano %4 ==0:
    print('Este é um ano bissexto')
else:
    print('Este não é um ano bissexto')
print('x'*25)

#Ler 3 numeros e mostrar qual é o maior e menor
print('ler 3 numeros e mostrar qual é o maior e menor')
n1=float(input('Informe o primeiro número '))
n2=float(input('Informe o segundo número '))
n3=float(input('Informe o terceiro número '))
if n1>n2 and n1>n3:
    print('O Maior número é {}'.format(n1))
if n2>n1 and n2>n3:
    print('O Maior número é {}'.format(n2))
if n3>n1 and n3>n2:
    print('0 maior número é {}'.format(n3))

if n1<n2 and n1<n3:
    print('O menor número é {}'.format(n1))
if n2<n1 and n2<n3:
    print('O menor número é {}'.format(n2))
if n3<n1 and n3<n2:
    print('O menor número é {}'.format(n3))
print('x'*25)

#Perguntar o salário de um funcinário e calcular
#seu aumento.Para salários superiores a R$1.250,00
#Calcule um aumento de 10%
#para salários inferiores calcule um aumento de 15%
print('''Perguntar o salário de um funcinário e calcular
seu aumento.Para salários superiores a R$1.250,00
Calcule um aumento de 10%
para salários inferiores calcule um aumento de 15%''')
s=float(input('Qual é o seu salário atual? '))
if s >=1250:
    aum1=s*(10/100)
    print('Seu salário de R${} sofrerá um aumento de {},resultando no valor de {}'.format(s,aum1,s+aum1))
else:
    aum2=s*(15/100)
    print('Seu salário de R${} sofrerá um aumento de R${},resultando em R${}'.format(s,aum2,s+aum2))
print('x'*25)

#Ler o comprimento de 3 retas e informar se podem ou
#não formar um triangulo
print('''Ler o comprimento de 3 retas e informar se podem ou
#não formar um triangulo''')
a=float(input('Informe a medida da primeira Reta '))
b=float(input('Informe a medida da segunda reta '))
c=float(input('Informe a medida da terceira reta '))
if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')


