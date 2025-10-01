while True:
    #Pedindo as notas
    note1 = int(input('Informe a nota da etapa 1:'))
    note2 = int(input('Informe a nota da etapa 2:'))
    if not note1>=0 and not note2<=100 and not note2>=0 and not note2<=100:
        print('Nota 1 ou 2 ultrapassou o limite')
    #Pedindo a carga horaria e faltas do aluno
    workload = int(input('Infome a carga horaria da diciplina (h/a):'))
    lack = int(input('Informe a quantidade de faltas do aluno:'))
    if not workload>=0:
        print('Uma carga horaria negativa???')
    if not lack>=0 and not lack>workload:
        print('A quantidade de faltas passou o limite existente.')
    #Calculando a media das notas
    average = int((note1*2 + note2*3)/5)
    frequency = int((1-(lack/workload))*100)
    #Informando o resultado da nota
    print(f'Sua media na Diatinf é {average} e tem uma frequencia de {frequency}%.')
    #Caso seja aprovado
    if average>=60 and frequency>=75:
        print('Você está aprovado')
        break
    #Caso esteja em recuperação
    elif average>=20 and frequency>=75:
        print('Você está em recuperação')
        break
    #Caso seja reprovado
    else:
        print('Você está reprovado')
        break