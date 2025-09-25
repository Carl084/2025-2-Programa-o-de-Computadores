#Pedindo as medidas de base maior, a menos e altura
Lbase = float(input('Me de a medida da base maior:'))
Sbase = float(input('Me de a medida da base menor:'))
Height = float(input('Me de a medida da altura:'))

#Calculo da área
area = ((Lbase+Sbase)*Height)/2

#Print do resultado
print(f'A área do trapezio é {area:.1f}.')