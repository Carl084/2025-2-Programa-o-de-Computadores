'''
   Fazer um programa que leia o conteúdo do arquivo resumo_lotr.txt e imprima na tela.
'''

import os,sys
from pathlib import Path

try:
   diretorio = os.path.dirname(__file__)
   arqLeitura =  open(f'{diretorio}/resumo_lotr.txt','r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('ERRO: Arquivo não encontrado!')
except Exception as e:
   sys.exit(f'ERRO: {e}')
   
else:
   conteudo = arqLeitura.read()
   print(conteudo)
   arqLeitura.close()