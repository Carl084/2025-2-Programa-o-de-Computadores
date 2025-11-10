'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é primo ou não.
'''

import sys

try:
   intnumber = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Informe um número inteiro!')
except KeyboardInterrupt:
   sys.exit('AVISO: Programa interrompido.')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # os primos são maiores que 1
   if intnumber < 2:
      sys.exit(f'O número {intnumber} não é primo.')

   # a quantidade de divisores
   intQtDivisores = 1

   # verifica os divisores
   for intDivisor in range(2, intnumber + 1):
      if intnumber % intDivisor == 0:
         intQtDivisores += 1
      if intQtDivisores > 2: break

   if intQtDivisores == 2:
      print(f'O número {intnumber} é primo.')
   else:
      print(f'O número {intnumber} não é primo.')