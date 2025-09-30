#Peço a frase a encontrar as letras A
frase = input('Digite uma frase:')
#Transformo a frase em menuscula
frase = frase.lower()
#Conto a quantidade de A
quantidade = frase.count('a')
#Encontro o primeiro A
primeira = frase.find('a') + 1
#Encontro o segundo A
ultima = frase.rfind('a') + 1
#Apresento a quantidade, a 1° e ultimo A
print(f'A letra "A" apareceu {quantidade} vezes.')
print(f'A primeira vez que apareceu foi na posição {primeira}')
print(f'A ultima vez que apareceu foi na posição {ultima}')