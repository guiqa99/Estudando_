sal = float(input('Qual o salário do funcionário? R$ '))
aum = float(input('Qual a porcentagem? '))
sal_at = (sal * (aum + 100))/100
print('O funcionário que ganhava R${}, com {:.2f}% de aumento vai começar a receber R${:.2f}.'.format(sal, aum, sal_at))

'''vl = float(input('Valor?: '))
por = float(input('Porcentagem?: '))
tt = (vl * (por/100))
print('{:.0f}% de {:.1f} é igual {:.1f}.'.format(por, vl, tt))'''
