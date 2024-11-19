totM = totH = 0
while True:
    
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input( 'Sexo: [Masculino/Feminino]')).strip().upper()[0]
    if sexo == 'M':
        totH += 1 
    if sexo == 'F':
        totM += 1 
        
    pesquiza = ' ' 
    while pesquiza not in 'SNI':
        pesquiza = str(input( 'Gostou do novo produto da empresa cara de pau?')).strip().upper() [0]
    
    resp = ' '   
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de mulheres:{totM}')
print(f'Total de homens:{totH}')
print(f'Ao todo temos {totM} mulheres e {totH} homens entrevistados \n')






