# from math import hypot
# co = float(input('Comprimento do  cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = hypot(co, ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

# co = float(input('Comprimento do  cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) **(1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

def func(x = 1, y = 2):
  x = x + y
  y += 1
  print(x, y)
func(y = 2, x = 1)
#output: 3 3