#Peço a temporatura em C°
temp = float(input('Informe a temperatura em Celsius:'))

#Faço o calculo de converção
tempF = (temp * 9/5) + 32

#Informo a temperatura
print(f'A temperatura em Fahrenheit é {tempF:.1f}')