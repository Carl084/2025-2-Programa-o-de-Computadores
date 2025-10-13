'''
    Solicitar a masa e a altura
    Calcular o IMC
    Exibir valor e classificação

        - Abaixo de 18.5: Abaixo do peso
        - 18.5 a 24.9: Peso ideal
        - 25.0 a 29.9: Sobrepeso
        - 30.0 a 34.9: Obesidade Grau I
        - Acima de 35.0: Obesidade Grau II
    
    Tratar entradas inválidas e a altura ser maior que zero
'''

import sys

def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    if imc<18.5:
        situacao = 'Abaixo do peso'
    elif imc<25:
        situacao = 'Peso ideal'
    elif imc<35:
        situacao = 'Obesidade 1°'
    else:
        situacao = 'Obesidade 2°'
    return imc, situacao

try:
    peso = float(input('Digite seu peso (Kg):'))
    altura = float(input('Digite sua altura (Metro):'))
except ValueError:
    sys.exit('Erro: Digite apenas numeros.')
except Exception as strErro:
    sys.exit(f'Erro: {strErro}')
if altura<0.40:
    sys.exit('Erro de altura: um recém-nascido tem entre 45 a 55 cm.')
if peso<1:
    sys.exit('Erro no massa corporal: está muito leve!')

imc, situacao = calcular_imc(peso, altura)

print(f'Seu IMC é {imc:.1f} e está na classificação de {situacao}.')