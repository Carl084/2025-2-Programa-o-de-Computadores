'''
   Contando de 1 a 10 e exibindo se o número é par ou ímpar
'''

# definir variavel
intnumber=1

# iniciar loop
while intnumber <= 10:

    # veificar se o numero é par ou impar
    if (intnumber%2)==0:
        print(f'{intnumber} é par.')
    
    else:
        print(f'{intnumber} é ímpar.')
    
    intnumber += 1