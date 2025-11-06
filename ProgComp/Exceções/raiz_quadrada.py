import sys

try:
   #Solicitar um valor
   Valor = int(input('Informe um valor inteiro: '))
    
   #Exceção para números negativos
   if Valor < 0:
       raise Exception('NegativeSquareRoot')
   
   #Calcular a raiz
   RaizQuadrada = Valor**0.5

#Verificar se há erros
except ValueError:
   sys.exit('ERRO: Por favor, insira apenas números inteiros.')
except Exception as strErro:
   
   #Retornar o erro do número negativo
   if str(strErro) == 'NegativeSquareRoot':
       sys.exit('ERRO: Não há Raiz Real para números negativos...')
   else:
       sys.exit(f'ERRO: {strErro}')

#Imprimir resultado da raiz quadrada
else:
   print(f'A raiz quadrada de {Valor} é {RaizQuadrada:.2f}')