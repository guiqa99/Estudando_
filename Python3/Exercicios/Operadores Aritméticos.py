#Ordem de Precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4- +, -
# n = 5 + 3 * 2
# n2 = 3 * 5 + 4 ** 2
# n3 = 3 * (5 + 4) ** 2
# print(n2)
# name = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:20}!'.format(name))
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end='! ')
print('Divisão inteira {} e potência {:2}'.format(di, e))
