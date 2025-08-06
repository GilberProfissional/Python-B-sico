# Programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todos (Sem Considerar espaços)
# Quatas letras tem o primeiro nome
nome=str(input('Digite seu nome completo ')).strip()
print('Seu nome em letras maiúsculas ficará desta forma: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas ficará desta forma: {}'.format(nome.lower()))
print('Seu nome, sem considerar  espaços, tem {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome possui {} Letras'.format(nome.find(' ')))
# ** OU **
separa=nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))


# Faça um programa que leia um numero de 0  a 9999 e mostre na tela cada um dos digitos separados
num=int(input('Informe um número '))
u=num//1 % 10
d=num//10 % 10
c=num//100 % 10
m=num//1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade=str(input('Qual o nome da Cidade? ')).strip()
print(cidade[:5].upper()== 'Santo')

##Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome
nome=str(input('Qual é o Seu Nome? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA'in nome.upper()))



#Ler uma frase e mostrar
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
frase=str(input('Digite uma Frase ')).upper().strip()
print('A Letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#Ler o nome completo,mostrando em sguida o primeiro e o ultimo nome separadamente

n=str(input(' Qual é o seu nome completo? ')).strip()
nome=n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))



