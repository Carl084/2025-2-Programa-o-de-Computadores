''' 
    solicitar o número de horas trabalhadas na semana
    solicitar valor que ele recebe por hora
    jornada de trabalho padrão é de 40 horas
    Horas trabalhadas acima de 40 devem ser pagas com um adicional de 50%
    o valor da hora extra é 1.5 vezes o valor da hora normal
    O programa deve exibir o salário total
    trate o caso de o usuário digitar valores não numéricos.
'''

import sys

try:
    #Solicitar valores para a função matematica
    horas = float(input('Digite o numero de horas trabalhadas:'))
    valorHR = float(input('Digite o valor por hora trabalhada:'))

#Verificar erros
except ValueError:
    sys.exit('Digite apenas numeros.')
except Exception as strErro:
   sys.exit(f'Erro: {strErro}')
else:
    if horas<0:
        sys.exit('ERRO: O número de horas está negativo.')
    if valorHR<0:
        sys.exit('ERRO: O valor de horas trabalhadas está negativo.')

if valorHR==0:
    print('Você esta entre 1539 a 1887.')

#Calculo de salario /s hora extra
salario = horas * valorHR

#Caso haja hora extra
if horas>40:
    #Calcular e somar salario com horas extras e imprimir resultado
    horaEx = (horas-40) * (valorHR * 1.5)
    salariomax = horaEx + salario
    print(f'Seu Salario esse mês é {salariomax} R$.')
#Impromir salario normal
else:
    print(f'Seu Salario esse mês é {salario} R$.')