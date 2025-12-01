'''
   Reescreva o código do exercício anterior, mas desta vez utilizando listas
   compostas (listas dentro de listas) para armazenar as informações dos alunos.
'''
lstPrincipal = []

intAlunos = 1
while intAlunos <= 5:
   strNome = input(f'Digite o nome do {intAlunos}º aluno: ')
   try:
      intNota1 = int(input('Digite a nota da etapa 1: '))
      intNota2 = int(input('Digite a nota da etapa 2: '))
   except ValueError:
      print('Erro: Digite um valor inteiro para a nota!')
      continue
   else:
      if not 0 <= intNota1 <= 100:
         print('ERRO: A nota da Etapa 1 deve estar entre 0 e 100.')
         continue
      if not 0 <= intNota2 <= 100:
         print('ERRO: A nota da Etapa 2 deve estar entre 0 e 100.')
         continue
   
   intMedia = round(((intNota1 * 2) + (intNota2 * 3)) / 5)
   
   lstPrincipal.append([strNome, intNota1, intNota2, intMedia])
   
   intAlunos += 1
   
lstPrincipal.sort()

print(f'{'Nome do Aluno':<15} {'Etapa 1':>8} {'Etapa 2':>8} {'Média':>8}')
print('-' * 60)

for strNome, intNota1, intNota2, intMedia in lstPrincipal:
   print(f'{strNome:<15} {intNota1:>8} {intNota2:>8} {intMedia:>8}')
print('-' * 60)