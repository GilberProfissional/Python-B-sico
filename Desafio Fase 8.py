#Criar um programa que leia um número real qualquer na tela e mostre sua porção inteira
import math

print('Desafio 16 : Ler um número real e mostrar sua porção inteira ')
from math import floor
num=float(input(' Digite um número '))
i=floor(num)
print(' O número digitado {} possui como versão inteira {}'.format(num,i))
#Resolução:
# Import math
# num=float(input('DIigite um valor: ')
#print('O valor digitado foi {} e  a sua porçÃO inteira é {}.format(num,math.trunc(num))
#---------------------------------------------------------------------------------------

#Ler o comprimento do cateto oposto e do Adjacente de um triangulo retângulo.
#Calcule e mostre o comprimento da Hipotenusa
from math import pow,sqrt
print(' Desafio 17 : Calcule a Hipotenusa ')
catop=float(input('Qual o valor do Cateto Oposto? '))
catadj=float(input('Qual o valor do Cateto Adjacente? '))
e=2
a=pow(catop,e)
b=pow(catadj,e)
h=a+b
print( 'Para os valores de Cateto Oposto {} e Cateto Adjacente {} a Hipotenusa será de {:.2f}'.format(catop,catadj,sqrt(h)))
#Resolução:
# Hipotenusa=(catop**2 + catadj**2)**1/2 ou
# Hipotenusa=math.hypot(catop,catadj)
#-----------------------------------------------------------------------------------------------------------------------------------


# Ler um angulo qualquer e mostrar na tela o valor do seno cosseno e tangente
print('Desafio 18: Seno,Cosseno e Tangente ')
from math import sin,cos,tan
x=float(input(' Qual o valor que deseja calcular? '))
ar=math.radians(x)
s=sin(ar)
c=cos(ar)
tg=tan(ar)
print('Para o Valor de {} o Seno será de {:.4f},o Cosseno de {:.4f} e a Tangente de {:4f}'.format(x,s,c,tg))
# Resolução:
# import math
# angulo=float('Digite o Angulo que voce deseja ')
# seno=math.sin(math.radians(angulo))
# print('O angulo de{} tem o Seno de {}.format(angulo,seno)
# cosseno=math.cos(math.radians(math.radians(angulo))
# print('O Angulo de {} tem o Cosseno de {}.format(angulo,cosseno)
# tangente=math.sin(math.radians(angulo))
# print('O angulo de {} tem a Tangente de {].format(angulo,tangente)
#------------------------------------------------------------------------------------------------------------------

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele lendo os nome deles e escrevendo o nome do escolhido
print('Desafio 19: Escolher aleatoriamente um aluno')
import random
alunos=('Alice','Gilbert','Marcos','Pedro')
num=random.choice(alunos)
print( 'Entre a Aluna {},{},{} e {} Quem apagará a lousa será o(a) {} '.format('Alice','Gilbert','Marcos','Pedro',num))
# Resolução:
# import random
# n1 = str(input('Primeiro aluno '))
# n2 = str(input('Segundo aluno '))
# n3 = str(input('Terceiro Aluno'))
# n4 = str(input('Quarto aluno'))
# lista = [n1,n2,n3,n4]
# escolhido = random.choice(lista)
# print9'O aluno escolhido foi {}'.formt (escolhido)
#---------------------------------------------------------------------------------------------------------------------------


# O mesmo professor quer sortear a ordem de apresentação de trabalhos de alunos
#Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
print('Desafio 20: Organizar aleatoriamente a apresentação destes alunos')
aluno1='Alice'
aluno2='Gilbert'
aluno3='Marcos'
aluno4='Pedro'
alunos=[aluno1,aluno2,aluno3,aluno4]
random.shuffle(alunos)
print( 'A ordem aleatoria de apresentação desses alunos será da seguinte forma: ')
for i,aluno in enumerate(alunos,start=1):
    print(f'{i}.{aluno}')
# Resolução:
# import random
# n1=str(input('Primeiro aluno')
# n2=str(input('Segundo aluno')
# n3=str(input('Terceiro Aluno')
# n4=st(input('Quarto aluno')
# lista=[n1,n2,n3,n4]
# random.shuffle(lista)
# print( 'A ordem de apresentação será')
# print(lista)
#----------------------------------------------------------------------------------

#Programa que abra e reproduza em MP3
print(' Desafio 21: Abrir e reproduzir um audio em MP3')
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Carlos Viola - Blasphemous - 03 Tierras de Azafrán.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
# Resolução:
# import pygame
# pygame.init()
# pygame.mixer.music.load("Carlos Viola - Blasphemous - 03 Tierras de Azafrán.mp3")
# pygame.mixer.music.play()
# pygame.event.wait()
#----------------------------------------------------------------------------------





