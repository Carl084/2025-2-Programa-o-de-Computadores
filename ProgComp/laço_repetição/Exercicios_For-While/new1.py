import sys

strtexto=input('Digite uma palavra: ').lower()

if ' ' in strtexto:
    sys.exit('Voce digitou mais de uma palavra ou apague o espaço')

strtextoinvertido=strtexto[::-1]
print(strtexto)
print(strtextoinvertido)
if strtexto==strtextoinvertido:
    print('É um Palidromo.')
else:
    print('Não é um Palidromo.')
    
    