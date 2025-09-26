
ValuePay = float(input('Qual foi o valor da conta?'))
tip = float(input('Quanto de gorjeta deseja dar?'))

TotalPay = ValuePay+tip

while True:
    PaymentMethod = input('Qual sera a forma de pagamento? (cartão ou Físico?)')
    
    if PaymentMethod.lower() == 'cartão':
        form = input('Débito ou Crédito?')
        if form.lower() == 'debito':
            print(f'Você pagou {TotalPay} no débito.')
            break
        elif form.lower() == 'credito':
            print(f'Você pagou {TotalPay} no crédito')
            break
        else:
            print('Opção inválida, tente novamente.')
    elif PaymentMethod.lower() == 'físico':
        NoteValue = int(input('Quanto em dinheiro deseja pagar?'))
        Change = NoteValue-TotalPay
        if Change >= 0:
            print(f'Você pagou {NoteValue} e tudo foi {TotalPay}, seu troco foi {Change}')
            break
        elif Change < 0:
            print(f'Valor insuficiente, você precisa pagar {TotalPay}')
    else:
        print('Forma de pagamento inválido, tente novamente.')