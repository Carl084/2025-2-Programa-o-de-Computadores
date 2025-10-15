'''
    Instruções:
        - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
        - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
        - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
        - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
        - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

    Observações:
        - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
        - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
        - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
        - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
        - Considere que os ângulos são expressos em graus.

    Dica: Utilize a biblioteca math.S
    https://docs.python.org/3/library/math.html
'''

import sys

def veriicar_lados(IntladoA, IntladoB, IntladoC):
    if IntladoA and IntladoB >= IntladoC:
        return True
    elif IntladoA and IntladoC >= IntladoB:
        return True
    elif IntladoC and IntladoB >= IntladoA:
        return True
    else:
        return False

def calcular_cosseno(IntladoA, IntladoB, IntladoC):
    

try:
    print('Vamos verificar o triagulo!')
    IntladoA = int(input('Informe o lado A:'))
    IntladoB = int(input('Informe o lado B:'))
    IntladoC = int(input('Informe o lado C:'))

except ValueError:
    sys.exit('Erro: informe apenas números inteiros.')
except Exception as strErro:
    sys.exit(f'{strErro}')

if veriicar_lados(IntladoA, IntladoB, IntladoC):
