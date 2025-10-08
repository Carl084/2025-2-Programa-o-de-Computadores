#Valor a converter para o dolar.
valueConvert = float(input('Insira o valor a converter em reais:'))
DolarValue = float(input('Insira o valor do dola atual:'))

#Calculo para a converção
ResultDiv = valueConvert/DolarValue

#Print do resultado
print(f'Você tinha {valueConvert} reais, que é {ResultDiv:.3f} dolares.')
