'''
    Pedir ao usuário para inserir um ano
    determina se ele é bissexto ou não 
   
    Regras de um ano bissexto:

      - É divisível por 4
      - Não é divisível por 100.
      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
    O programa deve exibir "O ano [ano] é bissexto."
    ou 
    "O ano [ano] não é bissexto.". 
   
    Usas try...except para validar a entrada.
'''

import sys

#Função para verificar ano bissexto
def verificar_ano(ano):
    #Verificar se é divisivel por 4 e por 400
    #Sé é dividido por 100
    if(ano%4==0)and(ano%100!=0)or(ano%400==0):
        return True
    else:
        return False

try:
    #Verificar possiveis erros
    ano = int(input('Digite um ano:'))

except ValueError:
    sys.exit('Erro: Digite apenas numeros inteiros')
except Exception as strErro:
    sys.exit(f'{strErro}')

if ano<0:
    sys.exit(f'Erro: digite um ano D.C.')

#Chamar função para verificar
#Imprimir de acordo com True ou False
if verificar_ano(ano):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')