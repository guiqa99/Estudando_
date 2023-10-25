prod = float(input('Qual o preço do produto? R$ '))
# desc = prod - (prod * 5/100)
desc = 5/100
newprod = prod - (prod * desc)
print("O produto que custava R$ {}, na promoção com {:.2f}% de desconto, vai custar R$ {:.2f}.".format(prod, desc, newprod))