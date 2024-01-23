sal = float(input('Qual o salário do funcionário? R$ '))
aum = float(input('Qual a porcentagem? '))
sal_at = (sal * (aum + 100))/100
print('O funcionário que ganhava R${}, com {:.0f}% de aumento vai começar a receber R${:.2f}.'.format(sal, aum, sal_at))
