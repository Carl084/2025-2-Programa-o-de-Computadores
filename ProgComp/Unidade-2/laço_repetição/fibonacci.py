'''
   Programa que solicita um número inteiro ao usuário e exiba os n
   primeiros elementos da Série de Fibonacci (usando WHILE).

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

import sys

try:
    intn = int(input('Digite um número inteiro: '))
except ValueError:
    sys.exit('ERRO: Por favor, digite um número inteiro...')
except KeyboardInterrupt:
    sys.exit('\nAVISO: CTRL+C pressionado pelo usuário...')
except Exception as e:
    sys.exit(f'ERRO: {e}...')
else:
    if intn <= 1:
        sys.exit('ERRO: Por favor, digite um número maior que 1...')

    intanterior, intatual = 0, 1

    intcontador = 1

    # Em While
    while intcontador <= intn:
        print(f'{intatual},', end=' ')
        intanterior, intatual = intatual, intanterior + intatual
        intcontador += 1

    # Em For
    for intcontador in range(1, intn + 1):
        print(f'{intatual},', end='')
        intanterior, intatual = intatual, intanterior + intatual