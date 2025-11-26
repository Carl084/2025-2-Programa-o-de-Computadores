'''

   Faça um programa que solicite ao usuário um número de até 4 dígitos inteiro positivo e exiba a soma dos seus algarismos.

   Exemplo: 2456 = 17 (2 + 4 + 5 + 6)

   DICA: Vocês irão usar o operador de divisão inteira (//) e o operador de resto de divisão inteiro (%)

'''

import sys
try: #Solicitar um número até 4 dígitos
    num = int(input('Diga um número de até 4 dígitos:'))

#Verificar possiveis erros
except ValueError:
    sys.exit('ERRO: Por favor, insira apenas número inteiro.')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')
if not (num>0) or (num>9999):
    sys.exit('Erro: Digite um número entre 1 e 9999.')

#Milhar
IntMil = num//1000
num = num%1000

#Centena
IntCent = num//100
num = num%100

#Dezena
IntDez = num//10
num = num%10

sum = IntMil+IntCent+IntDez+num
print(f'A soma dos algarismos é {sum}')