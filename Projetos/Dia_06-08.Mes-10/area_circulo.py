#Importação modulo sys
import sys

try:
   raio = float(input('Informe o raio: '))
except ValueError:
   sys.exit('EXCEÇÃO: ValueError -> Informe apenas valores númericos válidos...')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}\nEntre em Contato com o setor de desenvolvimento...')
else:
   if raio <= 0:
      sys.exit('ERRO: O Raio deve ser positivo...')

   area = 3.1416 * raio ** 2
   
   print(f'A área do círculo de raio = {raio} é {area:.2f}')