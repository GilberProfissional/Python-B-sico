# Programa que leia um número inteiro e mostre o
# seu sucessor e o seu antecessor
print("Desafio 1: >> Antecessor e Sucessor <<<")
n=int(input('Insira um Valor '))
suc=n+1
ant=n-1
print('O número preenchido é {}, seu antecessor é {} e seu sucessor é {}'.format(n,ant,suc))

#Algoritmo que leia um número e mostre seu dobro,triplo e Raiz Quadrada
print('Desafio 2: >>> Ler um número e mostrar o seu dobro,triplo e raiz quadrada <<<')
n=int(input('Insira Outro valor '))
dobro=n*2
triplo=n*3
raiz=n**(1/2)
print('O número preenchido foi {} seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n,dobro,triplo,raiz))

#Ler duas notas e Mostrar a média
print('Desafio 3: >>> Ler duas notas e mostrar a média <<<')
n=float(input("Qual a primeira nota do Aluno(a)? "))
n2=float(input('Qual a segunda nota do Aluno(a)? '))
n3=(n+n2)/2
print('Os valores de Notas preenchidos foram {} e {}, logo a média  é {}'.format(n,n2,n3))

# Ler um número em metros e  depois o exibir em centimetros e milímetros

print('Desafio 3: >>> Converter Metros em Centímetros e Milímetros <<<')
n=float(input("Qual o valor de Medida que deseja converter? "))
n2=n*100
n3=n*1000
print('O Valor em metros preenchido foi de {}, essa medida em centímetros será de {} e em milímetros de {}'.format(n,n2,n3))

# Ler um número inteiro e mostrar na tela sua tabuada
print('Desafio 4: >>> Ler um número inteiro e fazer a tabuada <<<')
n=float(input("Qual valor deseja verificar a tabuada? "))
n1=n*0
n2=n*1
n3=n*2
n4=n*3
n5=n*4
n6=n*5
n7=n*5
n8=n*6
n7=n*7
n9=n*8
n10=n*9
n11=n*10
print('A tabuada do número {} é '.format(n))
print("{} x 0 = {} ".format(n,n1))
print("{} x 1= {} ".format(n,n2))
print('{} x 2 = {}'.format(n,n3))
print('{} x 3 = {}'.format(n,n4))
print('{} x 4 = {}'.format(n,n5))
print('{} x 5 = {}'.format(n,n6))
print('{} x 6 = {}'.format(n,n7))
print('{} x 7 = {}'.format(n,n8))
print('{} x 8 = {}'.format(n,n9))
print('{} x 9 = {}'.format(n,n10))
print('{} x 10 = {}'.format(n,n11))
print('==========================')

# Ler quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
print('Desafio 5:  >>> Ler quanto uma pessoa tem na carteira e motrar quantos dólares ela pode comprar,considerando US$1=3,27')
n=float(input("Qual valor disponível atual? "))
d=3.27
n1=n*d
print('Considerando o valor do dólar atual de US${}, seu poder de compra em dólar será na quantia de {}'.format(d,n1))

# Ler a largura e a Altura de uma parede em metros. Calcule sua área e a quantidade de tinta necessária para pintá-lo,sabendo que cada litro de tinta pinta uma área de 2M²

print('Desafio 6: >>> Calcular Largura e altura de uma parede em metros,calcular area da parde e calcular quantos litros de tinta preciso para pintar ela <<< ')
l=float(input('Qual a Largura da Parede? '))
a=float(input('Qual a Altura da Parede? '))
ar=l*a
t=2
tpa=ar/t
print('A área total de sua parede é de {}m², sendo necessário {} Litros de tinta para sua pintura'.format(ar,tpa))

# Ler um preço de um produto e depois mostrar um novo preço com 5% de desconto
print('Desafio 7: >>> Ler um preço de um produto e depois ler o mesmo preço com 5% de desconto <<< ')
n=float(input('Qual o valor original? '))
desconto=float(0.05)
novopreço=n-(n*desconto)
print('O Preço original é de {}, com desconto de 5% será de {}'.format(n,novopreço))

 #Ler o salário de um funcionário e mostrar seu novo salário com 15% de aumento
print('Desafio 8: >>> Ler o salário de um funcionário e depois inforar qual seria seu salário com 15% de aumento <<< ')
n=float(input('Qual o valor de seu salário atualmente? '))
aumento=float(0.15)
novosalario=n+(n*aumento)
print('Baseado no salário atual de {},seu salário com 15% de aumento será de {}'.format(n,novosalario))

#Coverter temperaturas
print('Desafio 09: >>> Converter temperaturas de °C para °F <<< ')
c=float(input('Qual é a temperatura em °C? '))
f=((9*c)/5)+32
print('A temperatura de {} °C convertida será de {} °F '.format(c,f))

#Perguntar a quantidade de Km Percorrido por um carro alugado e a quantidade de dias que ele foi alugado
#Calcular preço a pagar sabendo que o carro custa R$60,00 por dia e R$ 80,15 por KM rodado
print('Desafio 10: >>> Preço total de carro alugado <<< ')
a=int(input('Quantos dias foi o alugel? '))
k=float(input('Qual a quilometragem rodada? '))
c=60
km=0.15
total=(k*km)+(a*c)
print('O preço total será de {}'.format(total))

