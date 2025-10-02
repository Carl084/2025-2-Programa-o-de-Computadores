x = int(input('Informe o primeiro numero:'))
y = int(input('Informe o segundo numero:'))

#Quadrante 1
if x>0 and y>0:
    print('O ponto está no quadrante 1.')
    
#Quadrante 2
elif x<0 and y>0:
    print('O ponto está no quadrante 2.')
    
#Quadrante 3
elif x<0 and y<0:
    print('O ponto está no quadrante 3.')

#Quadrante 4
elif x>0 and y<0:
    print('O ponto está no quadrante 4.')
    
#Sobre o eixo Y
elif x==0 and y<0 or y>0:
    print('O ponto está sobre o eixo Y.')

#Sobre o eixo X
elif y==0 and x<0 or x>0:
    print('O ponto está sobre o eixo X.')

#O ponto está na origem
else:
    print('O ponto está na origem.')