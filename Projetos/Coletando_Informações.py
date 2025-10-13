Lista_alunos = []

def media(n1, n2, n3, n4):
    medianotas = (n1 + n2 + n3 + n4) / 4
    return medianotas

def situacao(resultado):
    if resultado >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def cadastra_aluno ():
    while True:
        nome = input('Digite o nome do aluno (ou "fim" para emcerrar): ')
        if nome.lower() == 'fim':
            break

        n1 = float(input('Diga a nota 1° bimestre:'))
        n2 = float(input('Diga a nota 2° bimestre:'))
        n3 = float(input('Diga a nota 3° bimestre:'))
        n4 = float(input('Diga a nota 4° bimestre:'))

        m = media (n1, n2, n3, n4)
        resultado = situacao (m)

        aluno = {
            'nome': nome,
            'notas': [n1, n2, n3, n4],
            'situacao': resultado
        }

        Lista_alunos.append(aluno)
while True:
    print('1. Registrar aluno.')
    print('2. Situação da lista dos alunos.')
    print('3. Encerrar.')
    escolha = input('O que deseja fazer?')

    if escolha == '1':
        cadastra_aluno()

    elif escolha == '2':
        print(Lista_alunos)

        reprovados = sum(1 for a in Lista_alunos if a['situacao'] == 'Reprovado')
        aprovados = sum(1 for a in Lista_alunos if a ['situacao'] == 'Aprovado')

        print(f'São {reprovados} Reprovados e {aprovados} Aprovados')
    
    elif escolha == '3':
        break
    
    else:
        print('Erro: Opção Invalida')