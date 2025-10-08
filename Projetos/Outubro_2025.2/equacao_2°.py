import sys
try:
    #Pedir os valores
    a = int(input('Digite o valor "a":'))
    b = int(input('Digite o valor "b":'))
    c = int(input('Digite o valor "c":'))
#Verificar erros
except ValueError:
    sys.exit('ERRO: Informe apenas números válidos para a, b e c')
except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')
#Verificar erro do a sendo 0
if a == 0:
    sys.exit('ERRO: A equação não é de 2° grau.')
#calculo do delta
delta = b**2-4*a*c
print(f'\nDelta (discriminante) = {delta}')
#Verificar o delta e ver as necessidades de calcular
if delta > 0:
    #Caso o delta tenha duas raizes
    raiz1 = (-b+(delta**0.5)) / (2*a)
    raiz2 = (-b-(delta**0.5)) / (2*a)
    print('A equação possui duas raizes reais distintas:')
    print(f'A raiz 1 é {raiz1}')
    print(f'A raiz 2 é {raiz2}')
elif delta == 0:
    #Delta com raiz unica
    raiz = -b/(2*a)
    print('A equação possui uma unica raiz.')
    print(f'Raiz da equação é {raiz}')
else:
    #Não há raizes
    print('A equação não há raizes reais.')