# palavra = str(input('Digite um nome: '))

# def calabreso():
  
#   if palavra[-1] == 'a':
#     palavra_nova = palavra[:-1] + 'o'
#     return f'Calma {palavra_nova}'
#   else:
#     palavra_nova = palavra + 'o'
#     return f'Calma {palavra_nova}'
  
# msg = calabreso()
# print(msg) a

def calabreso(palavra):
    if palavra[-1] == 'a':
        nova_palavra = "".join([palavra[:-1], 'o'])  # Substitui o último 'a' por 'o'
    else:
        nova_palavra = "".join([palavra, 'o'])  # Adiciona 'o' ao final da palavra
    return f'Calma {nova_palavra}'  # Retorna a mensagem com a nova palavra

palavra = input('Digite um nome: ')
msg = calabreso(palavra)
print(msg)
