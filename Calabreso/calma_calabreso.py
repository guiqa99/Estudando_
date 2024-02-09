palavra = str(input('Digite um nome: '))

def calabreso():
  
  if palavra[-1] == 'a':
    palavra_nova = palavra[:-1] + 'o'
    return f'Calma {palavra_nova}'
  else:
    palavra_nova = palavra + 'o'
    return f'Calma {palavra_nova}'
  
msg = calabreso()
print(msg)