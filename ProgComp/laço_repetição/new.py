'''
    strtexto='natal'
    for letra in strtexto:
        print(letra)
        
    for letra in strtexto:
        print(letra,end='')
'''

strtexto = input('Digite algo')
aux=''

for palavra in strtexto:
    '''
        if palavra !=' ':
            print(palavra,end='')
        else:
            print()
    '''
        
    print(palavra,end='' if palavra!=' ' else '\n')
                        #I________________________I Ternáriostrtexto = input('Digite algo')