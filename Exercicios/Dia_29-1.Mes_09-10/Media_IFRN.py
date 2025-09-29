#Pedindo as notas
Nota1 = int(input('Informe a nota da etapa 1:'))
Nota2 = int(input('Informe a nota da etapa 2:'))

#Calculando a media das notas
Media = (Nota1*2 + Nota2*3)/5

#Informando o resultado da nota
print(f'Sua media na Diatinf é {Media}')

#Caso seja aprovado
if Media>=60:
    print('Você está aprovado')
#Caso esteja em recuperação
elif Media>=20:
    print('Você está em recuperação')
#Caso seja reprovado
else:
    print('Você está reprovado')