'''
   Fazer um programa que solicite ao usuário um valor inteiro positivo N e gere uma lista 
   com N valores inteiros aleatórios entre 1 e 100, sem repetição. 
   
   Em seguida, o programa deve exibir:

   - A lista gerada
   - A soma dos valores na lista
   - A média dos valores na lista
   - O maior valor na lista
   - O menor valor na lista
   - A mediana dos valores na lista
   - A variância dos valores na lista
   - O desvio padrão dos valores na lista
'''

import random

Lista_valores = []
i = 0

try:
    IntN = int(input('Digite um valor inteiro positivo: '))
except ValueError:
    print('Erro: Digite apenas números inteiros e positivos')
if IntN <= 0 or IntN > 100:
    print('Erro: O número deve ser maior que 1 e menor que 100')
else:
    while i < IntN:
        IntValor_aleatorio = random.randint(1,100)
        if IntValor_aleatorio not in Lista_valores:
            Lista_valores.append(IntValor_aleatorio)
            i += 1
    print(f'Lista gerada: {Lista_valores}')