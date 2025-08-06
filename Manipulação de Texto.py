frase='Curso em Video Python'

# Fatiamento
print('''Fatiamento por letra, colocar'
'entre colchetes  a posição da letra que eu quero
Exemplo:''')
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print('Pulando de 2 em 2: ')
print(frase[1:15:2])
print('Frase inteira pulando de 2 em 2')
print(frase[::2])
print('*'*25)

#Contar Quantidades
print('Contar Quantas vezes aparece uma letra')
print(frase.count('o'))
print(frase.count('O'))
print('''Deixar todas as letras maiúsculas e depois contar
quantas vezes alguma delas aparece''')
print(frase.upper().count('O'))
print('*'*25)
print('Verificar tamanho da frase')
print(len(frase))
print('Remover espaços e depois contar quantos caracteres tem ')
print(len(frase.strip()))
print('Trocar texto na Frase Apenas para imprimir')
print(frase.replace('Python',  'Android'))
print(frase)
print('Trocar texto na frase de forma Definitiva, o salvando')
frase=frase.replace('Python','Android')
print(frase)
frase=frase.replace('Android','Python')
print('*'*30)

print('Verificar se alguma palavra está na frase')
print('Curso'in frase)
print('Encontrar Posião inicial')
print(frase.find('Video'))
print('*'*30)
print('Dividir a Frase')
dividido=(frase.split())
print(dividido[2])
print(dividido[2][3])



