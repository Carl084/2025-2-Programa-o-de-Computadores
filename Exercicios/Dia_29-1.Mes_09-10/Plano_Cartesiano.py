#Peço as cordenadas X e Y
x = float(input('Informe a coordenada X:'))
y = float(input('Informe a coordenada Y:'))
#Quadrante 1
if (x and y>0):
    print('O ponto está no 1° quadrante.')
#Quadrante 2
elif (x<0) and (y>0):
    print('O ponto está no 2° quadrante.')
#Quadrante 3
elif (x and y<0):
    print('O ponto está no 3° quadrante.')
#Quadrante 4
elif (x>0) and (y<0):
    print('O ponto está no 4° quadrante.')
#Sobre o eixo Y
elif (x==0):
    print('O ponto está sobre o eixo Y.')
#Sobre o eixo X
elif (y==0):
    print('O ponto está sobre o eixo X.')
#O ponto está na origem
else:
    print('O ponto está na origem.')