'''
   Fazer um programa que leia o arquivo valores_1.txt, que contém números inteiros,
   um por linha, e calcule a soma desses números. O programa deve exibir o resultado na tela.
'''

import os,sys

try:
   diretorio = os.path.dirname(__file__)
   arqLeitura =  open(f'{diretorio}/valores_2.txt','r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('ERRO: Arquivo não encontrado!')
except Exception as e:
   sys.exit(f'ERRO: {e}')
   
else:
   lstNumeros = []
   while True:
      strLinha = arqLeitura.readline().split()
      if not strLinha: break
      
      intValor = int(strLinha)
      
      lstNumeros.append(intValor)
   
   arqLeitura.close()
   print(lstNumeros)