
# Massa magra = peso * (1 - percentual de gordura)
# Gordura = peso * percentual de gordura
# Peso ideal = imc desejado * (altura ** 2)
# Gordura a perder = peso atual - peso ideal
# Percentual de gordura = (1.2 * imc) + (0.23 * idade) - (10.8 * sexo) - 5.4
# Massa muscular = peso - gordura

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        status = 'Abaixo do peso'
    elif imc < 25:
        status = 'Peso normal'
    elif imc < 30:
        status = 'Sobrepeso'
    else:
        status = 'Obesidade'
    return imc, status

def calcular_percentual_gordura(imc, idade, sexo):
    percentual = (1.2 * imc) + (0.23 * idade) - (10.8 * sexo) - 5.4
    return percentual

def calcular_peso_ideal(altura, imc_desejado=21):
    peso_ideal = imc_desejado * (altura ** 2)
    return peso_ideal

def calcular_gordura(peso, percentual_gordura):
    gordura = peso * (percentual_gordura / 100)
    return gordura

def calcular_massa_magra(peso, percentual_gordura):
    massa_magra = peso * (1 - percentual_gordura / 100)
    return massa_magra

def calcular_gordura_a_perder(peso_atual, peso_ideal):
    gordura_a_perder = peso_atual - peso_ideal
    return gordura_a_perder

peso = float(input('Digite seu peso(Kg):'))
altura = float(input('Digite sua altura(m):'))
idade = int(input('Digite sua idade:'))
sexo = int(input('Digite 1 para masculino e 0 para feminino:'))
imc, status = calcular_imc(peso, altura)
percentual_gordura = calcular_percentual_gordura(imc, idade, sexo)
peso_ideal = calcular_peso_ideal(altura)
gordura = calcular_gordura(peso, percentual_gordura)
massa_magra = calcular_massa_magra(peso, percentual_gordura)
gordura_a_perder = calcular_gordura_a_perder(peso, peso_ideal)

print(f'Seu IMC é {imc:.2f}, você está classificado como: {status}')
print(f'Seu percentual de gordura é: {percentual_gordura:.2f}%')
print(f'Seu peso ideal é: {peso_ideal:.2f} Kg')
print(f'Sua massa magra é: {massa_magra:.2f} Kg')
print(f'Sua gordura corporal é: {gordura:.2f} Kg')
print(f'Sua gordura a perder para atingir o peso ideal é: {gordura_a_perder:.2f} Kg')