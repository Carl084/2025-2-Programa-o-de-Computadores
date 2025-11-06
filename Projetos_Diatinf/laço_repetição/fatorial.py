'''
   Fazer um programa que solicite um número inteiro e calcule seu fatorial
'''

import sys

try:
    intnumber = int(input('Digite um valor inteiro: '))

except ValueError:
    sys.exit('O valor deve ser inteiro.')
except:
    sys.exit(f'Erro: {sys.exc_info()}')

else:
    if intnumber < 0:
        sys.exit('Erro: não existe fatorial de número negativo.')
    if intnumber == 0 or intnumber == 1:
        sys.exit(f'{intnumber}! = 1')

    print(f'{intnumber}! = {intnumber}', end='')

    intfatorial = 1

    # Verção While
    while intnumber > 1:
        intfatorial *= intnumber
        intnumber -= 1
        print(f' x {intnumber}', end='')

    print(f' x 1 = {intfatorial}')

    # Verção For
    for intAuxiliar in range(intnumber, 1, -1):
        intFatorial *= intAuxiliar

    print(f'{intnumber}! = {intFatorial}')