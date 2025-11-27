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

List_values = []
i = 0

try:
    IntN = int(input('Digite um valor inteiro positivo: '))
except ValueError:
    print('Erro: Digite apenas números inteiros e positivos')
else:
    while i < IntN:
        IntValue_random = random.randint(1,100)
        if IntValue_random not in List_values:
            List_values.append(IntValue_random)
            i += 1
    
    average = sum(List_values)/len(List_values)
    square_deviation = [(x - average)**2 for x in List_values]

    List_values_salaries = sorted(List_values)
    size = len(List_values_salaries)
    
    variance = sum(square_deviation)/sum(List_values)

    if len(List_values) % 2 == 0:
        center1 = List_values_salaries[size//2-1]
        center2 = List_values_salaries[size//2]
        median = (center1)+(center2)/2
    else:
        median = List_values_salaries[size//2]
    

    print(f'Lista gerada: {List_values}')
    print(f'Lista orden.: {List_values_salaries}')
    print(f'Soma dos valores na lista: {sum(List_values)}')
    print(f'Média da lista: {average}')
    print(f'O Valor maximo: {max(List_values_salaries)}')
    print(f'O Valor minimo: {min(List_values_salaries)}')
    print(f'A mediana: {median}')
    print(f'Variância: {variance}')
    print(f'Desvio padrão: {variance**0.5}')