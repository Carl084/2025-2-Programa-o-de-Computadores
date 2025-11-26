'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é um número triangular ou não.

   Um número triangular é um número que pode ser representado na forma 
   de um triângulo equilátero.

   Os primeiros números triangulares são: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
'''

import sys

try:
   intNumber = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Informe um número inteiro válido...')
except KeyboardInterrupt:
   sys.exit('AVISO: Programa interrompido pelo usuário...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # verificar se número é positivos
   if intNumber < 1:
      sys.exit(f'O número {intNumber} não é triangular.')

   intTriangular = 0
   intIncremento = 1 

   while intTriangular < intNumber:
      intTriangular += intIncremento
      intIncremento += 1 
      
   if intTriangular == intNumber:
      print(f'O número {intNumber} é triangular.')
   else:
      print(f'O número {intNumber} não é triangular.')