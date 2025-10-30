'''
   Fazer um programa que solicite um número inteiro (n) e exiba os 
   n primeiros elementos da sequência de Fibonacci.

   Exemplo: n = 10

   Saída: 
      1, 1, 2, 3, 5, 8, 13, 21, 34, 55
'''

n = int(input('Digite um numero inteiro: '))

a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b