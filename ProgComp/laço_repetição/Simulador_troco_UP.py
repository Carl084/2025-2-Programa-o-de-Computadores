
#Peço o valor da conta e da gorjeta
ValuePay = float(input('Qual foi o valor da conta?'))
tip = float(input('Quanto de gorjeta deseja dar?'))

#Calculo o total a pagar
TotalPay = ValuePay+tip

#inicio um ciclo para o pagamento
while True:
    #Selecionar a forma de pagamento
    PaymentMethod = input('Qual sera a forma de pagamento? (cartão ou dinheiro?)')  
    #Forma 'CARTÃO'
    if PaymentMethod.lower() == 'cartão':
        #Seleciona o formato do cartão
        form = input('Débito ou Crédito?')
        #No caso do debito
        if form.lower() == 'debito':
            print(f'Você pagou {TotalPay} no débito.')
            break
        #No caso do credito
        elif form.lower() == 'credito':
            print(f'Você pagou {TotalPay} no crédito')
            break
        #No caso de erros
        else:
            print('Opção inválida, tente novamente.')

    #Forma 'DINHEIRO'
    elif PaymentMethod.lower() == 'dinheiro':
        #Peço a quantia do dinheiro
        NoteValue = int(input('Quanto em dinheiro deseja pagar?'))
        #Calculo e obtenho o troco
        Change = NoteValue-TotalPay
        #Troco maior que zero
        if Change > 0:
            #informo o valor pago e troco
            print(f'Você pagou {NoteValue}, tudo foi {TotalPay} e o seu troco foi {Change}')
            break
        #Troco igual a zero
        elif Change == 0:
            print(f'Tudo certo, você pagou: {TotalPay}')
            break
        #Troco insuficiente
        else:
            print(f'Valor insuficiente, você precisa pagar: {TotalPay}')
    #Caso dé 'ERRO'
    else:
        print('Forma de pagamento inválido, tente novamente.')