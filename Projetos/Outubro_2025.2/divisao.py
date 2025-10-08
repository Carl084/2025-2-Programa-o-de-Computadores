import sys

try:
   #Solicitar os números que serão parte da divisão
   dividendo = int(input('Informe o dividendo: '))
   divisor = int(input('Informe o divisor: '))
   
   #Calculo para encontrar o resultado
   quociente = dividendo/divisor

#Verrificar possiveis erros
except ZeroDivisionError:
   sys.exit('ERRO: Divisão por "zero" não é permitida.')
except ValueError:
   sys.exit('ERRO: Informe apenas números inteiros.')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')

#Imprimir o resiltado
else:
   print(f'{dividendo}/{divisor}={quociente:.2f}')