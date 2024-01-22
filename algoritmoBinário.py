def buscaBinaria(numeros: [int], valorProcurado: int):
    
    inicio = 0
    meio = []
    fim = numeros.cont - 1
    
    while inicio <= fim(meio = inicio + fim / 2):
        
        if numeros == valorProcurado:
           return True 
        
        if numeros < valorProcurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return False