'''
   Programa para exibir a tabua de multiplicação de um número
'''

intmultiplicando=1
intmultiplicador=6

# definir loop
# exibir a tabuada do 6 enquanto o multplicador for menor ou igual a 10
while intmultiplicando <= 10:
    # calculo do prduto
    intproduto = intmultiplicador * intmultiplicando

    # imprimir resultado
    print(f'{intmultiplicador} x {intmultiplicando} = {intproduto}')

    # incremento do multiplicando
    intmultiplicando += 1