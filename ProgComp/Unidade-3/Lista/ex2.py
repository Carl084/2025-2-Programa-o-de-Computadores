'''
   Faça um programa que solicite 5 nomes de alunos e suas respectivas notas da 
   etapa 1 e da etapa 2.

   Armazene essas informações em listas separadas.
      - Nomes dos alunos -> lstNomes
      - Notas da etapa 1 -> lstNotas1
      - Notas da etapa 2 -> lstNotas2
   
   Após a entrada dos dados, o programa deve calcular a média (IFRN) de cada aluno e 
   armazená-la em uma nova lista.
      - Médias dos alunos -> lstMedias

   A média deve ser calculada pela fórmula:
      Média = (Nota Etapa 1 * 2) + (Nota Etapa 2 * 3) / 5

   No final, imprima o nome de cada aluno junto com suas notas e suas médias.

   Exemplo:
      Nome do Aluno          Etapa 1    Etapa 2    Média
      --------------------------------------------------
      João Silva             75         80         78
      Maria Oliveira         90         85         88
      Pedro Santos           60         70         65
      Ana Costa              85         90         88
      Lucas Pereira          70         75         73
      --------------------------------------------------
'''

lstNomes = []
lstNotas1 = []
lstNotas2 = []
lstMedias = []

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
      if (intNota1 < 0 or intNota1 > 100):
         print('ERRO: A nota da Etapa 1 deve estar entre 0 e 100.')
         continue
      if (intNota2 < 0 or intNota2 > 100):
         print('ERRO: A nota da Etapa 2 deve estar entre 0 e 100.')
         continue
   
   intMedia = round(((intNota1 * 2) + (intNota2 * 3)) / 5)
   
   lstNomes.append(strNome)
   lstNotas1.append(intNota1)
   lstNotas2.append(intNota2)
   lstMedias.append(intMedia)
   
   intAlunos += 1
   
print(f'{'Nome do Aluno':<15} {'Etapa 1':>8} {'Etapa 2':>8} {'Média':>8}')
print('-' * 60)

for i in range(5):
   print(f'{lstNomes[i]:<15} {lstNotas1[i]:>8} {lstNotas2[i]:>8} {lstMedias[i]:>8}')
print('-' * 60)