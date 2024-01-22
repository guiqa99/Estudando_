# def encontra_par_soma(S, X):
#     # Inicializa os índices de início e fim da sequência
#     inicio = 0
#     fim = len(S) - 1

#     while inicio < fim:
#         # Calcula a soma dos elementos nos índices inicio e fim
#         soma_atual = S[inicio] + S[fim]

#         # Verifica se a soma é igual a X
#         if soma_atual == X:
#             return True  # Encontrou um par com a soma desejada
#         elif soma_atual < X:
#             inicio += 1  # Aumenta o índice de início para aumentar a soma
#         else:
#             fim -= 1  # Diminui o índice de fim para diminuir a soma

#     return False  # Não encontrou um par com a soma desejada

# # Exemplo de uso
# sequencia = [1, 2, 3, 4, 5]
# X = 8
# resultado = encontra_par_soma(sequencia, X)

# print(resultado)

#BUSCA LINEAR
numeros = [10, 12, 16, 18, 22]
valorBuscado = [9]

def buscaLinear():
    for numero in numeros:
        if numero == valorBuscado:
            return True
        else:
            if numero > valorBuscado:
                return False


    