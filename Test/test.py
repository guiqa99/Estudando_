# Palestras = ['Django', 'Java', 'React', 'docker', 'PHP'] # lista declarada
# print(Palestras)
# print(Palestras[-5]) #imprimindo o objeto na posição -5 da lista.
# Palestras[0] = 'C#' # alterando da posição zero ou -5 de Django para C#.
# Palestras[3] = 'Dockers'
# for i in range(0, len(Palestras)):
#     print('Palestras de :', Palestras[i])

lista = list(range(6))
comprimento = 6

while len(lista) == comprimento:
    print(lista)
    lista.append('item')
else:
    print(f'O comprimento da Lista é {len(lista)} e ultrapassou {comprimento}!')
    print(lista)