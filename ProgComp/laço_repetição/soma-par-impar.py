'''
   Programa que conta de 1 a 100 e exibe a soma dos números pares e
   a soma dos números ímpares.
'''

# variaveis
intsomapares = 0
intsomaimpares = 0
intconador = 1

# loop para contar de 1 a 100
while intconador <= 100:

    # Verifica se o número é par ou ímpar e acumula a soma
    if (intconador%2) == 0:
        intsomapares += intconador
    
    else:
        intsomaimpares += intconador

    intconador += 1

print(f'Soma dos númeoros pares: {intsomapares}')
print(f'Soma dos números ímpares: {intsomaimpares}')