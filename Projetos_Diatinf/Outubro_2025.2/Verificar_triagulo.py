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
import math
import sys

#Verificar sé ha uma possivel formação de um triagulo
def verificar_lados(a,b,c):
    if a + b > c or a + c > b or b + c > a:
        print('Os lados informados formam um triângulo.')
        return True
    else:
        print('Os lados informados não formam um triângulo válido.')
        return False

#Encontrar os angulos do triagulo
def Calcular_angulos(a,b,c):
    cosA = (b**2 + c**2 - a**2)/(2*b*c)
    cosB = (a**2 + c**2 - b**2)/(2*a*c)
    cosC = (a**2 + b**2 - c**2)/(2*a*b)

    A = math.degrees(math.acos(cosA))
    B = math.degrees(math.acos(cosB))
    C = math.degrees(math.acos(cosC))
    
    return A,B,C

#Classificar formato do triagulo
def classificacao_agulo(A,B,C):
    if A and B and C < 90:
        AngClass = 'Agudo'
    if A or B or C == 90:
        AngClass = 'Retângulo'
    if A or B or C > 90:
        AngClass = 'Obtuso'

    return AngClass

#classificar o tipo de triagulo
def classificacao_lados(a,b,c):
    if (a != b) or (a != c) or (b != c):
        LadClass = 'Escaleno'
    if a or b == c or b == a:
        LadClass = 'Isósceles'
    if a == b == c:
        LadClass = 'Equilátero'

    return LadClass

#Inicio
print('Vamos verificar o triagulo!')
try:
    #Pedir as info
    a = int(input('Informe o lado A:'))
    b = int(input('Informe o lado B:'))
    c = int(input('Informe o lado C:'))

#Verificar possiveis erros
except ValueError:
    sys.exit('Erro: informe apenas números inteiros.')
except Exception as strErro:
    sys.exit(f'{strErro}')

#Chamar as funcoes e imprimir os resultados
if verificar_lados(a,b,c):
    A,B,C = Calcular_angulos(a,b,c)
    AngClass = classificacao_agulo(A,B,C)
    LadClass = classificacao_lados(a,b,c)

    print(f'O triagulo é {LadClass} e {AngClass}')
    print(f'A área do triagulo é {a * b / 2}')
    print(f'O angulo A tem {A}°')
    print(f'O angulo B tem {B}°')
    print(f'O angulo C tem {C}°')
    print(f'A soma dos angulos é {A+B+C}°')