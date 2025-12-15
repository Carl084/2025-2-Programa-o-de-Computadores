import sys

#Solicitar o raio do circulo
try:
   raio = float(input('Informe o raio: '))

#Verificar possiveis erros
except ValueError:
   sys.exit('EXCEÇÃO: ValueError -> Informe apenas valores númericos válidos...')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}\nEntre em Contato com o setor de desenvolvimento...')

#Verificar raio negativo
if raio <= 0:
      sys.exit('ERRO: O Raio deve ser positivo...')

#Calcular e imprimir o resultado
else:
   area = 3.1416 * raio ** 2
   print(f'A área do círculo de raio = {raio} é {area:.2f}')